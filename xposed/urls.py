from django.conf.urls import url
from . import views



app_name = 'xposed'
urlpatterns = [
    url(r'index/$',views.IndexView.as_view(), name = 'home'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.ModelsDetail.as_view(), name = 'detail'),
    url(r'^about/$',views.AboutView.as_view() , name = 'about'),
    url(r'^gallery/$',views.GalleryView.as_view(), name = "gallery"),
    url(r'^registration/$',views.CreateView.as_view(), name = "register")

]
