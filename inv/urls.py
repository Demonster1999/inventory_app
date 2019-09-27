from django.urls import path
from . import views
namespace = 'inv'
urlpatterns = [
    path('', views.view1),
    path('login', views.login_view),
    path('f-pass', views.fpass_view),
    path('register', views.register_view),
    path('404', views.view_404),
]
