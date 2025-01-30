from django.contrib import admin # type: ignore
from .models import Expense

# Register your models here.

admin.site.register(Expense)
