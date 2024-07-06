from rest_framework import serializers
from .models import KitabPost, BabPost, FasalPost

class KitabPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitabPost
        fields = ["id", "title", "content", "published_date"]

class BabPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabPost
        fields = ["id", "title", "content", "published_date"]   
               
class FasalPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FasalPost
        fields = ["id",  "title", "content", "published_date"]  