from django.conf.urls import url

from bridge_lti.consumer import source_preview
from bridge_lti.provider import lti_launch, create_session

urlpatterns = [
    url(r'^launch/?(?P<collection_id>\d*)/?$', lti_launch, name='launch'),
    url(r'^source/$', source_preview, name='source-preview'),
    url(r'^create_session/$', create_session),
]
