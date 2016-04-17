from django.shortcuts import render
from .forms import FeatureRequestForm

def home(request):
    """ Renders view for application home page
    Args: 
	request: http get request from user
    Returns: 
        rendered html home page
    """

    title = "Welcome to Feature Request"
    context = {
        "template_title": title,
    }
    return render(request, "home.html", context)

def feature_request(request):
    """ Renders view for feature request page
    Args:
	request: http get request from user
    Returns:
        rendered html feature request page with request form
    """

    title = "Feature Request"
    form = FeatureRequestForm(request.POST or None)
    
    if form.is_valid():
        form.save(commit=False)
        print "Request Valid"

    context = {
        "template_title": title,
        "feature_form": form,
    }
    return render(request, "feature_request.html", context)
