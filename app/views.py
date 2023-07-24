from django.shortcuts import render

# Create your views here.
def num(request):
    return render(request,'num.html')
