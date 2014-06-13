# Imports {{{
from PIL import Image as PImage
import itertools
from AakashTechSupport.settings import MEDIA_URL
from questions.models import *

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required


def main(request, url):
    context = RequestContext(request)
    if url == 'latest' :
        posts=Post.objects.all().order_by("-post_date")
        context_dict = {
            'posts': posts,}


    elif url == 'unanswered':
        posts=Post.objects.all()
        replies = Reply.objects.all()
        files = []

        for p in posts :
            a=0
            for r in replies :
                if r.title.title == p.title :
                    a=1
            if a == 0:
                files.append(p)
            context_dict = {
                'posts': files,}


    elif url == '':
        posts= Post.objects.all()
        context_dict = {
            'posts': posts,}


    return render_to_response('questions/allqueries.html', context_dict, context)


def allqueries_link(request, id):
    context = RequestContext(request)

    post = Post.objects.get(pk=id)
    replies = Reply.objects.filter(title=post)

    context_dict = {
        'post': post,
        'replies': replies,
    }

    return render_to_response("questions/allqueries_link.html", context_dict, context)

def frequent(request):
    context = RequestContext(request)
    posts=Post.objects.all().order_by("-post_views")
    context_dict = {
            'posts': posts,}
    return render_to_response('questions/frequent.html', context_dict, context)

def votes(request):
    context = RequestContext(request)
    posts=Post.objects.all().order_by("-upvotes")
    context_dict = {
            'posts': posts,}
    return render_to_response('questions/votes.html', context_dict, context)


def frequent_link(request, id):
	context = RequestContext(request)
	post = Post.objects.get(pk=id)
	post.post_views = post.post_views + 1
	post.save()
	replies = Reply.objects.filter(title=post)
	context_dict = {
        	'post': post,
          	'replies': replies,
          }
	return render_to_response("questions/allqueries_link.html", context_dict, context)

def votes_link(request, id):
	context = RequestContext(request)
	post = Post.objects.get(pk=id)
	post.upvotes = post.upvotes + 1
	post.save()
	replies = Reply.objects.filter(title=post)
	context_dict = {
        	'post': post,
          	'replies': replies,
          }
	return render_to_response("questions/allqueries_link.html", context_dict, context)

@login_required
def your_answer(request):
    context = RequestContext(request)
    
    return render_to_response('questions/your_answer.html',  context)




