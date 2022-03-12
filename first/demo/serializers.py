from rest_framework import serializers
from .models import Book,BookNumber,Character,Authors



class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookNumber
        fields=['id','isbn_10','isbn_13']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Character
        fields=['id','name']

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Authors
        fields=['id','name','surname']


class BookSerializer(serializers.ModelSerializer):
    number=BookNumberSerializer(many=False)
    characters=CharacterSerializer(many=True)
    authors=AuthorsSerializer(many=True)
    class Meta:
        model=Book
        fields=['id','title','description','price','published','is_published','number','characters','authors']