def test_example():
    assert 5 > 3

def test_conflict():
    assert 8 > 1

def test_conflict_2():
    assert 8 > 5

def test_conflict_3():
    assert 8 > 7
    
def test_example_refactoring():
    assert 5 > 3

def test_conflict_master():
    assert 8123 > 11

def test_conflict_2_master_resolve():
    assert 10 > 6

def test_conflict_3_master():
    assert 823 > 27

def test_example_main_refactoring():
    assert 435 > 345

def test_conflict_4_master_resolve():
    assert 29 > 9