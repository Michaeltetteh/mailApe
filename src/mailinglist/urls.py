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
    path(
        "<uuid:pk>/delete",
        view.DeleteMailingListView.as_view(),
        name="delete_mailinglist"
    ),
    path(
        "<uuid:pk>/manage",
        view.MailingListDetailView.as_view(),
        name="manage_mailinglist"
    ),
    
    
]
