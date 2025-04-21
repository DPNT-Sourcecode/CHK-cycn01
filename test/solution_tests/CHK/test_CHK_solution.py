from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestHLO():
    def test_hlo(self):
        assert CheckoutSolution.checkout(self, "ABCCDE") == 175
        assert CheckoutSolution.checkout(self, "AAAAAAAAABBBBBCD") == 555
        assert CheckoutSolution.checkout(self, "gfjhb") == -1
        assert CheckoutSolution.checkout(self, "BBBBBEEEE") == 235