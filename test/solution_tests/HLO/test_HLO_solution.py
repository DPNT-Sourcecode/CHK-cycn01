from lib.solutions.HLO.hello_solution import HelloSolution


class TestHLO():
    def test_hlo(self):
        assert HelloSolution.hello("friend") == "hello, friend"