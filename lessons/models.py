from django.db import models
from django.core.exceptions import ValidationError
from tests.models import Question
from .base_models import BaseModel


class Lesson(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question}: {self.text[:50]}"

    def clean(self):
        if self.is_correct and self.question.answers.filter(is_correct=True).exclude(pk=self.pk).exists():
            raise ValidationError("There can only be one correct answer per question.")

