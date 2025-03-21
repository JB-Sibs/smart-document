from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.dateparse import parse_date
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt



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
def flight_tips(request):
    """
    Returns general flight booking tips.
    """
    tips = [
        "Book flights at least 2 months in advance for the best prices.",
        "Use incognito mode when searching for flights to avoid price hikes.",
        "Consider flying mid-week for cheaper fares.",
        "Check budget airlines, but watch out for hidden fees.",
        "Pack light to save on baggage fees."
    ]

    return Response({"flight_tips": tips})

    return Response({"nearest_embassy": embassy_info})

@csrf_exempt  # Disable CSRF for this view
@api_view(['POST'])
def nearest_embassy(request):
    embassies = {
        "united states": "Embassy in Washington D.C.",
        "united kingdom": "Embassy in London",
        "canada": "Embassy in Ottawa",
        "australia": "Embassy in Canberra",
        "japan": "Embassy in Tokyo",
        "philippines": "Embassy in Manila",
        "france": "Embassy in Paris",
        "germany": "Embassy in Berlin",
        "china": "Embassy in Beijing",
        "india": "Embassy in New Delhi"
    }

    country = request.data.get("country").lower()
    
    if not country:
        return Response({"error": "Missing 'country' parameter in request body."}, status=400)

    embassy = embassies.get(country, "No embassy found for this country.")
    return Response({"country": country, "nearest_embassy": embassy})

@csrf_exempt  # Disable CSRF for this view
@api_view(['POST'])
def customs_rules(request):
    country = request.data.get("country", "").lower()

    if not country:
        return Response({"error": "Country is required."}, status=400)

    RULES = {
        "united states": [
            "Declare cash over $10,000.",
            "No raw meats allowed.",
            "Strict drug import regulations.",
            "Firearms require ATF approval.",
            "No counterfeit goods."
        ],
        "united kingdom": [
            "No dairy products from non-EU countries.",
            "Declare cash over €10,000.",
            "Strict import limits on alcohol and tobacco.",
            "No dangerous weapons, including knives.",
            "Certain animal products require permits."
        ],
        "japan": [
            "Strict rules on prescription medicine imports.",
            "No fresh fruits or vegetables allowed.",
            "Declare cash over 1 million yen.",
            "Meat products require approval.",
            "No illegal or obscene materials."
        ],
        "canada": [
            "No firearms without special permits.",
            "Declare cash over CAD $10,000.",
            "No unpasteurized dairy from certain countries.",
            "Strict rules on plant and animal products.",
            "Personal alcohol and tobacco limits apply."
        ],
        "australia": [
            "No fresh fruits, seeds, or untreated wood.",
            "Declare all food, plant, and animal products.",
            "Strict restrictions on firearms and weapons.",
            "Medicines must have a doctor’s prescription.",
            "Declare cash over AUD $10,000."
        ],
        "philippines": [
            "Declare items worth over ₱10,000.",
            "No unlicensed firearms allowed.",
            "Strict restrictions on drugs and medicines.",
            "Gold over a certain amount must be declared.",
            "Pornographic materials are prohibited."
        ],
        "france": [
            "Limit on tobacco and alcohol imports.",
            "Declare cash over €10,000.",
            "No counterfeit goods allowed.",
            "Strict pet import regulations.",
            "Certain medicines require prescriptions."
        ],
        "germany": [
            "No more than €10,000 cash without declaration.",
            "Personal duty-free limits apply to alcohol and tobacco.",
            "Meat and dairy from non-EU countries are restricted.",
            "No weapons without proper authorization.",
            "Strict drug import controls."
        ],
        "china": [
            "Strict rules on electronic devices and books.",
            "Declare cash over 20,000 yuan.",
            "No fresh fruits or live animals.",
            "Prohibited items include political materials.",
            "Limits on personal import of alcohol and cigarettes."
        ],
        "india": [
            "Gold over 20 grams must be declared.",
            "No foreign drones allowed.",
            "Strict import restrictions on satellite phones.",
            "Personal duty-free limits on alcohol and tobacco.",
            "Electronics over a certain value must be declared."
        ]
    }

    rule = RULES.get(country)
    if not rule:
        return Response({"error": "Customs rules not available for this country."}, status=404)

    return Response({"country": country.title(), "customs_rules": rule})

@csrf_exempt  # Disable CSRF for this view
@api_view(['POST'])
def emergency_contacts(request):
    country = request.data.get("country", "").lower()

    if not country:
        return Response({"error": "Country is required."}, status=400)

    CONTACTS = {
        "united states": "+1-202-501-4444",
        "united kingdom": "+44-20-7008-1500",
        "canada": "+1-613-996-8885",
        "australia": "+61-2-6261-3305",
        "philippines": "+63-2-834-3000",
        "japan": "+81-3-3224-5000",
        "germany": "+49-30-1817-0",
        "france": "+33-1-43-17-53-53",
        "china": "+86-10-12308",
        "india": "+91-11-2301-4104"
    }

    contact = CONTACTS.get(country)
    if not contact:
        return Response({"error": "Emergency contact not available for this country."}, status=404)

    return Response({"country": country.title(), "emergency_contact": contact})

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

