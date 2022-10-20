
from django import forms
from testb_app import models


class MusicianForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name ", widget=forms.TextInput(
        attrs={'placeholder': 'Enter your First Name', 'style': 'width:200px'}))
    last_name = forms.CharField(label="Last Name ", widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Last Name', 'style': 'width:200px'}))
    instrument = forms.CharField(label="Instrument", widget=forms.TextInput(
        attrs={'placeholder': 'Enter Instrument name', 'style': 'width:200px'}))

    class Meta:
        model = models.Musician
        fields = "__all__"


class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Album
        fields = '__all__'
