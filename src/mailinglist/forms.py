from django import forms
from mailinglist.models import MailingList,Subscriber

class SubscriberForm(forms.ModelForm):
    mailing_list = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=MailingList.objects.all(),
        disable=True,
    )

    class Meta:
        model = Subscriber
        fields = ['mialing_list','email']