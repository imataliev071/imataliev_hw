from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER_CHOICES = (
    ('М', 'М'),
    ('Ж', 'Ж')
)


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996', label='Номер телефона')
    date_of_birth = forms.DateField(required=True, initial='Дата рождения',
                                    widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    works = forms.CharField()
    height = forms.CharField()

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'date_of_birth',
            'gender',
            'works',
            'height'
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
