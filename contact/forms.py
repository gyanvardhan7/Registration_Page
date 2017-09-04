from django import forms
from contact.models import member

class UserForm(forms.ModelForm):

    class Meta():
        model = member
        fields = ('name','email','contact','year','group','enroll')
        labels ={
        'name': ('Name'),
        'enroll': ('Enrollment No')
        }
        help_texts = {
        'year': ('Enter-First,Second,Third or Fourth')
        }
