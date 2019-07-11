import os
import unittest

from jsonasobj import loads
from rdflib import Namespace, Graph, XSD

from biolinkml import LOCAL_TYPES_PATH
from biolinkml.generators.rdfgen import RDFGenerator
from biolinkml.generators.shexgen import ShExGenerator

sourcedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'source')

METATYPE = Namespace("https://w3id.org/biolink/biolinkml/type/")


class UriTypeTestCase(unittest.TestCase):
    def test_uri_type(self):
        """ URI datatype should map to ShEx URI instead of NONLITERAL """
        shex = loads(ShExGenerator(LOCAL_TYPES_PATH, format='json').serialize())
        uri_shape = [s for s in shex.shapes if s.id == str(METATYPE.Uri)]
        self.assertEqual(1, len(uri_shape))
        self.assertEqual('iri', uri_shape[0].nodeKind)


if __name__ == '__main__':
    unittest.main()
