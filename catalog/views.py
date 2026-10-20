from django.shortcuts import render, redirect
from .models import Feature
from .forms import FeatureForm


def home(request):
    return render(request, 'trails/home.html')


def feature_list(request):
    features = Feature.objects.all()
    return render(request, 'catalog/feature_list.html', {
        'features': features,
    })


def feature_create(request):
    if request.method == 'POST':
        form = FeatureForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('feature-list')
    else:
        form = FeatureForm()

    return render(request, 'catalog/feature_form.html', {
        'form': form,
    })