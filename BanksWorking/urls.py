from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('customers/',views.view_customer,name='view'),
    path('transfer/',views.make_transaction,name='transfer'),
    path('success/',views.success,name='success'),
    path("history/", views.history, name="history"),
]