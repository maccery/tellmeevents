from __future__ import unicode_literals

from django import forms


class SearchForm(forms.Form):
    def __init__(self, categories, *args, **kwargs):
        # We need to switch the categories into tupules
        choices = []
        for category in categories:
            choices.append((category['id'], category['name']))

        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['category1'].choices = choices
        self.fields['category2'].choices = choices
        self.fields['category3'].choices = choices

    # Create the choice fields, we've already defined what the choices are in init
    category1 = forms.ChoiceField(choices=(), required=True)
    category2 = forms.ChoiceField(choices=(), required=True)
    category3 = forms.ChoiceField(choices=(), required=True)
