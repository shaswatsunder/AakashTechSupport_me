
from django.conf.urls import patterns, include, url
from questions import views
from questions import forumviews
urlpatterns = patterns(
    '',
    #url(r'^$', views.main, name='main'),
    #url(r'^(?P<id>\d+)/$', views.post, name='post'),
    #url(r'^post/(?P<id>\d+)/$', views.reply, name='reply'),
    url(r'^()$', views.main, name='question'),
    url(r'^votes/$', views.votes, name='votes'),
    url(r'^(latest)/$', views.main, name='latest'),
    url(r'^(frequent)/$', views.frequent, name='frequent'),
    url(r'^(unanswered)/$', views.main, name='unanswered'),
    url(r'^(link)/((?P<id>\d+))/$', views.allqueries_link, name='l_link'),
    url(r'^(frequent_link/(?P<id>\d+))/$', views.frequent_link, name='link'),
    url(r'^(votes_link/(?P<id>\d+))/$', views.votes_link, name='v_link'),
    url(r'^tag/$', forumviews.tag, name='tag'),
    url(r'^tag/(?P<id>\d+)/$', forumviews.linktag, name='linktag'),
    url(r'^tag_search/$', forumviews.tag_search, name='tag_search'),
    url(r'^tag/questions/(?P<id>\d+)/(?P<tagid>\d+)/$', forumviews.questions, name='questions'),
    url(r'^questions/$', 'aakashuser.views.display_questions', name='index'),
    url(r'^askquestion/$', 'aakashuser.views.ask_question', name='index'),
    url(r'^tags/$', 'aakashuser.views.view_tags', name='tags'),
    url(r'^search/$', 'aakashuser.views.search_tags', name='search_tags'),

    url(r'^youranswer$', views.your_answer, name='votes'),

)
