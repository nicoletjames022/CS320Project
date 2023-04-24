from django.shortcuts import render, redirect

from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

from .forms import PersonForm

# Create your views here.
def register(request):

    if request.method != 'POST':
        form = UserCreationForm()
        personForm = PersonForm()

    else:
        form = UserCreationForm(date=request.POST)
        personForm = PersonForm(data=request.POST)

        if form.is_valid() and personForm.is_valid():

            savedUser = form.save()

            person = personForm.save(commit=False)

            person.user = savedUser

            personForm.save()

            return redirect('users:login')
    context = {'form': form, 'person_form' : personForm}

    return render(request, "registration/registration.html", context)