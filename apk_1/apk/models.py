from django.db import models

# Create your models here.
class Register(models.Model):
     f_name =  models.CharField(max_length=50)
     l_name =  models.CharField(max_length=50)
     Phone = models.CharField(max_length=10)
     email = models.EmailField()
     pass_1 = models.CharField(max_length=256)
     City = models.CharField(max_length=50)
     State = models.CharField(max_length=50)
     Country = models.CharField(max_length=20)
     Zip_code = models.IntegerField()
     
     def __str__(self):
         return self.f_name + " " + self.l_name
     

class Login(models.Model): 
    Email = models.EmailField()
    pass_1 = models.CharField(max_length=256)
     
    def __str__(self):
         return self.Email