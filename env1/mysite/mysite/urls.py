from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url('myapp1/', include('myapp1.urls')),
    url(r'^admin/', admin.site.urls),
]
