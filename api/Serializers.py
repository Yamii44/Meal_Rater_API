from .models import Meal, Rating
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password', )
        extra_kwargs = {'password' : {'write_only' : True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user
    
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id','title','description','number_of_ratings','avg_rating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','stars','user','meal')

