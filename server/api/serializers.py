from rest_framework import serializers

from .models import Rekomendacje
from .models import Zamowienia
from .models import Wiadomosci
from .models import Newsletter
from .models import Blog
class RecomendationsSerializers(serializers.ModelSerializer):
        class Meta:
                model = Rekomendacje
                fields = ['name', 'content']

class OrderSerializers(serializers.ModelSerializer):
        class Meta:
                model = Zamowienia
                fields = ['name', 'email', 'phone']

class BlogSerializers(serializers.ModelSerializer):
        class Meta:
                model = Blog
                fields = ['id', 'image', 'title', 'content']

class MessageSerializers(serializers.ModelSerializer):
        class Meta:
                model = Wiadomosci
                fields = ['email', 'phone', 'content']

class NewsletterSerializers(serializers.ModelSerializer):
        class Meta:
                model = Newsletter
                fields = ['email']