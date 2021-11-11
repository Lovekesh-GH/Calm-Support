from django.shortcuts import render,HttpResponse
from tips.forms import UploadForm
from tips.models import Uploads

# Create your views here.

def UploadView(request):
    context = {}
    if request.method == 'POST': 
        form = UploadForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            context["message"] = "Successful"

        else: 
            context["error"] = form.errors
    
    context["form"] = UploadForm()
    return render(request, 'home.html', context)

def record(request):
    return render(request, 'record.html', {})