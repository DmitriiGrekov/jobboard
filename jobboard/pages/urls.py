from django.urls import path
from .views import CandidatesView


app_name = 'pages'
urlpatterns = [
    path('candidates/', CandidatesView.as_view(), name='list'),
]
