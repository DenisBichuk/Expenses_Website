from django.shortcuts import render


def add_expense(request):
    return render(request, 'expenses/add_expense.html')
