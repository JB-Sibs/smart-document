from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.dateparse import parse_date
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Disable CSRF for this view
@api_view(['GET'])
def common_mistakes(request):
    return Response({"mistakes": ["Missing signatures", "Incorrect fees", "Expired documents"]})

@csrf_exempt  # Disable CSRF for this view
@api_view(['GET'])
def visa_types(request):
    return Response({"visa_types": ["Tourist Visa", "Student Visa", "Work Visa"]})

@csrf_exempt  # Disable CSRF for this view
@api_view(['GET'])
def visa_rejection_reasons(request):
    reasons = [
        "Incomplete documentation",
        "Insufficient financial proof",
        "Previous visa violations",
        "Inaccurate or false information",
        "Failure to meet health requirements"
    ]
    return Response({"visa_rejection_reasons": reasons})

@csrf_exempt  # Disable CSRF for this view
@api_view(['GET'])
def emergency_contacts(request):
    contacts = {
        "US": "+1-202-501-4444",
        "UK": "+44-20-7008-1500",
        "Canada": "+1-613-996-8885",
        "Australia": "+61-2-6261-3305",
        "Philippines": "+63-2-834-3000"
    }
    return Response({"emergency_contacts": contacts})

@csrf_exempt  # Disable CSRF for this view
@api_view(['GET'])
def best_season(request):
    seasons = {
        "Japan": "Spring (March - May) for cherry blossoms",
        "Switzerland": "Winter (December - February) for skiing",
        "Thailand": "Cool season (November - February)",
        "Italy": "Spring (April - June) for sightseeing",
        "Australia": "Summer (December - February) for beaches"
    }
    return Response({"best_season": seasons})

@csrf_exempt  # Disable CSRF for this view
@api_view(['GET'])
def customs_rules(request):
    rules = {
        "US": "Declare cash over $10,000. No raw meats allowed.",
        "UK": "No dairy products from non-EU countries.",
        "Japan": "Strict rules on prescription medicine imports.",
        "Canada": "No firearms without special permits.",
        "Australia": "No fresh fruits, seeds, or untreated wood."
    }
    return Response({"customs_rules": rules})

@api_view(['POST'])
def required_docs(request):
    """
    Get required documents for a specific visa type.
    Example request body: { "visa_type": "tourist" }
    """
    visa_requirements = {
        "tourist": ["Passport", "Visa Application Form", "Proof of Funds", "Travel Itinerary"],
        "student": ["Passport", "Student Visa Application Form", "Acceptance Letter", "Proof of Tuition Payment"],
        "work": ["Passport", "Work Visa Application Form", "Employment Contract", "Medical Clearance"],
    }

    visa_type = request.data.get("visa_type", "").strip().lower()

    if not visa_type:
        return Response({"error": "visa_type is required in the request body."}, status=400)

    requirements = visa_requirements.get(visa_type, ["No specific requirements found."])

    return Response({"visa_type": visa_type, "required_documents": requirements})

@csrf_exempt  # Disable CSRF for this view
@api_view(['POST'])
def check_expiry(request):
    expiry_date_str = request.data.get("expiry_date")
    if not expiry_date_str:
        return Response({"error": "expiry_date is required"}, status=400)

    expiry_date = parse_date(expiry_date_str)
    if not expiry_date:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD"}, status=400)

    today = datetime.today().date()
    is_expired = expiry_date < today

    return Response({"expiry_date": expiry_date_str, "is_expired": is_expired})

@csrf_exempt  # Disable CSRF for this view
@api_view(['POST'])
def cost_estimate(request):
    documents = request.data.get("documents", [])
    if not isinstance(documents, list):
        return Response({"error": "Invalid input format. Expected a list of documents."}, status=400)

    total_cost = sum(doc.get("cost", 0) for doc in documents)

    return Response({"total_cost": total_cost, "documents_count": len(documents), "breakdown": documents})

@csrf_exempt  # Disable CSRF for this view
@api_view(['POST'])
def document_validation(request):
    if not request.FILES:
        return Response({"error": "No file uploaded"}, status=400)

    uploaded_file = list(request.FILES.values())[0]
    allowed_types = ['application/pdf', 'image/jpeg', 'image/png']
    if uploaded_file.content_type not in allowed_types:
        return Response({"error": "Invalid file type. Only PDF, JPG, and PNG are allowed."}, status=400)

    return Response({"message": "File uploaded successfully", "filename": uploaded_file.name}, status=200)

