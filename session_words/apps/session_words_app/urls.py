from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    # root goes to the index
    url(r'^$', views.index),
    # does all the work, called by the submit button
    url(r'^process', views.process),
    # lets us clear the session, called by clear button
    url(r'^clear', views.clear)
]   