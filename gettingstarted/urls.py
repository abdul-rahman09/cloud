
from django.contrib import admin
admin.autodiscover()
from django.conf.urls import url,include
from django.contrib import admin
from User import views as myview
from django.conf import settings
from django.conf.urls.static import static
import hello.views

urlpatterns = [
    url(r'^db', hello.views.db, name='db'),
    url(r'^$', myview.hotels),
    url(r'^admin/', admin.site.urls),
    url(r'^User/signup/', myview.signup),
    url(r'^User/update/', myview.update),
    url(r'^User/updateprof/', myview.updateprof),
    url(r'^add_user/', myview.add_user),
    url(r'^User/login/', myview.login),
    url(r'^bookaroom_view/(?P<roomid>\d+)/$', myview.bookaroom_view, name='roomid'),
    url(r'^fb/',myview.fb),
    url(r'^authenticate/', myview.authenticate),
    url(r'^User/logout/', myview.logout),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url('^accounts/', include('django.contrib.auth.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
