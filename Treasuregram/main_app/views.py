from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .models import Treasure
from .forms  import TreasureForm

def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})

def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})

def add_treasure(request):
    form = TreasureForm()
    return render(request, 'add.html', {'form':form})

def post_treasure(request):
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit = True)
    return HttpResponseRedirect('/')