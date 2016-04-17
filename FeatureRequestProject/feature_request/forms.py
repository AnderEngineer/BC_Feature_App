from django import forms
from django.forms.widgets import DateInput, NumberInput, URLInput
from .models import FeatureRequest
from datetime import datetime

class FeatureRequestForm(forms.ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ('title','description','client','client_priority',\
                  'target_date', 'ticket_url', 'product_area')
        # Select widgets for certain fields
        widgets = {
            'description':forms.Textarea(attrs={'rows':'4'}),
            'client_priority':NumberInput(attrs={'min': '1'}),
            'target_date':DateInput(attrs = {'type':'date'}),
            'ticket_url':URLInput(),
        }

    def clean_target_date(self):
        """ Checks if the given target date is in the future """
        date_given = self.cleaned_data.get('target_date')
        if date_given < datetime.today().date():
            raise forms.ValidationError("Please select a future target date.")
        return date_given
