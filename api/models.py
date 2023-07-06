from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator



#uuid
class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def __str__(self) :
        return self.title
    def number_of_ratings(self):
         ratings = Rating.objects.filter(meal=self)
         return len(ratings)
    def avg_rating(self):
         # sum of ratings stars / len of rating how many ratings
         sum = 0
         ratings = Rating.objects.filter(meal=self) #number of ratings happened to the meal

         for x in ratings:
              sum += x.stars

         if len(ratings) > 0 :
          return sum / len(ratings)
         else:
              return 0
         
    
class Rating(models.Model):
        meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

       

        
class Meta:
    unique_together = (('user' , 'meal'),)
    index_together = (('user' , 'meal'),)
    

