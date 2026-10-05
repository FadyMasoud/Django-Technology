from django.db import models

# Create your models here.
class Female(models.Model):
    name1 = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name1


class Male(models.Model):
    name2 = models.CharField(max_length=50,null=True)
    girls=models.OneToOneField("Female", verbose_name=("Girls Chosen"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name2



class Login(models.Model):
    username =models.CharField(max_length=50)
    password =models.CharField(max_length=50)


    def __str__(self):
        return self.username

