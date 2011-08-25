from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('subscription.views',
    url(r'^sucesso/(?P<id>\d+)/$', 'success', name='subs_success'),
    url(r'^nova/$', 'subscription', name='subs_new'),
)