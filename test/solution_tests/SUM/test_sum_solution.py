from lib.solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        print("checking 1 + 2")
        assert SumSolution().compute(1, 2) == 2

    def test_sum_0(self):
        assert SumSolution().compute(0, 10) == 10

