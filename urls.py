from django.urls import path

import views

urlpatterns = [
    path('', views.replicator),
    path('about/', views.about),
    path('meet-the-chef/', views.meet_the_chef),
    path('contact/', views.contact),
]

# Boilerplate to include static files--NO TOUCHING!
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)