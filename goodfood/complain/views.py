from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Complain
from complain.forms import ComplainForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = ComplainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
            'You complain has been successfully registered '
            '<a href="/">Go to home page</a>.',
            extra_tags='safe'
            )
    else:
        form = ComplainForm()
    return render(request, 'reg_form.html', {'form': form})
