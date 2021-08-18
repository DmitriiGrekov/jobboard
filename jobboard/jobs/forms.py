from django import forms
from .models import JobModel, ResumeModel, ResumeMessageModel


class ResumeForm(forms.ModelForm):
    portfolio_file = forms.FileField(widget=forms.widgets.FileInput(attrs={'class': "custom-file-input",
                                                                           'id': 'inputGroupFile03',
                                                                           'aria-describedby': 'inputGroupFileAddon03'}))

    class Meta:
        model = ResumeModel
        fields = ('full_name',
                  'email',
                  'portfolio_link',
                  'portfolio_file',
                  'coverletter')


class JobForm(forms.ModelForm):

    class Meta:
        model = JobModel
        fields = ('title',
                  'position',
                  'employment',
                  'description',
                  'category',
                  'experience',
                  'gender',
                  'responsibility',
                  'qualifications',
                  'benefits',
                  'vacancy',
                  'salary_min',
                  'salary_max',
                  'image')


class ResumeCommentForm(forms.ModelForm):

    class Meta:
        model = ResumeMessageModel
        fields = ('name', 'comment',)
