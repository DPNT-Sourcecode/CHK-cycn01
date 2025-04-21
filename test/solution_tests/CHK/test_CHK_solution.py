from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestHLO():
    def test_hlo(self):
        assert CheckoutSolution.checkout(self, "ABCCDE") == 175
        assert CheckoutSolution.checkout(self, "AAAAAAABBBBBCD") == 465
        assert CheckoutSolution.checkout(self, "gfjhb") == -1