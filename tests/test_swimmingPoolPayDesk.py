import pytest

from sample.swimming_pool_pay_desk import SwimmingPoolPayDesk

class TestSwimmingPoolPayDesk():
    def setup(self):
        self.swimming_pool_pay_desk = SwimmingPoolPayDesk()

    def test_invalid_type(self):
        with pytest.raises(TypeError):
            self.swimming_pool_pay_desk.calculate_admission_fee("young child")

    def test_invalid_value(self):
        with pytest.raises(ValueError):
            self.swimming_pool_pay_desk.calculate_admission_fee(-5)
        with pytest.raises(ValueError):
            self.swimming_pool_pay_desk.calculate_admission_fee(-1)

    def test_0_incl_6_incl(self):
        # pytest.approx used with floating point numbers, 0.005 EUR tolerance
        assert pytest.approx(1.00, 0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(0)
        assert pytest.approx(1.00, 0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(1)
        assert pytest.approx(1.00, 0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(3)
        assert pytest.approx(1.00, 0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(5)
        assert pytest.approx(1.00, 0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(6)

    def test_6_excl_16_incl(self):
        # pytest.approx used with floating point numbers, 0.005 EUR tolerance
        assert pytest.approx(2.00, abs=0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(7)
        assert pytest.approx(2.00, abs=0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(10)
        assert pytest.approx(2.00, abs=0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(15)
        assert pytest.approx(2.00, abs=0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(16)

    def test_16_excl_65_incl(self):
        # pytest.approx used with floating point numbers, 0.005 EUR tolerance
        assert pytest.approx(2.50, abs=0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(17)
        assert pytest.approx(2.50, abs=0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(53)
        assert pytest.approx(2.50, abs=0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(64)
        assert pytest.approx(2.50, abs=0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(65)

    def test_65_excl_older(self):
        # pytest.approx used with floating point numbers, 0.005 EUR tolerance
        assert pytest.approx(1.50, abs=0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(66)
        assert pytest.approx(1.50, abs=0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(75)
        assert pytest.approx(1.50, abs=0.005) == self.swimming_pool_pay_desk.calculate_admission_fee(9999)
