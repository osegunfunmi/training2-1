from django.contrib import messages
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from src.guest.models import Guest
from src.guest import forms



def guest(request, method=None, pk=None):
    payload = dict()
    form = dict()

    # process url
    if method == 'new':
        form = forms.FormGuest()
        instance = Guest()
        payload['form_action'] = '/guestapp/guest/new/'
        template = "guest/form-guest.html"

    elif method == 'update' and pk is not None:
        instance = Guest.objects.get(pk=pk)
        form = forms.FormGuest(instance=instance, data=model_to_dict(instance))
        payload['form_action'] = '/guestapp/guest/update/%s/' % str(pk)
        template = "guest/edit.html"

    else:
    	payload['guest_list'] = Guest.objects.all()
        template = "guest/index.html"

    # CREATE & UPDATE
    if request.method == "POST":

        errors = []

        form = forms.FormGuest(request.POST, instance=instance)
        if form.is_valid():
            for post in request.POST:
                if hasattr(instance, post):
                    setattr(instance, post, form.cleaned_data[post])

        if (request.POST.get('first_name') is None or request.POST.get('first_name') == ''):
            errors.append('No first name was entered')

        if not errors:
            instance.save()
            messages.success(request, "Your entry has been saved")
            return HttpResponseRedirect('/guestapp/guest/')

        else:
            return HttpResponseRedirect('/guestapp/guest/index/error/')

    # render to browser
    return render(
    	request,
        template,
        {'form': form, 'payload': payload},
    )

    # DELETE
def delete(request, pk):
    instance = Guest.objects.get(pk=pk)
    instance.delete()
    form = forms.FormGuest(instance=instance, data=model_to_dict(instance))
    messages.success(request, "Successfully deleted")
    return HttpResponseRedirect('/guestapp/guest/')
    
       


#def update(request, id):
    #form = payload.objects.get(pk=pk)
    #context = {"payload":payload}
    #return render(request,'guest/edit.html', context)

def index(request):
    context = locals()
    template = 'guest/index.html'
    return render(request,template,context)


def event(request, method=None, pk=None):
    payload = dict()
    form = dict()

    # process url
    if method == 'new':
        form = forms.FormEvent()
        instance = event()
        payload['form_action'] = '/guestapp/event/new/'
        template = "event/event-list.html"
    else:
        payload['event_list'] = Guest.objects.all()
        template = "event/event-list.html"

     # CREATE & UPDATE
    if request.method == "POST":

        errors = []

        form = forms.FormEvent(request.POST, instance=instance)
        if form.is_valid():
            for post in request.POST:
                if hasattr(instance, post):
                    setattr(instance, post, form.cleaned_data[post])

        if (request.POST.get('event_name') is None or request.POST.get('first_name') == ''):
            errors.append('No event name was entered')

        if not errors:
            instance.save()
            return HttpResponseRedirect('/guestapp/event/index/')

        else:
            return HttpResponseRedirect('/guestapp/event/index/error/')

    # render to browser
    return render(
        request,
        template,
        {'form': form, 'payload': payload},
    )

