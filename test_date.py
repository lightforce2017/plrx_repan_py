from repan import validateDate

assert validateDate('Dec-12-2012') == '2012-12-12'
assert validateDate('12-12-2012') == '2012-12-12'