from django.urls import path
from mailinglist import views


app_name = 'mailinglist'

urlpatterns = [
    path('',
         views.MailingListView.as_view(),
         name='mailinglist_list'
    ),
    path(
        'new',
        view.CreateMailingListView.as_view(),
        name='create_mailinglist'
    ),
]
