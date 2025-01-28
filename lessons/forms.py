from django import forms
from .models import Lesson, Answer
from tests.models import Test, Question
from tests.forms import QuestionForm


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
            'description': forms.Textarea(attrs={'class': 'w-full border border-gray-300 rounded p-2', 'rows': 4}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Lesson name must be at least 3 characters long.")
        return name


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'w-full border border-gray-300 rounded p-2'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 1:
            raise forms.ValidationError("Answer text cannot be empty.")
        return text


AnswerFormSet = forms.inlineformset_factory(
    Question, Answer, form=AnswerForm, extra=2, can_delete=True, min_num=2, validate_min=True
)

QuestionFormSet = forms.inlineformset_factory(
    Test, Question, form=QuestionForm, extra=1, can_delete=True, min_num=1, validate_min=True
)

