from django.conf.urls import patterns, include, url

urlpatterns = patterns('myapp.views',
   url(r'^signup/', 'signup'),
   url(r'^login/', 'login'),
   
   url(r'^add_user/', 'add_user'),
      url(r'^', 'hotels'),
      url(r'^bookaroom_view/', 'bookaroom_view'),
     
)
