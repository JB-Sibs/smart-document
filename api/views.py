from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.dateparse import parse_date
import datetime

@api_view(['POST'])
def check_expiry(request):
    """
    Checks if the given document's expiry date has passed.
    Expects a JSON payload: {"expiry_date": "YYYY-MM-DD"}
    """
    expiry_date_str = request.data.get("expiry_date")
    if not expiry_date_str:
        return Response({"error": "expiry_date is required"}, status=400)

    expiry_date = parse_date(expiry_date_str)
    if not expiry_date:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD"}, status=400)

    today = datetime.date.today()
    is_expired = expiry_date < today

    return Response({
        "expiry_date": expiry_date_str,
        "is_expired": is_expired
    })

@api_view(['POST'])
def cost_estimate(request):
    """
    Estimates the total cost of processing documents.
    Expects a JSON payload: {"documents": [{"name": "Passport", "cost": 950}, ...]}
    """
    documents = request.data.get("documents", [])
    if not isinstance(documents, list):
        return Response({"error": "Invalid input format. Expected a list of documents."}, status=400)

    total_cost = sum(doc.get("cost", 0) for doc in documents)

    return Response({
        "total_cost": total_cost,
        "documents_count": len(documents),
        "breakdown": documents  # Added this for more detailed responses
    })

@api_view(['GET'])
def document_requirements(request):
    return Response({"requirements": ["Passport", "Visa Application Form", "Proof of Funds"]})

@api_view(['GET'])
def common_mistakes(request):
    return Response({"mistakes": ["Missing signatures", "Incorrect fees", "Expired documents"]})

@api_view(['GET'])
def visa_types(request):
    return Response({"visa_types": ["Tourist Visa", "Student Visa", "Work Visa"]})
