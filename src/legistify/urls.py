from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
     url(r'^$', 'users.views.home', name='home'),
     url(r'^signupuser/$', 'users.views.signupuser', name='signupuser'),
     url(r'^signuplawyer/$', 'users.views.signuplawyer', name='signuplawyer'),
     url(r'^login/$', 'users.views.login', name='login'),
     url(r'^userdashboard/$', 'users.views.userdashboard', name='userdashboard'),
     url(r'^send_request/', 'users.views.send_request', name='send_request'),
     url(r'^pending_request/', 'users.views.pending_request', name='pending_request'),
     url(r'^accept_request/', 'users.views.accept_request', name='accept_request'),
     url(r'^reject_request/', 'users.views.reject_request', name='reject_request'),
     url(r'^lawyerdashboard/$', 'users.views.lawyerdashboard', name='lawyerdashboard'),
     url(r'^logout_view/$', 'users.views.logout_view', name='logout'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
