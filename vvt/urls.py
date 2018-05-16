from django.urls import path
from . import views, models

urlpatterns = [
    path('', views.IndexView.as_view(), name='vvt_index'),
    path('<int:pk>', views.pa_as_pdf, name='pdf_view'),
]
