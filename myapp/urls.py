from django.conf.urls import url, include
import myapp.views as views

urlpatterns = [
    url(r'add_user', views.add_user, ),
    url(r'show_user$', views.show_user, ),
    url(r'add_record', views.add_record, ),
    url(r'show_record$', views.show_record, ),
    url(r'modify_mapper', views.modify_mapper, ),
    url(r'show_mapper$', views.show_mapper, ),
    ]
