# Bootstrap Django
import sys, os, os.path

def relpath(p):
    return os.path.join(os.path.dirname(__file__), p)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path = sys.path[:1] + ['./'] + sys.path[1:]
sys.path = sys.path[:1] + [relpath('../..')] + sys.path[1:]

from vocabulary.models import Vocabulary, Concept
from vocabulary.sru import Sru

def test_queries():
    vocab = Vocabulary.objects.get(node_id='4d38db0d693aa694ddc88dde24a05513')
    concepts = Concept.objects.filter(vocabulary=vocab)
    for c in concepts:
        if c.query:
            sr = Sru(c.query).parse()
            print('%s pieces in: %s' % (sr['no_of_records'], c.forward_path()))
            # c.results = sr['no_of_results']
            # c.save()

test_queries()