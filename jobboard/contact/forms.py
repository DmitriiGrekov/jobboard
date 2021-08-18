from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
        Форма обратной связи
    """
    message = forms.CharField(max_length=5000,
                              widget=forms.widgets.Textarea(attrs={'class': 'form-control w-100',
                                                                   'cols': 30,
                                                                   'rows': 9,
                                                                   'onfocus': "this.placeholder = ''",
                                                                   'onblur': "this.placeholder = 'Enter Message'",
                                                                   'placeholder': 'Enter Message'}))
    name = forms.CharField(max_length=120,
                           widget=forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                 'onfocus': "this.placeholder = ''",
                                                                 'onblur': "this.placeholder = 'Enter your name'",
                                                                 'placeholder': 'Enter your name'}))
    email = forms.EmailField(max_length=120,
                             widget=forms.widgets.EmailInput(attrs={'class': 'form-control',
                                                                    'onfocus': "this.placeholder = ''",
                                                                    'onblur': "this.placeholder = 'Enter your email'",
                                                                    'placeholder': 'Enter your email'}))
    subject = forms.CharField(max_length=1000,
                              widget=forms.widgets.TextInput(attrs={'class': 'form-control',
                                                                    'onfocus': "this.placeholder = ''",
                                                                    'onblur': "this.placeholder = 'Enter Subject'",
                                                                    'placeholder': 'Enter Subject'}))

    class Meta:
        model = ContactMessage
        fields = ('message',
                  'name',
                  'email',
                  'subject')
