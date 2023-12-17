from django.shortcuts import render, get_object_or_404
from . import models


# не польная информация
def tv_shows_list(request):
    if request.method == 'GET':
        tv_shows = models.TvShow.objects.all()
        return render(request, 'tv/tv_shows_list.html', {'tv_shows': tv_shows})


def tv_shows_detail(request, id):
    if request.method == 'GET':
        tv_shows_id = get_object_or_404(models.TvShow, id=id)
        return render(request, 'tv/tv_shows_detail.html', {'tv_shows_id': tv_shows_id})
