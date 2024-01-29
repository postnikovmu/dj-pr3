from .models import Token
from rest_framework.decorators import api_view
from django.http import JsonResponse


# Create your views here.
@api_view(['GET'])
def get_token(request):
    new_token = Token()
    new_token.save()
    response = JsonResponse({'token': new_token.id})
    return response
