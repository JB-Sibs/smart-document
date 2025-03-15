from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Welcome to Smart Document & Budget Advisor API!"})

@api_view(['GET'])
def test_view(request):
    return Response({"message": "Smart API is running!"})

@api_view(['GET'])
def document_requirements(request):
    data = {
        "tourist_visa": ["Passport", "Visa application form", "Flight itinerary", "Proof of funds"],
        "business_visa": ["Passport", "Invitation letter", "Company registration", "Proof of funds"],
        "student_visa": ["Passport", "University acceptance letter", "Proof of tuition payment", "Proof of funds"]
    }
    return Response(data)
