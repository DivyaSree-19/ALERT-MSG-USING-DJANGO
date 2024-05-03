from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def message(request):
    return render(request,'message.html')

def success(request):
    messages.success(request,'this is success msg')
    return render(request,'message.html')

def info(request):
    messages.info(request,'this is info msg')
    return render(request,'message.html')

def error(request):
    messages.error(request,'this is error msg')
    return render(request,'message.html')

def warning(request):
    messages.warning(request,'this is warning msg')
    return render(request,'message.html')