from django.contrib import admin
from bankaccounts.models import Account,Kyc

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user','account_number','account_balance','account_status','kyc_submitted', 'kyc_confirmed']
    list_editable = ['account_balance','account_status', 'kyc_submitted', 'kyc_confirmed']

class KycAdmin(admin.ModelAdmin):
    list_display = ['fullname','gender','identity_type']
admin.site.register(Account,AccountAdmin)
admin.site.register(Kyc,KycAdmin)