@api_view(['POST'])
def cost_estimate(request):
    try:
        # Extract data from request
        destination = request.data.get("destination")
        duration = request.data.get("duration", 1)  # Removed unnecessary label
        travel_style = request.data.get("travel_style", "budget").lower()  # Simplified key
        num_travelers = request.data.get("Pax", 1)  # Kept "Pax" since it's intentional

        # Input validation
        if not destination:
            return Response({"error": "Destination is required."}, status=400)

        if not isinstance(duration, int) or duration <= 0:
            return Response({"error": "Duration must be a positive integer and in Days."}, status=400)

        if not isinstance(num_travelers, int) or num_travelers <= 0:
            return Response({"error": "Number of travelers must be a positive integer."}, status=400)

        # Base cost per day by travel style
        travel_costs = {
            "budget": 50,
            "mid-range": 100,
            "luxury": 250
        }

        # Ensure valid travel style
        if travel_style not in travel_costs:
            return Response({"error": "Invalid travel style. Choose from: budget, mid-range, luxury."}, status=400)

        # Calculate total cost
        cost_per_day = travel_costs[travel_style]
        total_cost = cost_per_day * duration * num_travelers

        return Response({
            "destination": destination,
            "duration": duration,
            "travel_style": travel_style,
            "num_travelers": num_travelers,
            "estimated_cost": round(total_cost, 2),
        })
    
    except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=500)

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
        "passport": ["National ID", "Birth Certificate", "Driver's License"],
        "bank statement": ["Payslip", "Certificate of Employment", "Tax Return Document"],
        "visa application form": ["Online Visa Confirmation", "Embassy Appointment Slip"],
        "driver's license": ["National ID", "Student ID", "Company ID"],
        "birth certificate": ["Baptismal Certificate", "Affidavit of Birth", "School Records"],
        "police clearance": ["Barangay Clearance", "NBI Clearance", "Court Affidavit"],
        "medical certificate": ["Doctor’s Note", "Hospital Discharge Summary"],
        "employment certificate": ["Company ID", "Payslip", "Letter of Recommendation"],
        "residence certificate": ["Utility Bill", "Lease Agreement", "Barangay Certificate"],
        "school ID": ["Library Card", "Transcript of Records", "Enrollment Form"]
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
        "united states": "2-4 weeks",
        "united_kingdom": "3-6 weeks",
        "japan": "5-10 days",
        "canada": "4-8 weeks",
        "australia": "3-5 weeks",
        "philippines": "2-3 weeks",
        "france": "3-7 weeks",
        "germany": "4-6 weeks",
        "china": "2-5 weeks",
        "india": "2-4 weeks"
    }

    estimated_time = processing_times.get(country, "Processing time unavailable")
    return Response({"visa_processing_time": estimated_time})

