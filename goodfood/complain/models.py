from django.db import models

# Create your models here.

class Complain(models.Model):
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField( max_length=100, unique=True)
    university_name = models.CharField(max_length=200, default='')
    university_address = models.TextField(max_length=400)
    quality_choice = [('1','bad'),('2','bearable'),('3','meidum'),('4','good'),('5','select')]
    food_quality = models.CharField(max_length=20, choices=quality_choice, default='5')
    further_complain = models.TextField()
    def publish(self):
        # self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.email
