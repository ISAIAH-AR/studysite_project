from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from main_app.models import SignUpModel
from main_app.forms import SignUpForm

# Create your views here.


def sign_up(request):


    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = SignUpForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            school = form.cleaned_data['school']


           # Create user and save to the database
            user = User.objects.create_user(username=username,email=None, password=password)
            user.save()

            signUpModel = SignUpModel(username=username, password=password, school=school)
            signUpModel.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('home') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = SignUpForm(request.POST)
    context = {
        'form': form,
    }

    return render(request, 'sign_up.html', context)

@login_required
def home(request):
    """View function for home page of site."""
    return render(request, 'home.html')

def math_one(request):
    return render(request, 'form_one/math_one.html')
