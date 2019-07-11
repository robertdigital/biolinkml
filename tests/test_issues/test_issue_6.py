import os
import unittest

from jsonasobj import loads
from rdflib import Namespace

from biolinkml.generators.shexgen import ShExGenerator

sourcedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'source')
DCT = Namespace("http://purl.org/dc/terms/")

class DefinedPrefixTestCase(unittest.TestCase):
    def test_dct_prefix(self):
        """ Make sure prefixes are handled correctly """
        with self.assertRaises(ValueError, msg="A colon in an identifier is illegal"):
            shex = loads(ShExGenerator(os.path.join(sourcedir, 'Issue_6.yaml'), format='json').serialize())
        shex = loads(ShExGenerator(os.path.join(sourcedir, 'Issue_6_fixed.yaml'), format='json').serialize())
        company_shape = [s for s in shex.shapes if 'Company' in s.id][0]
        for expr in company_shape.expression.expressions:
            if expr.min == 0:
                self.assertEqual(str(DCT.created), expr.predicate, )
                return
        self.assertFalse(True, "DCT.created predicate not found")


if __name__ == '__main__':
    unittest.main()
