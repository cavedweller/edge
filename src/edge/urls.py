from django.conf.urls import *
from django.views.generic.base import TemplateView
from edge.views import *

urlpatterns = patterns(
    '',

    # UI: previously we set / to redirect to a static page, permanently. That
    # was a bad idea. First, we really want to use a template to take advantage
    # of the staticfile facility from Django for managing asset versions.
    # Second, the permanent redirect is cached in browser permanently, so now
    # we have to add a redirect from the static page to the /ui/ URL, for any
    # browser that have the redirect memorized.

    url(r'^/?$', TemplateView.as_view(template_name='edge/edge.html'), name='edge-ui'),
    url(r'^ui/?$', TemplateView.as_view(template_name='edge/edge.html')),

    # APIs

    url('^fragments/$', FragmentListView.as_view(), name='fragment_list'),
    url('^fragments/(?P<fragment_id>\d+)/$',
        FragmentView.as_view(), name='fragment'),
    url('^fragments/(?P<fragment_id>\d+)/sequence/$',
        FragmentSequenceView.as_view(), name='fragment_sequence'),
    url('^fragments/(?P<fragment_id>\d+)/annotations/$',
        FragmentAnnotationsView.as_view(), name='fragment_annotations'),
    url('^genomes/$',
        GenomeListView.as_view(), name='genome_list'),
    url('^genomes/(?P<genome_id>\d+)/annotations/$',
        GenomeAnnotationsView.as_view(), name='genome_annotations'),
    url('^genomes/(?P<genome_id>\d+)/fragments/$',
        GenomeFragmentListView.as_view(), name='genome_fragment_list'),
    url('^genomes/(?P<genome_id>\d+)/fragments/(?P<fragment_id>\d+)/$',
        GenomeFragmentView.as_view(), name='genome_fragment'),
    url('^genomes/(?P<genome_id>\d+)/$',
        GenomeView.as_view(), name='genome'),
    url('^genomes/(?P<genome_id>\d+)/blast/$',
        GenomeBlastView.as_view(), name='genome_blast'),
    url('^genomes/(?P<genome_id>\d+)/pcr/$',
        GenomePcrView.as_view(), name='genome_pcr'),
    url('^genomes/(?P<genome_id>\d+)/recombination/$',
        GenomeRecombinationView.as_view(), name='genome_recombination'),
    url('^genomes/(?P<genome_id>\d+)/create_child/$',
        GenomeCreateChildView.as_view(), name='create_child'),
)
