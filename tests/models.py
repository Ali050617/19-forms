from django.db import models
from lessons.base_models import BaseModel


class Test(BaseModel):
    name = models.CharField(max_length=100)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE, related_name='tests')

    def __str__(self):
        return self.name


class Question(BaseModel):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return f"{self.test.name}: {self.text[:50]}"
