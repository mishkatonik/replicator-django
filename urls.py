from django.urls import path

import views

# In this example, we've separated out the views.py into a new file

urlpatterns = [
    path('the-replicator', views.replicator),
    path('about', views.about),
    path('meet-the-chef', views.meet_the_chef),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)