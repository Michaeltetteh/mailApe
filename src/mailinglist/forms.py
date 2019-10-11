from django import forms
from mailinglist.models import (
    MailingList,
    Subscriber,
    Message
)


class SubscriberForm(forms.ModelForm):
    mailing_list = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=MailingList.objects.all(),
        disable=True,
    )

    class Meta:
        model = Subscriber
        fields = ['mailing_list', 'email']


class MessageForm(forms.ModelForm):
    mailing_list = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=MailingList.objects.all(),
        disable=True,
    )

    class Meta:
        model = Message
        fields = ['mailing_list', 'subject', 'body']


class MailingListForm(forms.ModelForm):
    mailing_list = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=get_user_model().objects.all(),
        disable=True,
    )

    class Meta:
        model = MailingList
        fields = ['owner', 'name']
