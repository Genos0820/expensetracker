from django.shortcuts import render,redirect # type: ignore
from .forms import ExpenseForm
from django.views import View
from .models import Expense

# Create your views here.

def index(request):
    if request.method =="POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()
    expense_form=ExpenseForm()
    expenses=Expense.objects.all()
    return render(request,"splitexpense/index.html",{
        "expense_form":expense_form,
        "expenses": expenses
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
    
    


    
