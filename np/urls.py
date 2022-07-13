
from django.conf.urls.static import static  # new
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
] 
urlpatterns += staticfiles_urlpatterns()

