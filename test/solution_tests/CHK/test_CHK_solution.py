from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestHLO():
    def test_hlo(self):
        tester = CheckoutSolution()
        assert tester.checkout("ABCCDE") == 175
        assert tester.checkout("AAAAAAAAABBBBBCD") == 535
        assert tester.checkout("sfdgdf") == -1
        assert tester.checkout("BBBBBEEEE") == 235
        assert tester.checkout("FFFFF") == 40
        assert tester.checkout("HHHHHHHHHHHHHHHH") == 135
        assert tester.checkout("J") == 60
        assert tester.checkout("KKK") == 190
        assert tester.checkout("MMMNNNN") == 190
        assert tester.checkout("PPPPPP") == 250
        assert tester.checkout("QQQQRRRR") == 280
        assert tester.checkout("UUUU") == 120
        assert tester.checkout("VVVVV") == 220
        assert tester.checkout("XZSTY") == 82