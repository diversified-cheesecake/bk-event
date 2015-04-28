from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.start, name='start'),
    url(r'^entry/$', views.DataEntryView.as_view(), name='data_entry'),
    url(r'^result/$', views.DataEntryView.as_view(), name='result'),
    url(r'^save-data/$', views.save_data, name='save_data'),
    url(r'^save-add/$', views.save_and_add, name='save_and_add'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^attendee/add/$', views.AttendeeCreate.as_view(), name='attendee_add'),
    url(r'^attendee/update/(?P<pk>[0-9]+)/$', views.AttendeeUpdate.as_view(), name='attendee_update'),
    url(r'^csv-export/$', views.csv_export, name='csv_export'),
]