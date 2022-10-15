from django.shortcuts import render
from django.http import HttpResponse
from Registration.models import Course,Batch,Student
# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to Prime Intuit Registration Page<h1>")
def home(request):
    #return HttpResponse("<h1>Welcome to Prime Intuit home Page<h1>")
    # my_dict={'Insert_me':"I am a text from Registration/views.py now from subtemplates"}
    batch_list=Batch.objects.raw('select * from Registration_Batch')
    data_dict={'access_record':batch_list}

    return render(request,'Registration/index.html',context=data_dict)