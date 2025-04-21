from lib.solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3
        assert SumSolution().compute(0, 10) == 10
        assert SumSolution().compute(100, 99) == 199
        