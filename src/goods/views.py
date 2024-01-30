from .models import Token, Good
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import TokenSerializer, GoodSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
import uuid


# Create your views here.
@api_view(['GET'])
def get_token(request):
    new_token = Token()
    new_token.save()
    response = JsonResponse({'token': new_token.id})
    return response


@api_view(['GET'])
def goods(request):
    serializer = TokenSerializer(data=request.query_params)
    if 'token' not in request.query_params:
        return HttpResponse(['Token must be present'], status=401)
    serializer.is_valid(raise_exception=True)
    token = serializer.validated_data.get('token')

    try:
        token_as_uuid = uuid.UUID(token)
        Token.objects.get(id=token_as_uuid)
    except ValueError:
        return HttpResponse(['Token is invalid'], status=401)
    except Token.DoesNotExist:
        return HttpResponse(['Token is invalid'], status=401)

    goods_list = []
    goods = Good.objects.all()
    for good in goods:
        goods_list.append(GoodSerializer(good).data)

    return Response({'goods': goods_list}, status=status.HTTP_200_OK)


@api_view(['POST'])
def new_good(request):
    serializer = TokenSerializer(data=request.query_params)
    if 'token' not in request.query_params:
        return HttpResponse(['Token must be present'], status=401)
    serializer.is_valid(raise_exception=True)
    token = serializer.validated_data.get('token')

    try:
        token_as_uuid = uuid.UUID(token)
        Token.objects.get(id=token_as_uuid)
    except ValueError:
        return HttpResponse(['Token is invalid'], status=401)
    except Token.DoesNotExist:
        return HttpResponse(['Token is invalid'], status=401)

    good_serializer = GoodSerializer(data=request.data)
    good_serializer.is_valid(raise_exception=True)
    name = good_serializer.validated_data.get('name')
    price = good_serializer.validated_data.get('price')
    amount = good_serializer.validated_data.get('price')
    if not price > 0:
        return HttpResponse(['Price must be more than 0'], status=401)
    if not amount > 0:
        return HttpResponse(['Amount must be more than 0'], status=401)

    new_good_inst = Good(name=name, price=price, amount=amount)
    new_good_inst.save()

    return Response({'success': 'true', 'message': 'The good is created.'}, status=status.HTTP_201_CREATED)
