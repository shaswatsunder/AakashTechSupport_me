# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from aakashuser.models import User
from aakashuser.forms import RegisterForm

# INDEX PAGE VIEW

def index(request):
	return render_to_response("index.html", request)

# REGISTER VIEW

def register(request):
	context = RequestContext(request)
	
	if request.POST:
		postform = RegisterForm(data=request.POST)
		if postform.is_valid():
			postform.save(commit=True)
			return HttpResponseRedirect('/index/')
		else:
			print postform.errors 
	else:
		postform = RegisterForm()
		print postform # Not Neccessary
		
	context_dict = {
		'postform' : postform,
	}
		
	return render_to_response("register.html", context_dict, context)
		
# LOGIN VIEW

def login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        email_id = request.POST['email_id']
        password = request.POST['password']
        
        user = authenticate(email_id=email_id, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}" .format(email_id, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response("login.html", request)


