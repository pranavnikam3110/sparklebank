from BanksWorking.models import Customer, Transaction
from django.contrib import admin
from . models import Customer, Transaction


# Register your models here.
admin.site.register(Customer)
admin.site.register(Transaction)