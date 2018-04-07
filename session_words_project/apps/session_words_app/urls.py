from django.conf.urls import url
from django.contrib import admin
from . import views

# def test(request):
#     print "* app urls *"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', test),
    url(r'^$', views.index),
    url(r'^clear$', views.clear),
    url(r'^add$', views.add),

]
