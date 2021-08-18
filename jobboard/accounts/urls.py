from django.urls import path
from .views import (UserLoginView,
                    UserLogoutView,
                    UserRegisterView,
                    UserPasswordChangeView,
                    UserProfileView,
                    UserUpdateView,
                    ShowFavourtisView,
                    ShowResumeView,
                    ShowUserVacancy,
                    add_favourits_jobs,
                    delete_favourits,
                    delete_resume_view,
                    delete_jobs_user, 
                    detail_resume_view,
                    view_all_responses,
                    activate_user)


app_name = 'accounts'
urlpatterns = [
   path('login/', UserLoginView.as_view(), name='login'),
   path('logout/', UserLogoutView.as_view(), name='logout'),
   path('register/', UserRegisterView.as_view(), name='register'),
   path('register/activate/<str:token>/',
        activate_user,
        name='register_activate'),
   path('change_password/',
        UserPasswordChangeView.as_view(),
        name='change_password'),
   path('profile/', UserProfileView.as_view(), name='profile'),
   path('profile/update/<int:pk>/', UserUpdateView.as_view(), name='update'),
   path('add/favourits/<int:pk>/', add_favourits_jobs, name='add_favourits'),
   path('show_favourits/', ShowFavourtisView.as_view(), name='show_favourits'),
   path("delete_favourits/<int:pk>/",
        delete_favourits,
        name='delete_favourits'),
   path('show_resume/', ShowResumeView.as_view(), name='show_resume'),
   path('show_resume/detail/<int:pk>/',
        detail_resume_view,
        name='detail_resume'),
   path('delete_resume/<int:pk>/',
        delete_resume_view,
        name='delete_resume'),
   path('show_jobs/', ShowUserVacancy.as_view(), name='show_jobs'),
   path('delete_jobs/<int:pk>/', delete_jobs_user, name='delete_jobs'),
   path('view_all_response/', view_all_responses, name='all_responses')
]