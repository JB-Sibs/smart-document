from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def document_requirements(request):
    data = {"requirements": ["Passport", "Visa Application Form", "Proof of Funds"]}
    return Response(data)

@api_view(['GET'])
def common_mistakes(request):
    data = {"mistakes": ["Missing signatures", "Incorrect fees", "Expired documents"]}
    return Response(data)

@api_view(['GET'])
def visa_types(request):
    data = {"visa_types": ["Tourist Visa", "Student Visa", "Work Visa"]}
    return Response(data)
