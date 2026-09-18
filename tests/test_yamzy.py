from yamzy.yamzy import Combination, Yamzy


def test_get_score_sums_the_ones():
    yamzy = Yamzy()

    score = yamzy.get_score([1, 2, 1, 4, 5], Combination.ONES)

    assert score == 2
