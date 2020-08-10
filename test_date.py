from repan import dateType, validateDate, isDay, isMonth, isYear

# Check date type
def test_datet1():
    assert dateType('2012-12-31') == 1

def test_datet2():
    assert dateType('31-12-2012') == 2

def test_datet3():
    assert dateType('Dec-31-2012') == 3

def test_datetf():
    assert dateType('Dec-32-2012') == 0    
    
# Convert dates of 3 types
def test_answer1():
    assert validateDate('Dec-12-2012') == '2012-12-12'

def test_answer2():
    assert validateDate('12-12-2012') == '2012-12-12'
    
def test_answer3():
    assert validateDate('2012-12-12') == '2012-12-12'

    
# Validation of day, month, year
def test_day():
    assert isDay('31') == True

def test_dayf():
    assert isDay('32') == False

def test_dayf2():
    assert isDay('32f') == False

def test_month():
    assert isMonth('12') == True
    
def test_month2():
    assert isMonth('Dec') == True

def test_monthf():
    assert isMonth('13') == False

def test_monthf2():
    assert isMonth('Deb') == False
    
def test_year():
    assert isYear('2012') == True
    
def test_yearf():
    assert isYear('2007') == False

def test_yearf2():
    assert isYear('3032') == False

def test_yearf3():
    assert isYear('12') == False