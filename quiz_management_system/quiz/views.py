from django.shortcuts import render, redirect
from .forms import Quizform
# Create your views here.

def home(request):

    return render(request, 'index.html')


# Create your views here.
# def home(request):
#     if request.method == 'POST':
#         print(request.POST)
#         questions = QuesModel.objects.all()
#         score = 0
#         wrong = 0
#         correct = 0
#         total = 0
#         for q in questions:
#             total += 1
#             print(request.POST.get(q.question))
#             print(q.ans)
#             print()
#             if q.ans == request.POST.get(q.question):
#                 score += 10
#                 correct += 1
#             else:
#                 wrong += 1
#         percent = score / (total * 10) * 100
#         context = {
#             'score': score,
#             'time': request.POST.get('timer'),
#             'correct': correct,
#             'wrong': wrong,
#             'percent': percent,
#             'total': total
#         }
#         return render(request, 'Quiz/result.html', context)
#     else:
#         questions = QuesModel.objects.all()
#         context = {
#             'questions': questions
#         }
#         return render(request, 'Quiz/home.html', context)

def add_quiz(request):
    if request.user.is_staff:
        form = Quizform()
        if (request.method == 'POST'):
            form = Quizform(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'quiz/add_quiz.html', context)
    else:
        return redirect('home')