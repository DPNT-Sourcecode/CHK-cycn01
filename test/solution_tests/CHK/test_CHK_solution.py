from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestHLO():
    def test_hlo(self):
        tester = CheckoutSolution()
        assert tester.checkout("ABCCDE") == 175
        assert tester.checkout("AAAAAAAAABBBBBCD") == 535
        assert tester.checkout("gfjhb") == -1
        assert tester.checkout("BBBBBEEEE") == 235
        assert tester.checkout("FFFFF") == 40
        assert tester.checkout("HHHHHHHHHHHHHHHH") == 160
        assert tester.checkout("KKK") == 230