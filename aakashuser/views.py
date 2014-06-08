# Create your views here.
__author__ = 'ushubham27'

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from forms import UserForm
from aakashuser.models import Post

# INDEX PAGE VIEW

def index(request):
    return render_to_response("index.html", request)

def search(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("search.html", c)

# REGISTER VIEW

def register(request):
    context = RequestContext(request)
    er1 = ""
    if request.POST:
        postform = UserForm(data=request.POST)

        if postform.is_valid():
            pwd = request.POST['password']
            rpwd = request.POST['password1']

            if pwd == rpwd:
                postform.save(commit=True)
                return HttpResponseRedirect('/index/')
            else:
                er1 = "Passwords don't match"
        else:
            print postform.errors
    else:
        postform = UserForm()

    context_dict = {
        'postform': postform,
        'er1': er1,
    }

    return render_to_response("register.html", context_dict, context)

# LOGIN VIEW

def login_x(request):
    session_id = ""
    if request.method == 'POST':
        try:
            m = User.objects.get(username=request.POST['username'])
            if m.password == request.POST['password']:
                request.session['id'] = m.email_id
                session_id = request.session['id']

                login_dict = {
                    'm': m,
                    'session_id': session_id,
                }
                return render_to_response('index.html', login_dict)
        except User.DoesNotExist:
            return HttpResponse("Your username and password pair didn't match.")
    else:
        c = {}
        c.update(csrf(request))
        context = RequestContext(request)
        return render_to_response("login.html", c, context)


def logout_x(request):
    try:
        del request.session['id']
        msg = "You have been succesfully logged out."
        print msg
    except KeyError:
        msg = "KeyError : Unable to Logout "
        print msg

    logout_msg = {
        'msg': msg
    }

    return HttpResponseRedirect('/index/', logout_msg)


def login_new(request):
   # t = loader.get_template('registration/login.html') - not needed
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['id'] = user.email
                session_id = request.session['id']
                login_dict = {
                    'm': user,
                    'session_id': session_id,
                }
                response = render_to_response('index.html', login_dict)
                response.set_cookie('logged_in', user.email)
                return response
            else:
                return HttpResponse("Not an active user.")
        else:
            return HttpResponse("User Auth failed.")
    else:
        #URL was accessed directly
        c = {}
        c.update(csrf(request))
        context = RequestContext(request)
        return render_to_response('login.html', c)


def logout_new(request):
    logout(request)
    response = HttpResponseRedirect('/index/')
    response.delete_cookie('logged_in')
    print "You have been logged out successfully."
    return response


def display_questions(request):
    return render_to_response('questions.html')

def ask_question(request):
    if request.POST:
        title = request.POST['post_title']
        body = request.POST['post_text']
        vote = 0
        post = Post.objects.create(title=title, body=body, vote=vote)
        post.tags.all()
        post.tags.add(request.POST['post_tags'])#Adding tags to the object created.

        """
        Foreign Key for User ?

        """

        post.save()
    else:
        c = {}
        c.update(csrf(request))
        return render_to_response('ask_question.html', c)

