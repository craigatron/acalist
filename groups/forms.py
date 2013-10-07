from django import forms
from groups.models import Group

class SearchForm(forms.Form):
  search = forms.CharField(required=False,
      widget=forms.TextInput(attrs={'class': 'form-control',
                                    'placeholder': 'Search'}))
  distance = forms.IntegerField(min_value=1, required=False,
      widget=forms.TextInput(attrs={'class': 'form-control',
                                    'placeholder': 'X'}))
  unit = forms.ChoiceField([(0, 'miles of'), (1, 'kilometers of')])
  location = forms.CharField(required=False,
      widget=forms.TextInput(attrs={'class': 'form-control',
                                    'placeholder': 'location'}))
  makeup = forms.ChoiceField((('', ''),) + Group.MAKEUPS, required=False,
      widget=forms.Select(attrs={'class': 'form-control'}))
  group_type = forms.ChoiceField((('', ''),) + Group.TYPES, required=False,
      widget=forms.Select(attrs={'class': 'form-control'}))
