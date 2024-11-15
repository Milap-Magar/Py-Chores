from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.subject, name='subject'),
    path('unit/<int:id>', views.unit, name='unit'),
    path('chapter/<int:id>', views.chapter, name='chapter'),
    path('chapter-details/<int:id>/', views.chapterdetails, name='chapterdetails'),
    path('read-completed/<int:id>/', views.read_completed_chapter, name='readcompleted'),
    path('chapterwisemcqsplay/<int:id>/', views.chapterwise_mcq, name='chapterwisemcq'),
    # path('download/<int:id>/', views.render_pdf_view, name='render_pdf'),
    # path('courses/', views.courses, name='courses'),
    # path('syllabus/', views.syllabus, name='syllabus'),
    # path('syllabus-details/<int:id>', views.syllabus_details, name='syllabus-detail'),
]
