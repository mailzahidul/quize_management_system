from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Quizform
from .models import Quiz
# Create your views here.

@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def quiz_list(request):
    context={}
    quizes = Quiz.objects.all()
    context['quizes'] = quizes
    return render(request, 'quiz/quiz_list.html', context)

@login_required
def quiz_test(request):
   context={}
   if request.POST:
       print(request.POST, "All Input Answer")
       questions = Quiz.objects.all()
       total_score = 0
       wrong_answer = 0
       correct_answer = 0
       total = 0
       for q in questions:
           total += 1
           print(request.POST.get(q.question), "Select option")
           print(q.answer, "Answer")
           print()
           if q.answer == request.POST.get(q.question):
               total_score += 10
               correct_answer += 1
           else:
               wrong_answer += 1
       percent = total_score / (total * 10) * 100
       context['score'] = total_score
       context['time'] = request.POST.get('timer')
       context['correct'] = correct_answer
       context['wrong'] = wrong_answer
       context['total'] = total
       context['percent'] = percent

       return render(request, 'quiz/result.html', context)
   else:
       questions = Quiz.objects.filter(active=True)
       context['questions'] = questions
       return render(request, 'quiz/quiz_test.html', context)

def add_quiz(request):
    forms = Quizform()
    if request.POST:
        forms = Quizform(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('quiz_list')
    context={'forms':forms}
    return render(request, 'quiz/add_quiz.html', context)