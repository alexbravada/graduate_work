from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movies.api.urls')),

]

if DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
