from django import forms
from .models import Test, Question


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'lesson']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
            'lesson': forms.Select(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Test name must be at least 3 characters long.")
        return name


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'w-full border border-gray-300 rounded p-2', 'rows': 3}),
        }

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 10:
            raise forms.ValidationError("Question text must be at least 10 characters long.")
        return text

