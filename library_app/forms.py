from django import forms
from .models import IssuedBook

class IssueBookForm(forms.ModelForm):
    class Meta:
        model = IssuedBook
        fields = ['student', 'book']