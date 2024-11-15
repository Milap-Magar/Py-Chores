from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.course, name='course'),
    path('category/<slug:slug>', views.category, name='category'),
    path('modelsets/<int:id>/', views.modelsets, name='modelsets'),
    path('play/<int:id>/', views.mcq, name='mcq'),
    path('result/', views.result_view, name='result'),
    path('download/<int:id>/', views.render_pdf_view, name='render_pdf'),
    path('courses/', views.courses, name='courses'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('syllabus-details/<int:id>', views.syllabus_details, name='syllabus-detail'),
]
