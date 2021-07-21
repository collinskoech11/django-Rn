from rest_framework import serializers
from .models import Article

class ArticleSerializers(serializers.Serializers):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=400)
