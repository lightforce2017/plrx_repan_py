from repan import validateDate

def test_answer1():
    assert validateDate('Dec-12-2012') == '2012-12-12'

def test_answer2():
    assert validateDate('12-12-2012') == '2012-12-12'
    
def test_answer3():
    assert validateDate('2012-12-12') == '2012-12-12'