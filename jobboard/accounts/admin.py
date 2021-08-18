from django.contrib import admin
from .models import AdvUser


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'email',
                    'phone',
                    'last_login')
    list_display_links = ('first_name',
                          'last_name',
                          'email',
                          'phone')
    list_filter = ('last_login',)
    search_fields = ('first_name',
                     'last_name',
                     'email',
                     'phone',)
