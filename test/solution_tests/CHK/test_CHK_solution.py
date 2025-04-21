from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestHLO():
    def test_hlo(self):
        assert CheckoutSolution.checkout(self, "ABCCD") == 135
        assert CheckoutSolution.checkout(self, "AAAAAAABBBBBCD") == 465