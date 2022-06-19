from quiz.models import Course

def custom_context_processor(request):
    context={}
    courses = Course.objects.filter(active=True)
    context['courses'] = courses
    return context