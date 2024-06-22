from django.http import JsonResponse
from django.shortcuts import render

from .models import SalesData


def Chart(request):
    return render(request, 'charts/chart.html')


def get_chart_data(request, chart_type):
    if chart_type == 'polarArea' or chart_type == 'radar' or chart_type == "bar" or chart_type == "line" or chart_type == "pie" or chart_type == "doughnut":
        sales_data = list(SalesData.objects.values('month', 'sales'))
        chart_data = {'labels': [entry['month'] for entry in sales_data],
                      'data': [entry['sales'] for entry in sales_data]}

    elif chart_type == 'area':
        sales_data = list(SalesData.objects.values('month', 'sales'))
        chart_data = {'labels': [entry['month'] for entry in sales_data], 'datasets': [{
            'label': 'Sales Data',
            'data': [entry['sales'] for entry in sales_data],
            'backgroundColor': 'rgba(75, 192, 192, 0.2)',
            'borderColor': 'rgba(75, 192, 192, 1)',
            'borderWidth': 1,
        }]}

    return JsonResponse(chart_data)
