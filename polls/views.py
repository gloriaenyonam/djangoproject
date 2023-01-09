from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from .models import Question,Choice
from django.http import HttpResponseRedirect
from django.urls import reverse



def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
        }
    return render(request, 'polls/index.html', context)



def detail(request, question_id):
    # print("war", question_id)
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    #print("voters",request.POST['choice'])
    try:
        selected_choice = Choice.objects.get(pk=request.POST['choice'])
        
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    

