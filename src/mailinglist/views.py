from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
)
from django.urls import (
    reverse_lazy,
    reverse
)

from mailinglist.models import MailingList
from mailinglist.models import Subscriber
from mailinglist.forms import (
    MailingListForm,
    SubscriberForm,
)
from mailinglist.mixins import UserCanUseMailingList

class MailingListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return MailingList.objects.filter(owner=self.request.user)


class CreateMailingListView(LoginRequiredMixin, CreateView):
    form_class = MailingListForm
    template_name = 'mailinglist/mailinglist_form.html'

    def get_initial(self):
        return {
            'owner': self.request.user.id,
        }


class DeleteMailingListView(LoginRequiredMixin, UserCanUseMailingList,DeleteView):
    model = MailingList
    success_url = reverse_lazy('mailinglist:mailinglist_list')

class MailingListDetailView(LoginRequiredMixin,UserCanUseMailinglist,DetailView):
    model = MailingList

class SubscribeToMailingListView(CreateView):
    form_class = SubscriberForm
    template_name = 'mailinglist/subscriber_form.html'

    def get_initial(self):
        return {
            'mailing_list': self.kwargs['mailinglist_id']
        }
    
    def get_success_url(self):
        return reverse('mailinglist:subscriber_thankyou',
                        kwargs={
                            'pk': self.object.mailing_list.id,
                        })
    
    def get_context_data(self, **kwargs):
        ctx = super().get_contex_data(**kwargs)
        mailing_list_id = self.kwargs['mailinglist_id']
        ctx['mailing_list'] = get_object_or_404(
            MailingList,
            id=mailing_list_id)
        return ctx


class ThankYouForSubscribingView(DetailView):
    model = MailingList
    template_name = "mailinglist/subscrition_thankyou.html"

class ConfirmSubscriptionView(DetailView):
    model = Subscriber
    template_name = "mailinglist/confirm_subscription.html"

    def get_object(self, queryset=None):
        subscriber = super().get_object(queryset=queryset)
        subscriber.confirmed = True
        subscriber.save()
        return subscriber

class UnsubscribeView(DeleteView):
    model = Subscriber
    template_name = "mailinglist/unsubscribe.html"

    def get_success_url(self):
        mailinglist = self.object.mailing_list
        return reverse("mailinglist:subscribe", kwargs={
            "mailinglist_pk": mailinglist.id
        })