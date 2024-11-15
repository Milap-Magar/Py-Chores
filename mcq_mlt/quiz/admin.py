from csv import list_dialects
from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Questions, StudentGroup
from .models import *

class QuestionsResource(resources.ModelResource):

    class Meta:
        model = Questions
        fields = ('question_statement', 'choice_1', 'choice_2', 'choice_3', 'choice_4', 'answer', 'explanation')
        
        
class QuestionsAdmin(ImportExportModelAdmin):
    resource_class = QuestionsResource
    list_display = ('less_question_st', 'modelset', ) 
    list_filter = ('modelset',)

    def less_question_st(self, obj):
        """ show only first 50 characters of question"""
        """ also render html"""
        return format_html(f'{obj.question_statement[:70]}')
admin.site.register(Questions, QuestionsAdmin)



class ResultAdmin(admin.ModelAdmin):
    model = Result
    list_display = ('user', 'modelset' ,'markes_obtained', 'datetime')
    list_filter = ('datetime', 'modelset')


class ModelsetAdmin(admin.ModelAdmin):
    model = Modelset
    list_display = ('modelset_title', 'course', 'category', 'active')
    list_filter = ('active', 'course', 'category')
 
# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(StudentGroup)
admin.site.register(Modelset, ModelsetAdmin)
admin.site.register([CourseSyllabus, Syllabus, QuizGroup])
# admin.site.register(Questions, QuestionAdmin)
admin.site.register(QOTD)
admin.site.register(Result, ResultAdmin)
