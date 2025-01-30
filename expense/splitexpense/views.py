from django.shortcuts import render,redirect # type: ignore
from .forms import ExpenseForm
from django.views import View # type: ignore
from .models import Expense
import datetime
from django.db.models import Sum

# Create your views here.

def index(request):
    if request.method =="POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()
            
    expense_form=ExpenseForm()
    expenses=Expense.objects.all()
    total_expenses=expenses.aggregate(Sum("amount"))
    
    #logic to calculate 365 days expenses
    last_year=datetime.date.today()-datetime.timedelta(days=365)
    data=Expense.objects.filter(date__gt=last_year)
    yearly_sum=data.aggregate(Sum('amount'))
    
    #logic to calculate 30 days expenses
    last_month=datetime.date.today()-datetime.timedelta(days=30)
    data_m=Expense.objects.filter(date__gt=last_month)
    monthly_sum=data_m.aggregate(Sum('amount'))
    
    #logic to calculate 7 days expenses
    last_week=datetime.date.today()-datetime.timedelta(days=365)
    data_w=Expense.objects.filter(date__gt=last_week)
    weekly_sum=data_w.aggregate(Sum('amount'))
    
    return render(request,"splitexpense/index.html",{
        "expense_form":expense_form,
        "expenses": expenses,
        "total_expenses": total_expenses,
        "yearly_sum":yearly_sum,
        "monthly_sum":monthly_sum,
        "weekly_sum":weekly_sum,
    })

def delete(request,id):
    if request.method=="POST" and 'delete' in request.POST:
        expense=Expense.objects.get(id=id)
        expense.delete()
    return redirect('index')

    
def edit(request,id):
    expense=Expense.objects.get(id=id)
    expense_form=ExpenseForm(instance=expense)
    
    if request.method=="POST":
        ex=Expense.objects.get(id=id)
        edited_form=ExpenseForm(request.POST,instance=ex)
        if edited_form.is_valid(): 
            edited_form.save()
            return redirect('index')

    return render(request,"splitexpense/edit.html",{
        "expense_form":expense_form,
    })
    
    


    
