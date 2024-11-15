from django.urls import path

from .views import index, signupview, verify_registered_email
from . import views

app_name='users'
urlpatterns = [
    path('', index, name='index'),
    path('about-us/', views.about, name='about'),
    path('history/', views.history, name='history'),
    path('contact-us/', views.contact, name='contact'),
    path('user/register', signupview, name='register'),
    # path('category/<slug:slug>', views.category, name='category'),
    # path('modelsets/<int:id>/', views.modelsets, name='modelsets'),
    # path('play/<int:id>/', views.mcq, name='mcq'),
    path('activate/<uidb64>/<token>', verify_registered_email, name='activate'), 
]
