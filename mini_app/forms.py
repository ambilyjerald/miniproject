from django import forms
from mini_app.models import todo
class reg_form(forms.ModelForm):
    class Meta:
        model=todo
        fields=("__all__")
