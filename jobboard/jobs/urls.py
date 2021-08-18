from django.urls import path
from .views import (JobsListView,
                    JobsDetailView,
                    JobListFilterView,
                    create_job_view)


app_name = 'jobs'
urlpatterns = [
    path('filter/',  JobListFilterView.as_view(), name='filter'),
    path('', JobsListView.as_view(), name='list'),
    path('<int:pk>/', JobsDetailView.as_view(), name='detail'),
    path('create/new/jobs/', create_job_view, name='create'),
]
