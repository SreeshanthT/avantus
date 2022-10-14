from django.shortcuts import render
from .forms import StringForm

# Create your views here.

def check_the_string(request,**kwargs):
    form = StringForm()

    if request.method == "POST":
        form = StringForm(request.POST)
        if form.is_valid():
            output_sample = form.check()
            
    return render(request,"base.html",locals())