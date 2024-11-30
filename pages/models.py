from django.db import models

# Create your models here.
def upload_employee_image(instance,file_name):
    extension=file_name.split('.')[1]
    return f'Employee/{instance}.{extension}'

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)
    salary = models.IntegerField(max_length=100)
    image =models.ImageField(upload_to=upload_employee_image, blank=True, null=True)



    def __str__(self):
        return self.name