@api_view(['POST'])
def visa_success_rate(request):
    country = request.data.get("country", "").lower()
    past_approval_rates = {
        "united states": "60%",
        "united_kingdom": "75%",
        "japan": "90%",
        "canada": "80%",
        "australia": "85%",
        "philippines": "70%",
        "france": "78%",
        "germany": "82%",
        "china": "65%",
        "india": "72%"
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
    "usd_to_php": 56.0,  # US Dollar to Philippine Peso 
    "eur_to_php": 61.0,  # Euro to Philippine Peso 
    "jpy_to_php": 0.38,  # Japanese Yen to Philippine Peso  
    "gbp_to_php": 71.5,  # British Pound to Philippine Peso
    "aud_to_php": 37.8,  # Australian Dollar to PHP
    "cad_to_php": 41.2,  # Canadian Dollar to PHP
    "sgd_to_php": 42.5,  # Singapore Dollar to PHP
    "cny_to_php": 7.8,   # Chinese Yuan to PHP
    "krw_to_php": 0.043, # South Korean Won to PHP
    "inr_to_php": 0.67,  # Indian Rupee to PHP

    "php_to_usd": 0.018, 
    "php_to_eur": 0.016, 
    "php_to_gbp": 0.014, 
    "php_to_aud": 0.026, 
    "php_to_cad": 0.024, 
    "php_to_sgd": 0.023, 
    "php_to_cny": 0.13,  
    "php_to_krw": 23.26, 
    "php_to_inr": 1.49,  

    "usd_to_eur": 0.91,  
    "eur_to_usd": 1.10,  
    "usd_to_gbp": 0.78,  
    "gbp_to_usd": 1.28,  
    "usd_to_jpy": 150.2, 
    "jpy_to_usd": 0.0067,
    "eur_to_gbp": 0.85,  
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
        "united states": {
            "insurance_name": "AXA Travel Insurance",
            "coverage": [
                "Medical emergencies",
                "Trip cancellations",
                "Lost or stolen baggage",
                "Emergency evacuation",
                "24/7 assistance services"
            ],
            "requirements": [
                "Valid passport",
                "Travel itinerary",
                "Proof of residency",
                "Health declaration (if required)"
            ]
        },
        "canada": {
            "insurance_name": "Allianz Global Assistance",
            "coverage": [
                "Emergency medical expenses",
                "Trip delays and interruptions",
                "Baggage loss and damage",
                "Rental car coverage",
                "Emergency repatriation"
            ],
            "requirements": [
                "Passport and visa details",
                "Travel itinerary",
                "Proof of financial means",
                "Medical history (for pre-existing conditions)"
            ]
        },
        "europe": {
            "insurance_name": "Schengen Visa Insurance",
            "coverage": [
                "Minimum coverage of €30,000",
                "Medical expenses in Schengen countries",
                "Emergency hospitalization",
                "Repatriation of remains",
                "Accidental death or disability"
            ],
            "requirements": [
                "Schengen visa application",
                "Passport and travel details",
                "Proof of accommodation",
                "Bank statements (for financial proof)"
            ]
        },
        "australia": {
            "insurance_name": "Medibank Travel Insurance",
            "coverage": [
                "Hospital and medical treatment",
                "Dental emergencies",
                "Flight cancellations",
                "Lost luggage",
                "Adventure activity coverage"
            ],
            "requirements": [
                "Valid travel documents",
                "Health insurance details",
                "Proof of sufficient funds",
                "Visa confirmation"
            ]
        },
        "united_kingdom": {
            "insurance_name": "Aviva Travel Insurance",
            "coverage": [
                "Emergency medical expenses",
                "Lost or stolen items",
                "Trip cancellations",
                "Personal liability",
                "Legal assistance"
            ],
            "requirements": [
                "Passport and visa (if required)",
                "Proof of travel dates",
                "Financial statements",
                "Health assessment (if needed)"
            ]
        },
        "japan": {
            "insurance_name": "Tokio Marine Travel Insurance",
            "coverage": [
                "Medical treatment in Japan",
                "Personal accident coverage",
                "Trip delays and interruptions",
                "Lost baggage",
                "Natural disaster coverage"
            ],
            "requirements": [
                "Valid passport",
                "Proof of travel plans",
                "Visa confirmation (if required)",
                "Emergency contact details"
            ]
        },
        "china": {
            "insurance_name": "Ping An Travel Insurance",
            "coverage": [
                "Medical expenses",
                "Accident compensation",
                "Flight delays and cancellations",
                "Personal liability",
                "Emergency evacuation"
            ],
            "requirements": [
                "Travel visa",
                "Passport",
                "Itinerary proof",
                "Medical records (if needed)"
            ]
        },
        "south_korea": {
            "insurance_name": "Samsung Fire & Marine Insurance",
            "coverage": [
                "Hospitalization and medical treatment",
                "Trip cancellations",
                "Lost baggage",
                "Personal accident coverage",
                "Adventure sports coverage"
            ],
            "requirements": [
                "Valid passport",
                "Proof of travel bookings",
                "K-ETA (if required)",
                "Financial proof"
            ]
        },
        "philippines": {
            "insurance_name": "Malayan Travel Insurance",
            "coverage": [
                "Medical and hospital expenses",
                "Baggage loss and delay",
                "Flight cancellations",
                "Personal liability",
                "Emergency assistance services"
            ],
            "requirements": [
                "Valid ID or passport",
                "Proof of travel itinerary",
                "Payment confirmation",
                "Health declaration (if needed)"
            ]
        },
        "india": {
            "insurance_name": "Tata AIG Travel Insurance",
            "coverage": [
                "Medical emergencies",
                "Flight delays and cancellations",
                "Loss of personal belongings",
                "Accident coverage",
                "Legal assistance"
            ],
            "requirements": [
                "Valid passport",
                "Visa confirmation",
                "Proof of travel bookings",
                "Medical assessment (if applicable)"
            ]
        }
    }

    insurance = recommendations.get(country, "No recommendation available.")
    return Response({"insurance_recommendation": insurance})

