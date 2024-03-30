from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('login/',views.user_login, name='user_login'),
    path('logout/',views.user_logout, name='user_logout'),
    path('',views.index, name='index'),
    
    path('password_change/', 
    auth_view.PasswordChangeView.as_view(template_name='users/password_change_form.html'),
    name='password_change'),
    path('password_change_done/',
         auth_view.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change/done/'),
    path('password_reset/',
         auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    
    path('register/', views.user_register, name='user_register'),
]