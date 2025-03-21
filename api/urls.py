from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Smart Document & Budget Advisor API",
        default_version='v1',
        description="API for document verification and budget estimation",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from .views import (
    visa_rejection_reasons, # 1
    best_season, # 2
    nearest_embassy, # 3
    flight_tips, # 4
    
    customs_rules, # 5
    emergency_contacts, # 6
    required_docs, # 7
    check_expiry, # 8
    cost_estimate, # 9
    missing_docs, # 10 
    smart_expiry_check, # 11
    budget_breakdown, # 12
    alternative_docs, # 13
    visa_processing_time, # 14
    visa_success_rate, # 15
    travel_mode_cost, # 16
    convert_currency, # 17
    insurance_recommend, # 18
    packing_checklist, # 19
    travel_restrictions # 20
)



urlpatterns = [
    # GET Endpoints
    path('visa-rejection-reasons/', visa_rejection_reasons, name='visa-rejection-reasons'),
    path('best-season/', best_season, name='best-season'),
    path('nearest-embassy/', nearest_embassy, name='nearest_embassy'),
    path('flight-tips/', flight_tips, name='flight_tips'),

    # POST Endpoints
    path('customs-rules/', customs_rules, name='customs-rules'),
    path('emergency-contacts/', emergency_contacts, name='emergency-contacts'),
    path('required-docs/', required_docs, name='required_docs'),
    path('check-expiry/', check_expiry, name='check-expiry'),
    path('cost-estimate/', cost_estimate, name='cost-estimate'),
    path('missing-docs/', missing_docs, name='missing_docs'),
    path('smart-expiry-check/', smart_expiry_check, name='smart-expiry-check'),
    path('budget-breakdown/', budget_breakdown, name='budget-breakdown'),
    path('alternative-docs/', alternative_docs, name='alternative-docs'),
    path('visa-processing-time/', visa_processing_time, name='visa-processing-time'),
    path('visa-success-rate/', visa_success_rate, name='visa-success-rate'),
    path('travel-mode-cost/', travel_mode_cost, name='travel-mode-cost'),
    path('convert-currency/', convert_currency, name='convert-currency'),
    path('insurance-recommend/', insurance_recommend, name='insurance-recommend'),
    path('packing-checklist/', packing_checklist, name='packing-checklist'),
    path('travel-restrictions/', travel_restrictions, name='travel-restrictions'),

    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
