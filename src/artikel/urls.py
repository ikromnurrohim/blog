from django.conf.urls import url 

from .views import ArtikelListView, ArtikelDetailView

urlpatterns = [
	url(r'^detail/(?P<slug>[\w-]+)', ArtikelDetailView.as_view(), name='detail'),
	url(r'^(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
]
