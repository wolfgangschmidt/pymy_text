import pytest 

from match import Score

def test_match_perfect():

    ret = Score(
        candidate='string 1', 
        input='string 1', 
        words=['string', '1']
        ).string_score()

    assert ret == 1.0


def test_match_partial():

    ret = Score(
        candidate=' Answer to the Ultimate Question of Life, The Universe, and Everything', 
        input='what is the ultimate question of life, the universe and everything', 
        words=[
            'what', 'is', 'the', 'ultimate', 'question', 
            'of', 'life,', 'the', 'universe', 'and', 'everything'
            ]
        ).string_score()

    assert ret == 0.8970588235294118


def test_match_words():

    ret = Score(
        candidate=' Answer to the Ultimate Question of Life, The Universe, and Everything', 
        input='what is the ultimate question of life, the universe and everything', 
        words=[
            'what', 'is', 'the', 'ultimate', 'question', 
            'of', 'life,', 'the', 'universe', 'and', 'everything'
            ]
        ).words_score()
    assert ret[0] == 0.8761951061416302


def test_match_multy_score():

    ret = Score(
        candidate=' Answer to the Ultimate Question of Life, The Universe, and Everything', 
        input='what is the ultimate question of life, the universe and everything', 
        words=[
            'what', 'is', 'the', 'ultimate', 'question', 
            'of', 'life,', 'the', 'universe', 'and', 'everything'
            ]
        ).multy_score()

    assert ret == 0.886626964835521
