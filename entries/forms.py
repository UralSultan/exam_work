from django import forms
from .models import GuestbookEntry

class SearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=100,
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя автора...'
        })
    )

class GuestbookEntryForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ('author_name', 'author_email', 'content')
        labels = {
            'author_name': 'Имя',
            'author_email': 'Email',
            'content': 'Текст',
        }
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class DeleteEntryForm(forms.Form):
    author_email = forms.EmailField(
        label='Email автора',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )