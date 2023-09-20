from django.db.models import fields
from .models import item
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields=('category','subcategory','name','amount')