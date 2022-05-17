from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Salary(models.Model):
    amount = models.DecimalField( max_digits=19, decimal_places=10)
    date = models.DateField('Salary entry date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.date)
    class Meta:
        verbose_name = "Salaire"    

class Category(models.Model):
    max_amount = models.DecimalField( max_digits=19, decimal_places=10)
    label = models.TextField('name')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
            return str(self.label)
    class Meta:
        verbose_name = "Categorie"    

    # depecys=models.ManyToManyField(Depency)
class Depency(models.Model):
    amount = models.DecimalField( max_digits=19, decimal_places=10)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.TextField(default="12-02-22 16:18" ,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE ,default=None)

    def __str__(self) -> str:
        return str(self.category)
    class Meta:
        verbose_name = "Depence"    
    
class Family(models.Model):
    ids =  models.TextField()
    salary = models.DecimalField( max_digits=19, decimal_places=10)
    pourcentage =  models.TextField()
    
    def __str__(self) -> str:
        return str(self.salary)
    class Meta:
        verbose_name = "Family"    
        