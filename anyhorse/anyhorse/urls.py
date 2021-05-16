from django.contrib import admin
from django.urls import path, include
import main.views
import anyhorseTest.views
import community.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('community.urls')),
    path('', include('anyhorseTest.urls')),

]

