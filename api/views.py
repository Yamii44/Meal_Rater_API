from django.shortcuts import render
from .models import Meal , Rating
from rest_framework import viewsets , status
from .Serializers import MealSerializer, RatingSerializer , UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import request
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework import permissions




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny,)



class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)



    @action(detail =True , methods = ['post'] )
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            '''
            create or update 

            '''
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            # print(user)
            # username = request.data['username']
            # user =User.objects.get(username=username)
            try:
            #update 
                rating = Rating.objects.get(user=user.id,meal=meal.id) #specific rate
                rating.stars = stars 
                rating.save
                serializer = RatingSerializer(rating,many = False)

                json = {
                    'message' : 'Meal Rate Updated',
                    'result' : serializer.data
                }
                return Response( json, status= status.HTTP_400_BAD_REQUEST)

            except:
                # create if the rate does not exist
                rating = Rating.objects.create(stars=stars , meal=meal , user = user)
                serializer = RatingSerializer(rating,many = False)
                json = {
                    'message' : 'Meal Rate Created',
                    'result' : serializer.data
                }
                return Response( json, status= status.HTTP_200_OK)




        else:
            json = {
            'message' : 'kindly rate the meal first'}
            

            return Response( json, status= status.HTTP_400_BAD_REQUEST)
    


class RatingViewSet (viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated)

    def update(self, request, *args, **kwargs):
        response = {
            'message' : 'This is not how you should create or update rating',
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        response = {
            'message' : 'This is not how you should create or update rating',
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)