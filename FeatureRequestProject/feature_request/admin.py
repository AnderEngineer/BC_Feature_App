from django.contrib import admin

# Register your models here.
from .models import FeatureRequest
from .forms import FeatureRequestForm

class FeatureRequestAdmin(admin.ModelAdmin):
   list_display = ('title','description','client','client_priority',\
                   'target_date','ticket_url','product_area','date_created')
   form = FeatureRequestForm

admin.site.register(FeatureRequest, FeatureRequestAdmin)
