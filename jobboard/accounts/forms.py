from django import forms
from django.contrib.auth import password_validation, get_user_model
from django.core.exceptions import ValidationError
from .models import AdvUser
from .dispatch import dp_send_mes


class UserRegisterForm(forms.ModelForm):
    """
        Форма регистрации пользователя
    """
    password1 = forms.CharField(label='Пароль',
                                widget=forms.widgets.PasswordInput(),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль(поовторно)',
                                widget=forms.widgets.PasswordInput())
    phone = forms.CharField(max_length=20,
                            label='Телефон',
                            widget=forms.widgets.TextInput())
    avatar = forms.ImageField(label='Аватар')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data['password2']
        user = get_user_model()
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Введенные пароли не совпадают',
                                                   code='password_mismatch')}
            raise ValidationError(errors)
        if user.objects.filter(email=self.cleaned_data.get('email')).exists():
            errors = {'email': ValidationError('Введенные email уже существует')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        if commit:
            user.save()
        dp_send_mes.send_messages.send(sender=self.__class__, user=user)
        return user

    class Meta:
        model = AdvUser
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'type_user',
                  'phone',
                  'avatar',
                  'password1',
                  'password2')


class UserUpdateForm(forms.ModelForm):
    """
        Форма изменения данных пользователя
    """

    class Meta:
        model = AdvUser
        fields = ('first_name',
                  'last_name',
                  'phone',
                  'avatar')
