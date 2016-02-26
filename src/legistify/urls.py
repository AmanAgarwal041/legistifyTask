from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
     url(r'^$', 'users.views.home', name='home'),
     url(r'^signupuser/$', 'users.views.signupuser', name='signupuser'),
     url(r'^signuplawyer/$', 'users.views.signuplawyer', name='signuplawyer'),
     url(r'^login/$', 'users.views.login', name='login'),
     url(r'^userdashboard/$', 'users.views.userdashboard', name='userdashboard'),
     url(r'^lawyerdashboard/$', 'users.views.lawyerdashboard', name='lawyerdashboard'),
     url(r'^logout_view/$', 'users.views.logout_view', name='logout'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
