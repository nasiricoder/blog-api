from django.contrib import admin
from django.urls import path

admin.site.site_title = 'Blog'
urlpatterns = [
    path('admin/', admin.site.urls),
]
