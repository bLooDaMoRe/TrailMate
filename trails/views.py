from django.shortcuts import render, redirect
from .models import Trail, Location
from .forms import LocationForm, TrailForm
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'trails/home.html')


def trail_list(request):
    trails = Trail.objects.all()
    return render(request, 'trails/trail_list.html', {'trails': trails})


def location_list(request):
    locations = Location.objects.all()
    return render(request, 'trails/location_list.html', {'locations': locations})


def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('location-list')
    else:
        form = LocationForm()

    return render(request, 'trails/location_form.html', {'form': form})


def trail_create(request):
    if request.method == 'POST':
        form = TrailForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('trail-list')
    else:
        form = TrailForm()

    return render(request, 'trails/trail_form.html', {'form': form})


def trail_edit(request, pk):
    trail = Trail.objects.get(pk=pk)

    if request.method == 'POST':
        form = TrailForm(request.POST, instance=trail)

        if form.is_valid():
            form.save()
            return redirect('trail-list')
    else:
        form = TrailForm(instance=trail)

    return render(request, 'trails/trail_form.html', {
        'form': form,
        'trail': trail,
    })

def trail_delete(request, pk):
    trail = Trail.objects.get(pk=pk)

    if request.method == 'POST':
        trail.delete()
        return redirect('trail-list')

    return render(request, 'trails/trail_confirm_delete.html', {
        'trail': trail,
    })

def location_edit(request, pk):
    location = Location.objects.get(pk=pk)

    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)

        if form.is_valid():
            form.save()
            return redirect('location-list')
    else:
        form = LocationForm(instance=location)

    return render(request, 'trails/location_form.html', {
        'form': form,
        'location': location,
    })


def location_delete(request, pk):
    location = Location.objects.get(pk=pk)

    if request.method == 'POST':
        location.delete()
        return redirect('location-list')

    return render(request, 'trails/location_confirm_delete.html', {
        'location': location,
    })

def trail_detail(request, pk):
    trail = get_object_or_404(Trail, pk=pk)

    return render(request, 'trails/trail_detail.html', {
        'trail': trail,
    })
