from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
     url(r'^$', 'users.views.home', name='home'),
     url(r'^userreg/$', 'users.views.signupuser', name='userreg'),
     url(r'^lawyerreg/$', 'users.views.signuplawyer', name='lawyerreg'),
     url(r'^login/$', 'users.views.login', name='login'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
