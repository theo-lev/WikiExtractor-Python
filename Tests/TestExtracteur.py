import unittest
import os
from Tests.function_number import IteratorURL


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(8, IteratorURL('Comparison_between_Esperanto_and_Ido'))
        self.assertEqual(24, IteratorURL('Comparison_of_layout_engines_(XHTML_1.1)'))
        self.assertEqual(28, IteratorURL('Comparison_of_integrated_development_environments'))
        self.assertEqual(11, IteratorURL('Comparison_of_email_clients'))
        self.assertEqual(10, IteratorURL('Comparison_of_antivirus_software'))
        self.assertEqual(21, IteratorURL('Comparison_of_TLS_implementations'))
        self.assertEqual(84, IteratorURL('List_of_Nvidia_graphics_processing_units'))
        self.assertEqual(20, IteratorURL('Comparison_of_Nvidia_chipsets'))
        self.assertEqual(12, IteratorURL('List_of_Intel_graphics_processing_units'))
        self.assertEqual(83, IteratorURL('List_of_AMD_graphics_processing_units'))
        self.assertEqual(16, IteratorURL('Comparison_of_programming_languages_(basic_instructions)'))

if __name__ == '__main__':
    unittest.main()
