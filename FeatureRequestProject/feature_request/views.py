from django.shortcuts import render
from .forms import FeatureRequestForm
from .models import FeatureRequest

def view_requests(request):
    """ Renders view that diplays all feature requests
    Args: 
        request: http get request from user
    Returns: 
        rendered html page with requests
    """
    
    title = "Feature Requests"
    feature_requests = FeatureRequest.objects.all().order_by('client_priority')
    context = {
        "template_title": title,
        "feature_requests": feature_requests,
    }
    return render(request, "view_requests.html", context)

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

def update_priorities(current_priority, client_name):
    """ Updates client priorities to priority + 1 if a record with
        the same client name and priority exist.
    Args:
	current_priority: priority to check for existing record
        client_name: name of client to check for existing record
    Returns:
	None
    """
    try:
        # check if there is a client with the same priority in records
        priority_exists = FeatureRequest.objects.get(client=client_name, \
						     client_priority=current_priority)
        # If there is, check if there is for the next priority
        current_priority += 1
        update_priorities(current_priority, client_name)
        # Now update current record with updated priority
        priority_exists.client_priority = current_priority
        priority_exists.save()
    except FeatureRequest.DoesNotExist:
        # No other records in the way
        return

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
        # Get the client and priority to check for existing records
        provided_client = form.cleaned_data.get("client")
        provided_priority = form.cleaned_data.get("client_priority")
        # Move records with same client and priority back
        update_priorities(provided_priority, provided_client)
        form.save()
        return view_requests(request)
	
    context = {
        "template_title": title,
        "feature_form": form,
    }
    return render(request, "feature_request.html", context)
