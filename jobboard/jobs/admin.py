from django.contrib import admin
from .models import JobCategory, JobModel, ResumeModel, ResumeMessageModel


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(JobModel)
class JobModelAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'date_publish',
                    'salary_min',
                    'salary_max',
                    'experience',
                    'employment',)
    list_display_links = ('title',
                          'date_publish',
                          'salary_min',
                          'salary_max',
                          'experience',
                          'employment')
    list_filter = ('gender',
                   'experience',
                   'employment',
                   'date_publish',)
    search_fields = ('title',
                     'responsibility',
                     'qualifications',
                     'benefits')


@admin.register(ResumeModel)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('full_name',
                    'email',
                    'vacancy',)
    search_fields = ('full_name',) 


@admin.register(ResumeMessageModel)
class ResumeMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'resume',)
