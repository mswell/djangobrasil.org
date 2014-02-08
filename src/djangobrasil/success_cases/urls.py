from django.conf.urls import patterns

urlpatterns = patterns(
    'success_cases.views',
    (r'^$', 'all_cases'),
    (r'^novo/$', 'new_case'),
    (r'^(?P<slug>[\w_-]+)/$', 'specific_case'),
)
