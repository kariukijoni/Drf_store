# # Create your views here.
# from django.http import HttpResponse,JsonResponse
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from API.models import Item
# from API.serializers import ItemSerializer

# @api_view(['GET','POST'])
# def item_list(request,format=None):
#     if request.method == 'GET':
#         items=Item.objects.all()
#         serializer=ItemSerializer(items,many=True)
#         return JsonResponse(serializer.data,safe=False)
    
#     elif request.method == 'POST':
#         data=JSONParser().parse(request)
#         serializer=ItemSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)
    
# @api_view(['GET','PUT','DELETE'])
# def item_detail(request,pk,format=None):
#     try:
#         Item.objects.get(pk=pk)
#     except Item.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         items=Item.objects.all()
#         serializer=ItemSerializer(items,many=True)
#         return JsonResponse(serializer.data,safe=False)
    
#     elif request.method == 'POST':
#         data=JSONParser().parse(request)
#         serializer=ItemSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)

from .models import Item
from .serializers import ItemSerializer
from rest_framework import generics

class ItemList(generics.ListCreateAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer
    
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer