from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import os
from user.forms import UserRegisterForm, UserEditForm, AvatarForm
from user.models import Avatar
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request=request, template_name='ask.html')
        else:
            messages.error(request, "Usuario no ha sido creado :(")
    form = UserRegisterForm()
    return render(request, context={'form':form}, template_name='register.html')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                template_name = 'home.html'
        else:
            template_name = 'login.html'
        return render(request, context={'form':form}, template_name=template_name)

    form = AuthenticationForm()
    return render(request, context={'form': form}, template_name='login.html')


def logout_user(request):
    logout(request)
    return redirect('user:login')


def user(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    return render(request, template_name='profile.html', context=context_dict)


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {'url': avatars[0].image.url}
    return {}


@login_required
def update_user(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos cargados exitosamente", extra_tags='names')
            return redirect('user:profile')
    
    form = UserEditForm(model_to_dict(user))
    return render(request, context={'form':form}, template_name='profile_change.html')


@login_required
def avatar_load(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente", extra_tags='image')
            return redirect('user:profile')

    form= AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="avatar_form.html",
    )