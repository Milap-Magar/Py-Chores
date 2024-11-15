from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from courses import views

from django.conf.urls.static import static
from django.conf import settings
from django.urls import path


urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
    path('subjects/', include('courses.urls')),
    path('accounts/', include('allauth.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),

    
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html', 
        redirect_authenticated_user=True), 
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # for password update 
    path(
        "password_change/", 
        auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), 
        name="password_change"
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
        name="password_change_done",
    ),

    # urls for password reset
    path(
        "password_reset/", 
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
        name="password_reset"
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name="password_reset_complete",
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# site dashboard configurations
admin.site.site_header  =  "MCQMLT ADMIN"  
admin.site.site_title  =  "MCQMLT ADMIN"
admin.site.index_title  =  "MCQMLT ADMIN"

# views for error pages
handler404 = 'users.views.custom_page_not_found_view'
handler500 = 'users.views.custom_error_view'