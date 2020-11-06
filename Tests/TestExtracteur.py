import unittest
import os
from Tests.function_number import IteratorURL


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(8, IteratorURL('Comparison_between_Esperanto_and_Ido'))

if __name__ == '__main__':
    unittest.main()
