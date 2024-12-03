from django.shortcuts import render,redirect
from .models import Planet
from .forms import PlanetForm

def home(request):
    planets = Planet.objects.all()
    return render(request, 'cosmos/home.html', {'planets': planets})

def planet_detail(request, planet_id):
    planet = get_object_or_404(Planet, id=planet_id)
    return render(request, 'cosmos/planet_detail.html', {'planet': planet})

def add_planet(request):
    if request.method == 'POST':
        form = PlanetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlanetForm()
    return render(request, 'cosmos/add_planet.html', {'form': form})

def edit_planet(request, planet_id):
    planet = get_object_or_404(Planet, id=planet_id)
    if request.method == 'POST':
        form = PlanetForm(request.POST, instance=planet)
        if form.is_valid():
            form.save()
            return redirect('planet_detail', planet_id=planet.id)
    else:
        form = PlanetForm(instance=planet)
    return render(request, 'cosmos/edit_planet.html', {'form': form, 'planet': planet})
