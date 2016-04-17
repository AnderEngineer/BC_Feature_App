from django import forms
from django.forms.widgets import DateInput, NumberInput, URLInput
from .models import FeatureRequest

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
