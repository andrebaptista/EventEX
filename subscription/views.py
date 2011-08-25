from django.views.defaults import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from subscription.models import Subscription
from subscription.forms import SubscriptionForm

def success(request, id):
    inscricao = True
    subscriber = get_object_or_404(Subscription, pk=id)
    return render_to_response("subscription/success.html", {"subs":subscriber, "inscricao":inscricao}, context_instance=RequestContext(request))
	
def subscription(request):
    inscricao = True    
    form = SubscriptionForm()
    
    if request.method == "POST":
	form = SubscriptionForm(request.POST)
    
	if not form.is_valid():
	    return render_to_response("subscription/form.html", {"form":form, "inscricao":inscricao}, context_instance=RequestContext(request))
	    
	get_form = form.save()
	return redirect("subscription:subs_success", id=get_form.pk)
    else:
	return render_to_response("subscription/form.html", {"form":form, "inscricao":inscricao}, context_instance=RequestContext(request))