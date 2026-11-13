from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Question, Choice, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # منطق معالجة إجابات الاختبار وحفظ Submission
        # ...
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)
    return render(request, 'onlinecourse/submit.html', {'course': course})

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    # حساب النتيجة
    score = 0
    total = 0
    # ... منطق الحساب ...
    context = {
        'course': course,
        'submission': submission,
        'score': score,
        'total': total,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)