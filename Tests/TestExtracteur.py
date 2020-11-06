import unittest
import os
from Tests.function_number import IteratorURL

#TESTS

class MyTestCase(unittest.TestCase):

    def test_link1(self):
        self.assertEqual(8, IteratorURL('Comparison_between_Esperanto_and_Ido'))

    def test_link2(self):
        self.assertEqual(3, IteratorURL('Comparison_between_Esperanto_and_Interlingua'))

    def test_link3(self):
        self.assertEqual(5, IteratorURL('Comparison_between_Esperanto_and_Novial'))

    def test_link4(self):
        self.assertEqual(2, IteratorURL('Comparison_between_Ido_and_Interlingua'))

    def test_link5(self):
        self.assertEqual(2, IteratorURL('Comparison_between_Ido_and_Novial'))

    def test_link6(self):
        self.assertEqual(1, IteratorURL('Comparison_between_U.S._states_and_countries_by_GDP_(PPP)'))

    def test_link7(self):
        self.assertEqual(1, IteratorURL('Comparison_of_ALGOL_68_and_C++'))

    def test_link8(self):
        self.assertEqual(3, IteratorURL('Comparison_of_Afrikaans_and_Dutch'))

    def test_link9(self):
        self.assertEqual(6, IteratorURL('Comparison_of_Android_e-book_reader_software'))

    def test_link10(self):
        self.assertEqual(40, IteratorURL('Comparison_of_Asian_national_space_programs'))

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

if __name__ == '__main__':
    unittest.main()
