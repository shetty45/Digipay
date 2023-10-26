from django.contrib import admin
from transactions.models import Transaction
from transactions.models import CreditCard
# Register your models here.
admin.site.register(Transaction)
admin.site.register(CreditCard)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['amount','description',]