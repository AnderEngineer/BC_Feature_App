from django import forms
from django.forms.widgets import SelectDateWidget
from .models import FeatureRequest

class FeatureRequestForm(forms.ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ('title','description','client','client_priority',\
                  'target_date', 'ticket_url', 'product_area')
        # Select widgets for certain fields
        widgets = {
            'target_date':SelectDateWidget(),
        }
