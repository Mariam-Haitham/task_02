from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def step7(request):
    context = {
            "msg": "Hello World!",
            }
    return render(request, "html_file.html", context)
