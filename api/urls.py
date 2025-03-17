from django.urls import path
from .views import (
    common_mistakes, # X
    visa_types, # X
    visa_rejection_reasons, # 1
    emergency_contacts, # 2
    best_season, # 3
    customs_rules, # 4

    required_docs, # 5
    check_expiry, # 6
    cost_estimate, # 7
    document_validation, # X
    missing_docs, # 8 
    smart_expiry_check, # 9
    budget_breakdown, # 10
    alternative_docs, # 11
    visa_processing_time, # 12
    visa_success_rate, # 13
    travel_mode_cost, # 14
    convert_currency, # 15
    insurance_recommend # 16
    #/embassy-location/<country>/ # 18
    #/flight-tips/ # 19
    # ????????? # 20
)

urlpatterns = [
    # GET Endpoints
    path('common-mistakes/', common_mistakes, name='common-mistakes'),
    path('visa-types/', visa_types, name='visa-types'),
    path('visa-rejection-reasons/', visa_rejection_reasons, name='visa-rejection-reasons'),
    path('emergency-contacts/', emergency_contacts, name='emergency-contacts'),
    path('best-season/', best_season, name='best-season'),
    path('customs-rules/', customs_rules, name='customs-rules'),

    # POST Endpoints
    path('required-docs/', required_docs, name='required_docs'),
    path('check-expiry/', check_expiry, name='check-expiry'),
    path('cost-estimate/', cost_estimate, name='cost-estimate'),
    path('document-validation/', document_validation, name='document-validation'),
    path('missing-docs/', missing_docs, name='missing_docs'),
    path('smart-expiry-check/', smart_expiry_check, name='smart-expiry-check'),
    path('budget-breakdown/', budget_breakdown, name='budget-breakdown'),
    path('alternative-docs/', alternative_docs, name='alternative-docs'),
    path('visa-processing-time/', visa_processing_time, name='visa-processing-time'),
    path('visa-success-rate/', visa_success_rate, name='visa-success-rate'),
    path('travel-mode-cost/', travel_mode_cost, name='travel-mode-cost'),
    path('convert-currency/', convert_currency, name='convert-currency'),
    path('insurance-recommend/', insurance_recommend, name='insurance-recommend'),

]
