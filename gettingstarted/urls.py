from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [

    url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
    url(r'^$', myview.hotels),
    url(r'^admin/', admin.site.urls),
    url(r'^User/signup', myview.signup),
       url(r'^add_user', myview.add_user),
    url(r'^User/login', myview.login),
url(r'^bookaroom_view', myview.bookaroom_view),
url(r'^authenticate', myview.authenticate),
url(r'^User/logout', myview.logout),
]
