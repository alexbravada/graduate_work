import os
from django.contrib import admin
from django.urls import path, include
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movies.api.urls')),

]

debug = os.environ.get('DEBUG', False) == 'True'

if debug:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
