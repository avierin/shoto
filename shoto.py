import pytest
def sum_score(army):
    if len(army) != 3:
        return 0

    return sum([v for v,c in army])

def run_score(army):
    
    if len(army) != 3:
        return 0
    
    army = sorted(army)
    
    if army[0][0] + 2 == army[2][0]:
        return army[2][0]
    
    return 0


def color_score(army):
    if len(army) != 3 or len(set(c for v,c in army)) != 1:
        return 0

    return sum(v for v,c in army)

def color_run_score(army):
    if len(set(c for v, c in army)) > 1 or len(army) != 3:
        return 0

    army = sorted(army)

    if (army[0][0] == army[2][0] - 2 ):
        return army[2][0]

    return 0


def three_kind_score(army):
    print("three kind", army)
    if len(army) == 3 and len(set(v for v,c in army)) == 1:
        return army[0][0]

    print("\t not a three")
    return 0


def get_stone_winner_for(waytowin, p1Game, p2Game, first_to_finish = 1):
    s1, s2 = waytowin(p1Game), waytowin(p2Game)
    if s1 == 0 and s2 == 0:
        return 0

    if s1 > s2:
        return 1
    elif s1 < s2:
        return 2
    else:
        return first_to_finish

def get_stone_winner(p1Game, p2Game):
    if len(p1Game) > 3 or len(p2Game) > 3:
        raise Exception(f"Wrong input {p1Game} {p2Game}")

    if len(p1Game) != 3 or len(p2Game) != 3:
        return 0

    
    for way in [color_run_score, three_kind_score, color_score, run_score, sum_score]:

        w = get_stone_winner_for(way, p1Game, p2Game)
        print(f"for {way} w={w}") 
        if w != 0:
            return w

    return 0


def test_get_stone_winner():
    
    #color suite vs three of k
    assert 1 == get_stone_winner([(1,1), (2,1), (3,1)],
            [(3,3),(3,1),(3,6)])
    #three of k vs color
    assert 2 == get_stone_winner([(4,1), (6,1), (9,1)],
            [(3,3),(3,1),(3,6)])
    #color vs run
    assert 1 == get_stone_winner([(4,1), (6,1), (7,1)],
            [(7,3),(8,1),(9,6)])
    #run vs sum
    assert 2 == get_stone_winner([(9,1), (8,2), (6,3)],
            [(3,3),(4,1),(5,6)])



def test_color_run_score():
    assert 3 == color_run_score([(1,1),(2,1),(3,1)])
    assert 0 == color_run_score([(1,1),(2,1),(3,2)])
    assert 0 == color_run_score([(1,1),(2,1),(4,1)])


def test_three_kind_score():
    assert 8 == three_kind_score([(8,1),(8,2),(8,3)])
    assert 0 == three_kind_score([(7,1),(8,2),(8,3)])


def test_color_score():
    assert 7 == color_score([(1,1),(2,1),(4,1)])
    assert 0 == color_score([(1,1),(2,2),(4,1)])


def test_run_score():
    assert 3 == run_score([(1,1),(2,2),(3,1)])
    assert 0 == run_score([(1,1),(2,2),(4,1)])
   
def test_sum_score():
    assert 10 == sum_score([(1,1),(3,2),(6,4)])
  
