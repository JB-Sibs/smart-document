from django.urls import path
from .views import (
    document_requirements, common_mistakes, visa_types, 
    check_expiry, cost_estimate
)

urlpatterns = [
    # GET Endpoints
    path('document-requirements/', document_requirements, name='document-requirements'),
    path('common-mistakes/', common_mistakes, name='common-mistakes'),
    path('visa-types/', visa_types, name='visa-types'),

    # POST Endpoints
    path('check-expiry/', check_expiry, name='check-expiry'),
    path('cost-estimate/', cost_estimate, name='cost-estimate'),
]
