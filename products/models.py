from django.db import models

# Create your models here.

class products(models.Model):

    x=[
        ('phone','phone'),
        ('computer','computer'),
        ('lab','lab'),

    ]
    name=models.CharField(max_length=50)
    content=models.TextField(max_length=50)
    price=models.DecimalField(max_length=50)
    image=models.ImageField(upload_to="photo/%y/%m/%d")
    active=models.BooleanField(default=True)
    category=models.CharField(max_length=50,choices=x,null=True,blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Product'
        ordering =['price']
