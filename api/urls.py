from django.urls import path
from api import views  # Importing the views module

urlpatterns = [
    path('hello/', views.hello_world, name='api-hello'),
    path('test/', views.test_view, name='api-test'),
    path('documents/', views.document_requirements, name='api-documents'),
]
