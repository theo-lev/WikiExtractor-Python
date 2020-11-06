import unittest
import os
from Tests.function_number import IteratorURL


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(8, IteratorURL('Comparison_between_Esperanto_and_Ido'))

    def test_link11(self):
        self.assertEqual(0, IteratorURL('Comparison_of_Axis_&_Allies_games'))

    def test_link12(self):
        self.assertEqual(0, IteratorURL('Comparison_of_C_Sharp_and_Visual_Basic_.NET'))

    def test_link13(self):
        self.assertEqual(1, IteratorURL('Comparison_of_Chernobyl_and_other_radioactivity_releases'))

    def test_link14(self):
        self.assertEqual(0, IteratorURL('Comparison_of_Exchange_ActiveSync_clients'))

    def test_link15(self):
        self.assertEqual(4, IteratorURL('Comparison_of_Hokkien_writing_systems'))

    def test_link16(self):
        self.assertEqual(0, IteratorURL('Comparison_of_Home_Owners'+'_and_Civic_Associations'))

    def test_link17(self):
        self.assertEqual(2, IteratorURL('Comparison_of_IOC,_FIFA,_and_ISO_3166_country_codes'))

    def test_link18(self):
        self.assertEqual(6, IteratorURL('Comparison_of_Java_and_C++'))

    def test_link19(self):
        self.assertEqual(6, IteratorURL('Comparison_of_Linux_distributions'))

    def test_link20(self):
        self.assertEqual(1, IteratorURL('Comparison_of_MD_and_DO_in_the_United_States'))

    def test_link324(self):
        self.assertEqual(16, IteratorURL('Comparison_of_programming_languages_(basic_instructions)'))

    def test_link325(self):
        self.assertEqual(83, IteratorURL('List_of_AMD_graphics_processing_units'))

    def test_link327(self):
        self.assertEqual(12, IteratorURL('List_of_Intel_graphics_processing_units'))

    def test_link329(self):
        self.assertEqual(20, IteratorURL('Comparison_of_Nvidia_chipsets'))

    def test_link330(self):
        self.assertEqual(84, IteratorURL('List_of_Nvidia_graphics_processing_units'))

    def test_link331(self):
        self.assertEqual(21, IteratorURL('Comparison_of_TLS_implementations'))

    def test_link332(self):
        self.assertEqual(10, IteratorURL('Comparison_of_antivirus_software'))

    def test_link333(self):
        self.assertEqual(11, IteratorURL('Comparison_of_email_clients'))

    def test_link334(self):
        self.assertEqual(28, IteratorURL('Comparison_of_integrated_development_environments'))

    def test_link335(self):
        self.assertEqual(24, IteratorURL('Comparison_of_layout_engines_(XHTML_1.1)'))

if __name__ == '__main__':
    unittest.main()
