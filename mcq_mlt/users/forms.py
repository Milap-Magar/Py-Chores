from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'gender',
            'phonenumber',
            'is_EDUMLT_student',
            'student_code',
            'heard_from'
        )

        def __init__(self, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ContactUsForm(forms.Form):
    full_name = forms.CharField(max_length=90)
    email = forms.EmailField()
    phone_number = forms.IntegerField(required=False)
    message = forms.CharField(widget=forms.Textarea)