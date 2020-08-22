from django import forms
from .models import players


class addplayer(forms.ModelForm):
    class Meta:
        model = players
        fields = ['firstName','lastName','imageUri','playernum','country','teamid']
    def __init__(self, *args, **kwargs):
        super(addplayer, self).__init__(*args, **kwargs)
        self.fields['firstName'].widget.attrs['class'] = 'form-control'
        self.fields['lastName'].widget.attrs['class'] = 'form-control'
        self.fields['imageUri'].widget.attrs['class'] = 'form-control'
        self.fields['playernum'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'
        self.fields['teamid'].widget.attrs['class'] = 'form-control'
