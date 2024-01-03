from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from . import forms


class ParserFormView(FormView):
    template_name = 'parser.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Данные взяты')
        else:
            return super().post(request, *args, **kwargs)
