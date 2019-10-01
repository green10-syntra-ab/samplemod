from unittest import TestCase

from sample.product import Product


class TestProduct(TestCase):
    def test_transform_name_for_sku(self):
        cherry_red_dr_martens = Product("DrMartensVeganBoots", 44, "CherryRed")
        expected_value = "DRMARTENSVEGANBOOTS"
        actual_value = cherry_red_dr_martens.transform_name_for_sku()
        self.assertEqual(expected_value, actual_value)

    def test_generate_sku(self):
        cherry_red_dr_martens = Product("DrMartensVeganBoots", 44, "CherryRed")
        expected_value = "DRMARTENSVEGANBOOTS-44-CHERRYRED"
        actual_value = cherry_red_dr_martens.generate_sku()
        self.assertEqual(expected_value, actual_value)



