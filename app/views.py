from django.shortcuts import render

# Create your views here.

def india(request):
    return render (request,'india.html')

def aus(request):
    return render (request,'aus.html')

def indfans(request):
    return render (request,'indfans.html')
