from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$' , views.index),
    url(r'^session_words/process$' , views.process),
    url(r'^session_words/addword$' , views.add),
    url(r'^clear$' , views.clear)
]