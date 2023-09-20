from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from API.models import Item
from API.serializers import ItemSerializer

@csrf_exempt
def item_list(request):
    if request.method == 'GET':
        items=Item.objects.all()
        serializer=ItemSerializer(items,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method == 'POST':
        data=JSONParser().parse(request)
        serializer=ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    
@csrf_exempt
def item_detail(request,pk):
    try:
        Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        items=Item.objects.all()
        serializer=ItemSerializer(items,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method == 'POST':
        data=JSONParser().parse(request)
        serializer=ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)