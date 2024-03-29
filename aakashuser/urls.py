#Define your urls here.
__author__ = 'ushubham27'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^questions/$', 'aakashuser.views.display_questions', name='index'),
    url(r'^askquestion/$', 'aakashuser.views.ask_question', name='index'),
    url(r'^tags/$', 'aakashuser.views.view_tags', name='tags'),
    url(r'^search/$', 'aakashuser.views.search_tags', name='search_tags'),
)