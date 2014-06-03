# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from aakashuser.models import User
from aakashuser.forms import RegisterForm


def index(request):
	return render_to_response("index.html", request)

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

