from django import forms
from .models import teamform


class addteam(forms.ModelForm):
    class Meta:
        model = teamform
        fields = ['name','logouri']
    def __init__(self, *args, **kwargs):
        super(addteam, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['logouri'].widget.attrs['class'] = 'form-control'
