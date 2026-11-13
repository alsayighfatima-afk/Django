from django.db import models
from django.utils.timezone import now

class Course(models.Model):
    name = models.CharField(max_length=200)
    # ... الحقول الأخرى الموجودة أصلاً في المشروع ...

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # ...

# النماذج المطلوبة في المشروع
class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class Submission(models.Model):
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE) # افترض وجود Enrollment
    choices = models.ManyToManyField(Choice)