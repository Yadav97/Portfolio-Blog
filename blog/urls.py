
from django.urls import path

from . import views


urlpatterns = [
 
        path('', views.allblogs, name="allblogs"),
        path('<int:blog_id>/',views.detail,name='detail'),
     
]       

#To capture a value from the URL, use angle brackets.
#Captured values can optionally include a converter type. For example, use <int:name> to capture an integer parameter. If a converter isn’t included, any string, excluding a / character, is matched.

#example == > http://localhost:8000/blog/1

#so <int:blog_id> capture the integer 1 and store into blog_id var 