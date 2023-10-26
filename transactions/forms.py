from django import forms
from transactions.models import CreditCard

class AccountSearchForm(forms.Form):
    account_number = forms.CharField(label='Account Number', max_length=50)


class CreditCardForms(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['name','number','month','year','CVV','crad_type']