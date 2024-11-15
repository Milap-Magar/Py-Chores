from django.contrib import admin
from django.utils.html import format_html

from .models import *

class AboutAdmin(admin.ModelAdmin):
    model = About
    # question_statement is replaced with less_question_st
    list_display = ('less_about_content', )

    def less_about_content(self, obj):
        """ show only first 50 characters of question"""
        """ also render html"""
        return format_html(f'{obj.about_mcqmlt[:150]}...')

admin.site.register(About, AboutAdmin)
admin.site.register(Team)
admin.site.register(Advisors)