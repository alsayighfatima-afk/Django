from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# 1. نموذج الدورة
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default="Default description")
    # يمكنك إضافة حقول أخرى إذا كان مشروعك السابق يتطلبها
    pub_date = models.DateField(default=now)

    def __str__(self):
        return self.name

# 2. نموذج الدرس
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField(default="Default content")
    # يمكنك إضافة حقول أخرى مثل الفيديو أو الملفات

    def __str__(self):
        return self.title

# 3. نموذج التسجيل (مهم جداً لربط الطالب بالدورة)
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    date_enrolled = models.DateField(default=now)
    mode = models.CharField(max_length=5, default='audit') # audit or honor
    rating = models.FloatField(default=5.0)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.name}"

# ==========================================
# النماذج المطلوبة في المشروع (Tasks)
# ==========================================

# 4. نموذج السؤال
class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text

    # دالة مساعدة للتحقق من صحة الإجابة وحساب الدرجة
    def is_get_score(self, selected_ids):
        all_answers = self.choice_set.filter(is_correct=True).count()
        selected_correct = self.choice_set.filter(id__in=selected_ids, is_correct=True).count()
        
        # التحقق من أن جميع الإجابات الصحيحة تم اختيارها ولا توجد إجابات خاطئة
        if all_answers == selected_correct and len(selected_ids) == all_answers:
            return True
        return False

# 5. نموذج الخيارات
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

# 6. نموذج التسليم (الإجابات النهائية للطالب)
class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f"Submission by {self.enrollment.user.username} for {self.enrollment.course.name}"

