from pyexpat import model
from django.contrib import admin
from .models import *


class ChapterAdmin(admin.ModelAdmin):
    model = Chapters
    list_display = ('name', 'subject', 'unit')
    list_filter = ('subject', 'unit')

class UnitAdmin(admin.ModelAdmin):
    model = Units
    list_display = ('name', 'subject')
    list_filter = ('subject',)

class ChapterWiseModelsetAdmin(admin.ModelAdmin):
    model = ChapterWiseModelset 
    list_display = ('modelset_title', 'chapter')
    list_filter = ('chapter',)

class QuestionAdmin(admin.ModelAdmin):
    model = Questions 
    list_display = ('question_statement', 'modelset')
    list_filter = ('modelset',)

admin.site.register([Subjects, SubjectGroup])
admin.site.register(Units, UnitAdmin)
admin.site.register(Chapters, ChapterAdmin)
admin.site.register(ChapterWiseModelset, ChapterWiseModelsetAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(UsersReadChapters)