@csrf_exempt  # Disable CSRF for this view
@api_view(['POST'])
def missing_docs(request):
    required_docs = request.data.get("required_docs", [])
    provided_docs = request.data.get("provided_docs", [])

    if not isinstance(required_docs, list) or not isinstance(provided_docs, list):
        return Response({"error": "Invalid input format. Expected lists for required_docs and provided_docs."}, status=400)

    missing_documents = [doc for doc in required_docs if doc not in provided_docs]

    return Response({"missing_docs": missing_documents}, status=200)

@api_view(['POST'])
def smart_expiry_check(request):
    expiry_date_str = request.data.get("expiry_date")
    travel_date_str = request.data.get("travel_date")

    if not expiry_date_str or not travel_date_str:
        return Response({"error": "Both expiry_date and travel_date are required."}, status=400)

    try:
        expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")
        travel_date = datetime.strptime(travel_date_str, "%Y-%m-%d")

        if expiry_date < travel_date:
            return Response({"status": "Warning", "message": "Your document will expire before your trip. Renew now!"})

        return Response({"status": "Valid", "message": "Your document is valid for the trip."})

    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

@api_view(['POST'])
def budget_breakdown(request):
    try:
        total_budget = float(request.data.get("total_budget", 0))
        
        if total_budget <= 0:
            return Response({"error": "Total budget must be greater than zero."}, status=400)

        allocation = {
            "Accommodation (40%)": round(total_budget * 0.4, 2),
            "Food & Drinks (25%)": round(total_budget * 0.25, 2),
            "Transport (15%)": round(total_budget * 0.15, 2),
            "Activities & Tours (10%)": round(total_budget * 0.10, 2),
            "Miscellaneous (10%)": round(total_budget * 0.10, 2),
        }

        return Response({"budget_breakdown": allocation})

    except ValueError:
        return Response({"error": "Invalid input. Please provide a numerical value for total_budget."}, status=400)

@api_view(['POST'])
def alternative_docs(request):
    required_docs = request.data.get("required_docs", [])
    available_docs = request.data.get("available_docs", [])

    alternative_suggestions = {
        "passport": "National ID or Birth Certificate",
        "bank statement": "Payslip or Certificate of Employment",
        "visa application form": "Online visa confirmation",
    }

    missing_alternatives = {
        doc: alternative_suggestions.get(doc, "No alternative available")
        for doc in required_docs if doc not in available_docs
    }

    return Response({"alternative_docs": missing_alternatives})

@api_view(['POST'])
def visa_processing_time(request):
    country = request.data.get("country", "").lower()
    processing_times = {
        "usa": "2-4 weeks",
        "uk": "3-6 weeks",
        "canada": "4-8 weeks",
        "australia": "3-5 weeks",
        "japan": "5-10 days",
    }

    estimated_time = processing_times.get(country, "Processing time unavailable")
    return Response({"visa_processing_time": estimated_time})

@api_view(['POST'])
def visa_success_rate(request):
    country = request.data.get("country", "").lower()
    past_approval_rates = {
        "usa": "60%",
        "uk": "75%",
        "canada": "80%",
        "australia": "85%",
        "japan": "90%",
    }

    success_rate = past_approval_rates.get(country, "No data available")
    return Response({"visa_success_rate": success_rate})

@csrf_exempt  
@api_view(['POST'])
def travel_mode_cost(request):
    travel_modes = {
        "plane": 500,
        "train": 100,
        "bus": 50,
        "car": 75,
    }
    mode = request.data.get("mode", "").lower()
    cost = travel_modes.get(mode, "Cost not available for this mode.")
    return Response({"mode": mode, "cost": cost})

@csrf_exempt  
@api_view(['POST'])
def convert_currency(request):
    conversion_rates = {
        "usd_to_php": 56.0,
        "eur_to_php": 61.0,
        "jpy_to_php": 0.38,
    }

    amount = float(request.data.get("amount", 0))
    from_currency = request.data.get("from_currency", "").lower()
    to_currency = request.data.get("to_currency", "").lower()
    conversion_key = f"{from_currency}_to_{to_currency}"

    if conversion_key in conversion_rates:
        converted_amount = round(amount * conversion_rates[conversion_key], 2)
        return Response({"converted_amount": converted_amount})
    else:
        return Response({"error": "Conversion rate not available."}, status=400)

@csrf_exempt  
@api_view(['POST'])
def insurance_recommend(request):
    country = request.data.get("country", "").lower()
    recommendations = {
        "usa": "AXA Travel Insurance",
        "canada": "Allianz Global Assistance",
        "europe": "Schengen Visa Insurance",
        "australia": "Medibank Travel Insurance",
    }
    insurance = recommendations.get(country, "No recommendation available.")
    return Response({"insurance_recommendation": insurance})
