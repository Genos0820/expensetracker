from django.db import models # type: ignore

# Create your models here.

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date=models.DateField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return f"{self.name}"
