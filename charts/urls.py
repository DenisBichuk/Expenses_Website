from django.urls import path
from django.views.generic import TemplateView

from charts import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='expenses/index.html'), name='home'),
    path('chart/', views.Chart, name='chart'),
    path('get_chart_data/<str:chart_type>/', views.get_chart_data, name='get_chart_data'),
    # path('add-expense/', views.add_expense, name='add-expense')
]
