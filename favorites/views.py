from django.shortcuts import render, redirect, get_object_or_404
from trails.models import Trail

def favorites_list(request):
    favorite_ids = request.session.get('favorites', [])
    trails = Trail.objects.filter(pk__in=favorite_ids)
    return render(
        request,
        'favorites/favorites_list.html',
        {'trails': trails}
    )

def add_favorite(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    favorite_ids = request.session.get('favorites', [])

    if trail.id not in favorite_ids:
        favorite_ids.append(trail.id)

    request.session['favorites'] = favorite_ids
    return redirect('trail-list')

def remove_favorite(request, trail_id):
    favorite_ids = request.session.get('favorites', [])

    if trail_id in favorite_ids:
        favorite_ids.remove(trail_id)

    request.session['favorites'] = favorite_ids
    return redirect('favorites:favorites_list')
