from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import SignupForm, SignupFormWidget, SignupFormData

def signup10_affichage(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Process the form data if needed
            return redirect('myform_form:success')
    return render(request, 'myform_form/signup10_affichage.html', {'form': form})

def signup20_widget(request):
    form = SignupFormWidget()
    if request.method == 'POST':
        form = SignupFormWidget(request.POST)
        if form.is_valid():
            # Process the form data if needed
            return redirect('myform_form:success')
    return render(request, 'myform_form/signup20_widget.html', {'form': form})

def signup30_data(request):
    if request.method == "POST":
        form = SignupFormData(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            return redirect(reverse("myform_form:signup30_reussi"))
    else:
        form = SignupFormData()

    return render(request, "myform_form/signup30_data.html", context={"form":form})

def signup30_reussi(request):
    return render(request, 'myform_form/signup30_reussi.html')

def success(request):
    return render(request, 'myform_form/success.html')

from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignupFormData

def signup31_data(request):
    form = SignupFormData()
    return render(request, "myform_form/signup31_data.html", context={"form": form})

def signup31_affichage(request):
    form = SignupFormData(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print(cd)
        return render(request, 'myform_form/signup31_affichage.html', {"cd": cd})
    else:
        return HttpResponse("Les données ne sont pas valides")