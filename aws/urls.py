from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    url(r'^signup$', views.SignUpView.as_view(), name='signup'),
    url(r'^login$', views.UserLoginView.as_view(), name='login'),
    url(r'^dashboard$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^configure$', views.ConfigurationView.as_view(), name='configuration'),
    url(r'^monitor$', views.RequestMonitorView.as_view(), name='monitor'),
    url(r'^logout$', views.UserLogoutView.as_view(), name='logout'),
    url(r'^.*$', views.NotFoundView.as_view(), name='not_found')
]
