from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from . import models, forms
from django.urls import reverse


# не польная информация
def tv_shows_list(request):
    if request.method == 'GET':
        tv_shows = models.TvShow.objects.all()
        return render(request, 'tv/tv_shows_list.html', {'tv_shows': tv_shows})


def tv_shows_detail(request, id):
    if request.method == 'GET':
        tv_shows_id = get_object_or_404(models.TvShow, id=id)
        return render(request, 'tv/tv_shows_detail.html', {'tv_shows_id': tv_shows_id})


def tv_shows_create(request):
    if request.method == 'POST':
        form = forms.TvShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('film_list'))
    else:
        form = forms.TvShowForm()
        return render(request, 'crud/tv_shows_create.html', {'form': form})


def tv_shows_delete(request):
    if request.method == 'GET':
        tv_shows_delite = models.TvShow.objects.all()
        return render(request, 'crud/delete/tv_shows_list_delite.html', {'tv_shows_delite': tv_shows_delite})


def tv_drop_view(request, id):
    tv_shows_id = get_object_or_404(models.TvShow, id=id)
    tv_shows_id.delete()
    # return HttpResponse('удален')
    return redirect(reverse('tv_shows_list_delite'))


def tv_shows_edit_view(request):
    if request.method == 'GET':
        tv_shows_update = models.TvShow.objects.all()
        return render(request, 'crud/update/tv_shows_list_update.html',
                      {'tv_shows_update': tv_shows_update})


def tv_shows_update(request, id):
    tv_shows_id = get_object_or_404(models.TvShow, id=id)
    if request.method == 'POST':
        form = forms.TvShowForm(instance=tv_shows_id, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tv_shows_list_update'))
    else:
        form = forms.TvShowForm(instance=tv_shows_id)
        return render(request, 'crud/update/tv_shows_update.html',
                      {
                          'form': form,
                          'tv_shows_id': tv_shows_id
                      })
