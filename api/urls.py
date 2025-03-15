from django.urls import path
from .views import document_requirements, common_mistakes, visa_types

urlpatterns = [
    path('document-requirements/', document_requirements, name='document-requirements'),
    path('common-mistakes/', common_mistakes, name='common-mistakes'),
    path('visa-types/', visa_types, name='visa-types'),
]
