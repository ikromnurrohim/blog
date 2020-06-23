from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView


from .views import register_page, login_page, home_page

urlpatterns = [
	url(r'^login/$', login_page, name='login'),
	url(r'^logout/$', LogoutView.as_view(), name='logout'),
	url(r'^artikel/', include('artikel.urls', namespace='artikel')),
	url(r'^register/$', register_page, name='register'),
	url(r'^$', home_page, name='home'),
    url(r'^admin/', admin.site.urls),
]
