from django.db import models

# Models can be thought as a python object. 
class Contact(models.Model):
    name= models.CharField(max_length=122) # here, name is an attribute and charfield is known as formfield which determines the datatype of attribute.
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

def __str__(self):
    return self.name
