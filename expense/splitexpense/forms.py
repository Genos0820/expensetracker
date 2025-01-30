from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields='__all__'
        exclude=('date',)
        labels={
            "name":"Expense",
            "amount":"Amount",
            "category":"Category"
        }