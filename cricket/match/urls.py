from django.conf.urls import url
from match.views import matchdetails
app_name="match"

urlpatterns = [
    url(r'^matchdetails/(?P<id>[0-9]+)/$', matchdetails,name='matchdetails'),
    # url(r'^matchfixtures$', matchfixtures, name='matchfixtures'),
    # url(r'^add_city$', add_city,name='add_city'),
]
