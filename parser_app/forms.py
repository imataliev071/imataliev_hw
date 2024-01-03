from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = [('kinogo.uk', 'kinogo.uk')]
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    def parser_data(self):
        if self.cleaned_data['media_type'] == 'kinogo.uk':
            film_parser = parser.parser_kinogo()
            for movie_data in film_parser:
                models.KinogoModel.objects.create(**movie_data)

