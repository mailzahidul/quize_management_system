from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import Quizform
from .models import Quiz, Course, Semester, Result
from user_admin.models import User
from django.contrib import messages
from user_admin.models import User as UUser
# Create your views here.

@login_required
def home(request):
    context={}
    courses = Course.objects.filter(active=True)
    context['courses'] = courses
    l = Group.objects.all()
    return render(request, 'index.html', context)


@login_required
def quiz_list(request):
    context={}
    quizes = Quiz.objects.all()
    context['quizes'] = quizes
    return render(request, 'quiz/quiz_list.html', context)

@login_required
def quiz_test(request, id):
   context={}
   course = Course.objects.get(id=id)
   questions = Quiz.objects.filter(course_name=course)
   context['questions'] = questions
   context['course'] = course

   if request.POST:
       print(request.POST, "All Input Answer")
       # questions = Quiz.objects.all()
       # course = Course.objects.get(id=id)
       # questions = Quiz.objects.filter(course_name=course)
       total_marks = 0
       wrong_answer = 0
       correct_answer = 0
       total = 0
       for q in questions:
           total += 1
           print(request.POST.get(q.question), "Select option")
           print(q.answer, "Answer")
           print()
           if q.answer == request.POST.get(q.question):
               total_marks += q.marks
               correct_answer += 1
           else:
               wrong_answer += 1
       percent = (total_marks / total) * 100
       try:
           profile_user = request.user
           if profile_user == User.objects.get(email=profile_user):
               user = User.objects.get(email=profile_user)
               print(user, "UUUUUUUUUUUUUU")
               Result.objects.create(user=user, course_name=course, marks=total_marks, )
               context['marks'] = total_marks
               context['time'] = request.POST.get('timer')
               context['correct'] = correct_answer
               context['wrong'] = wrong_answer
               context['total'] = total
               context['percent'] = percent
               return render(request, 'quiz/result.html', context)
       except Exception as err:
           messages.warning(request, f"{err}")
       # user = UserProfile.objects.get(user=profile_user)
       # Result.objects.create(user=user, course_name=course, marks=total_marks, )
       # context['marks'] = total_marks
       # context['time'] = request.POST.get('timer')
       # context['correct'] = correct_answer
       # context['wrong'] = wrong_answer
       # context['total'] = total
       # context['percent'] = percent
       # return render(request, 'quiz/result.html', context)

   return render(request, 'quiz/quiz_test.html', context)




def add_quiz(request):
    context={}
    forms = Quizform()
    courses = Course.objects.filter(active=True)
    context['courses'] = courses
    if request.POST:
        forms = Quizform(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('quiz_list')
    context['forms']=forms
    return render(request, 'quiz/add_quiz.html', context)


# def quiz_test_by_course(request, id):
#     course = Course.objects.get(id=id)
#     quizs = Quiz.objects.filter(course_name=course)
#     print(quizs, "Course wise quiz")
#
#     return redirect('home')