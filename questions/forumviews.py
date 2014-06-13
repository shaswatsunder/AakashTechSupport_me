from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from questions.models import Post,Reply
from taggit.models import Tag


def tag(request): #This view has been defined for displaying all the tags and the number of posts related to each tag.
	context=RequestContext(request)
	tags=Tag.objects.all()#for fetching all the tags.
	for tag in tags:
		tag.count=len(Post.objects.filter(tags=tag))
	context_dict= {'tags': tags}
	return render_to_response('forum/tags.html', context_dict, context)
	
	
def linktag(request,id):#This view has been defined for linking a tag with its associated questions.
	context=RequestContext(request)
	tag= Tag.objects.get(pk=id)#for fetching the tag with a particular id.
	posts= Post.objects.filter(tags=tag).order_by('-post_date')#for fetching posts related to a particular tag.
	posts1= Post.objects.filter(tags=tag).order_by('-post_views')
	context_dict ={'posts':posts,'mytag':tag,'posts1':posts1}
	return render_to_response('forum/questions.html', context_dict, context)
	
def tag_search(request):#This view has been defined to search a tag, and if found , display the associated questions.
	context=RequestContext(request)
	mytag = request.POST.get('search_text')#value of search_text comes through the textbox in html
	mytag=mytag.upper()
	try:
		tag= Tag.objects.get(name=mytag)
		posts=Post.objects.filter(tags=tag).order_by('-post_date')#for fetching posts related to a particular tag.
		posts1= Post.objects.filter(tags=tag).order_by('-post_views')
		context_dict={'posts':posts,'mytag':tag,'posts1':posts1}
	except Tag.DoesNotExist:
		context_dict={}
	return render_to_response('forum/questions.html',context_dict,context) 
	
def questions(request,id,tagid):#This view has been defined to display all the replies related to a particular post.
	context=RequestContext(request)
	post=Post.objects.get(pk=id)#for fetching post having a particular id.
	mytag=Tag.objects.get(pk=tagid)
	reply=Reply.objects.filter(title=post)#for fetching replies related to a particular post
	mypost=Post.objects.filter(tags=mytag).exclude(pk=id)
	context_dict={'posts':post,'reply':reply,'mytag':mytag,'mypost':mypost}
	return render_to_response('forum/reply.html',context_dict,context) 