@csrf_exempt  # Disable CSRF for this view
@api_view(['POST'])
def packing_checklist(request):
    """
    Get packing suggestions based on season and purpose.
    Example request body: { "season": "winter", "purpose": "hiking" }
    """

    season_packing = {
        "winter": ["Heavy coat", "Gloves", "Thermal wear", "Snow boots"],
        "summer": ["Light clothing", "Sunglasses", "Sunscreen", "Flip-flops"],
        "rainy": ["Raincoat", "Waterproof shoes", "Umbrella", "Quick-dry clothes"],
        "autumn": ["Sweater", "Scarf", "Light jacket", "Comfortable walking shoes"],
        "spring": ["Light sweater", "Hat", "Comfortable shoes", "Sunscreen"]
    }

    purpose_packing = {
        "hiking": ["Hiking boots", "Backpack", "Water bottle", "Trekking poles", "First aid kit"],
        "business": ["Formal wear", "Laptop", "Notepad", "Business cards", "Dress shoes"],
        "beach": ["Swimsuit", "Beach towel", "Sunglasses", "Flip-flops", "Sunscreen"],
        "casual": ["Casual clothes", "Comfortable shoes", "Everyday accessories", "Light backpack"]
    }

    season = request.data.get("season", "").strip().lower()
    purpose = request.data.get("purpose", "").strip().lower()

    if not season or not purpose:
        return Response({"error": "Both 'season' and 'purpose' are required in the request body."}, status=400)

    season_list = season_packing.get(season, [])
    purpose_list = purpose_packing.get(purpose, [])

    if not season_list and not purpose_list:
        return Response({"error": "Invalid season and purpose."}, status=400)

    # Merge lists while avoiding duplicates
    final_packing_list = list(set(season_list + purpose_list))

    return Response({
        "season": season,
        "purpose": purpose,
        "packing_list": final_packing_list
    })

@csrf_exempt  # Disable CSRF for this view
@api_view(['POST'])
def travel_restrictions(request):
    country = request.data.get("country", "").strip().title()

    if not country:
        return Response({"error": "Country is required."}, status=400)

    TRAVEL_RESTRICTIONS = {
        "United States": {
            "visa_required": True,
            "covid_test_required": False,
            "quarantine_days": 0,
            "banned_travelers": ["Iran", "North Korea"]
        },
        "Canada": {
            "visa_required": True,
            "covid_test_required": True,
            "quarantine_days": 14,
            "banned_travelers": []
        },
        "United Kingdom": {
            "visa_required": True,
            "covid_test_required": False,
            "quarantine_days": 0,
            "banned_travelers": []
        },
        "Australia": {
            "visa_required": True,
            "covid_test_required": True,
            "quarantine_days": 7,
            "banned_travelers": []
        },
        "Japan": {
            "visa_required": True,
            "covid_test_required": True,
            "quarantine_days": 3,
            "banned_travelers": []
        },
        "China": {
            "visa_required": True,
            "covid_test_required": True,
            "quarantine_days": 14,
            "banned_travelers": ["USA", "UK"]
        },
        "Germany": {
            "visa_required": True,
            "covid_test_required": False,
            "quarantine_days": 0,
            "banned_travelers": []
        },
        "France": {
            "visa_required": True,
            "covid_test_required": False,
            "quarantine_days": 0,
            "banned_travelers": []
        },
        "Italy": {
            "visa_required": True,
            "covid_test_required": False,
            "quarantine_days": 0,
            "banned_travelers": []
        },
        "India": {
            "visa_required": True,
            "covid_test_required": True,
            "quarantine_days": 7,
            "banned_travelers": []
        },
        "United Arab Emirates": {
            "visa_required": False,
            "covid_test_required": False,
            "quarantine_days": 0,
            "banned_travelers": []
        },
        "Brazil": {
            "visa_required": False,
            "covid_test_required": False,
            "quarantine_days": 0,
            "banned_travelers": []
        },
        "Russia": {
            "visa_required": True,
            "covid_test_required": False,
            "quarantine_days": 0,
            "banned_travelers": ["Ukraine"]
        },
        "Saudi Arabia": {
            "visa_required": True,
            "covid_test_required": True,
            "quarantine_days": 3,
            "banned_travelers": []
        },
        "Thailand": {
            "visa_required": False,
            "covid_test_required": True,
            "quarantine_days": 7,
            "banned_travelers": []
        },
        "South Africa": {
            "visa_required": True,
            "covid_test_required": True,
            "quarantine_days": 7,
            "banned_travelers": []
        },
        "Philippines": {
            "visa_required": False,
            "covid_test_required": False,
            "quarantine_days": 0,
            "banned_travelers": []
        }
    }

    restrictions = TRAVEL_RESTRICTIONS.get(country)

    if not restrictions:
        return Response({"error": "Travel restrictions for this country are not available."}, status=404)

    return Response({
        "country": country,
        "visa_required": restrictions["visa_required"],
        "covid_test_required": restrictions["covid_test_required"],
        "quarantine_days": restrictions["quarantine_days"],
        "banned_travelers": restrictions["banned_travelers"]
    })