from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from . import models, forms
from django.urls import reverse
from django.views import generic


# не польная информация
# def tv_shows_list(request):
#     if request.method == 'GET':
#         tv_shows = models.TvShow.objects.all()
#         return render(request, 'tv/tv_shows_list.html', {'tv_shows': tv_shows})


class TvShowListView(generic.ListView):
    template_name = 'tv/tv_shows_list.html'
    model = models.TvShow

    def get_queryset(self):
        return self.model.objects.all()


class TvShowDetailView(generic.DetailView):
    template_name = 'tv/tv_shows_detail.html'
    context_object_name = 'tv_shows_id'

    def get_object(self, **kwargs):
        tv_shows_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tv_shows_id)


# def tv_shows_detail(request, id):
#     if request.method == 'GET':
#         tv_shows_id = get_object_or_404(models.TvShow, id=id)
#         return render(request, 'tv/tv_shows_detail.html', {'tv_shows_id': tv_shows_id})


class TvShowCreateView(generic.CreateView):
    template_name = 'crud/tv_shows_create.html'
    model = models.TvShow
    form_class = forms.TvShowForm
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TvShowCreateView).form_valid(form=form)


# def tv_shows_create(request):
#     if request.method == 'POST':
#         form = forms.TvShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('film_list'))
#     else:
#         form = forms.TvShowForm()
#         return render(request, 'crud/tv_shows_create.html', {'form': form})


def tv_shows_delete(request):
    if request.method == 'GET':
        tv_shows_delete = models.TvShow.objects.all()
        return render(request, 'crud/delete/tv_shows_list_delete.html', {'tv_shows_delete': tv_shows_delete})


class TvShowDropView(generic.DetailView):
    template_name = 'crud/delete/confirm_delete.html'
    success_url = '/tv_shows_list_delete/'

    def get_object(self, **kwargs):
        tv_shows_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tv_shows_id)


# def tv_drop_view(request, id):
#     tv_shows_id = get_object_or_404(models.TvShow, id=id)
#     tv_shows_id.delete()
#     # return HttpResponse('удален')
#     return redirect(reverse('tv_shows_list_delete'))


def tv_shows_edit_view(request):
    if request.method == 'GET':
        tv_shows_update = models.TvShow.objects.all()
        return render(request, 'crud/update/tv_shows_list_update.html',
                      {'tv_shows_update': tv_shows_update})


class TvShowUpdateView(generic.UpdateView):
    template_name = 'crud/update/tv_shows_update.html'
    form_class = forms.TvShowForm
    success_url = '/tv_shows_list_update/'

    def get_object(self, **kwargs):
        tv_shows_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=tv_shows_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)


# def tv_shows_update(request, id):
#     tv_shows_id = get_object_or_404(models.TvShow, id=id)
#     if request.method == 'POST':
#         form = forms.TvShowForm(instance=tv_shows_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('tv_shows_list_update'))
#     else:
#         form = forms.TvShowForm(instance=tv_shows_id)
#         return render(request, 'crud/update/tv_shows_update.html',
#                       {
#                           'form': form,
#                           'tv_shows_id': tv_shows_id
#                       })


class SearchView(generic.ListView):
    template_name = 'tv/tv_shows_list.html'
    paginate_by = 6

    def get_queryset(self):
        return models.TvShow.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, object_list=None, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context