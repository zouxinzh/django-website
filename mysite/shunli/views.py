from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Question
from .forms  import ContactForm
from django.core.mail import send_mail, BadHeaderError
# Create your views here.

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)  
        if form.is_valid():
            form.save()    
    else:
        form = ContactForm()
    
    context ={
        'form':form,
    }
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    return render(request, 'shunli/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def contact(request):
    template = "shunli/contact.html"
    if request.method == "POST":
        form = ContactForm(request.POST)  
        if form.is_valid():
            form.save()    
    else:
        form = ContactForm()
    
    context ={
        'form':form,
    }
    return render(request,template,context)