from django.shortcuts import render, get_object_or_404
from .models import Survivor, Hunter

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