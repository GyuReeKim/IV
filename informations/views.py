from django.shortcuts import render, redirect, get_object_or_404
from .models import Survivor, Hunter
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'informations/index.html')

def survivor_list(request):
    characters = Survivor.objects.all()
    context = {
        'characters': characters,
        'role' : '생존자',
    }
    return render(request, 'informations/character_list.html', context)

def hunter_list(request):
    characters = Hunter.objects.all()
    context = {
        'characters': characters,
        'role': '감시자',
    }
    return render(request, 'informations/character_list.html', context)

def survivor_detail(request, survivor_id):
    character = get_object_or_404(Survivor, id=survivor_id)
    context = {
        'character': character,
        'role': '생존자',
    }
    return render(request, 'informations/character_detail.html', context)

def hunter_detail(request, hunter_id):
    character = get_object_or_404(Hunter, id=hunter_id)
    context = {
        'character': character,
        'role': '감시자',
    }
    return render(request, 'informations/character_detail.html', context)

@login_required
def survivor_like(request, survivor_id):
    survivor = get_object_or_404(Survivor, id=survivor_id)
    user = request.user
    if user in survivor.like_users.all():
        survivor.like_users.remove(user)
    else:
        survivor.like_users.add(user)
    return redirect('informations:survivor_detail', survivor_id)

@login_required
def hunter_like(request, hunter_id):
    hunter = get_object_or_404(Hunter, id=hunter_id)
    user = request.user
    if user in hunter.like_users.all():
        hunter.like_users.remove(user)
    else:
        hunter.like_users.add(user)
    return redirect('informations:hunter_detail', hunter_id)