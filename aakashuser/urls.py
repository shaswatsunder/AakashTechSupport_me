#Define your urls here.
__author__ = 'ushubham27'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^questions/$', 'aakashuser.views.display_questions', name='index'),
    url(r'^askquestion/$', 'aakashuser.views.ask_question', name='index'),
)