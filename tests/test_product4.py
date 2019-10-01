from sample.product import Product


class TestProduct:
    def setup_method(self):
        """Set-up code can be factored out, will be run before every single test"""
        self.cherry_red_dr_martens =  Product("DrMartensVeganBoots", 44, "CherryRed")

    def test_transform_name_for_sku(self):
        expected_value = "DRMARTENSVEGANBOOTS"
        actual_value = self.cherry_red_dr_martens.transform_name_for_sku()
        assert expected_value == actual_value

    def test_generate_sku(self):
        expected_value = "DRMARTENSVEGANBOOTS-44-CHERRYRED"
        actual_value = self.cherry_red_dr_martens.generate_sku()
        assert expected_value == actual_value

    def teardown_method(self):
        """Tear-down code can be factored out, will be run to tidy up after every single test"""
        self.cherry_red_dr_martens=None



