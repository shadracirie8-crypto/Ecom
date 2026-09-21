from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm





# REGISTER
def register_view(request):

    if request.method == 'POST':

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            messages.error(request, "Nom déjà utilisé")

            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('index')

    return render(request, 'users/register.html')


# LOGIN


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # ADMIN
            if user.is_superuser:

                return redirect('dashboard')

            # USER NORMAL
            return redirect('index')

        else:

            messages.error(
                request,
                "Identifiants invalides"
            )

    return render(
        request,
        'users/login.html'
    )


# LOGOUT
def logout_view(request):

    logout(request)

    return redirect('index')

@login_required
def account(request):

    if request.method == 'POST':

        u_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid():

            u_form.save()

            p_form.save()

            messages.success(
                request,
                'Profil mis à jour avec succès'
            )

            return redirect('account')

    else:

        u_form = UserUpdateForm(
            instance=request.user
        )

        p_form = ProfileUpdateForm(
            instance=request.user.profile
        )

    context = {

        'u_form': u_form,

        'p_form': p_form

    }

    return render(
        request,
        'users/account.html',
        context
    )