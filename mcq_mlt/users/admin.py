from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Student


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ('username', 'email', 'student_code', 'is_active', 'is_staff')
    list_filter = ('is_active', 'student_code', 'is_staff')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Student)
