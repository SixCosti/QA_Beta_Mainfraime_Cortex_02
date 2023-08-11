from applications.count import count

def test_count_zeros():
	assert count.count([0,0,0],0)==3

def test_count_string():
	assert count.count(["a","a","a"],"a")==3

def test_count_minus():
	assert count.count([-1,-3,-5,-4], -1)==1

def test_count_normalNum():
	assert count.count([1,2,3,4,5,6,6,5,4,3,2,1], 1)==2

def test_count_integers():
    sequence = [1, 2, 3, 4, 1, 1, 5]
    item = 1
    assert count(sequence, item) == 3

def test_count_strings():
    sequence = ['apple', 'banana', 'apple', 'orange', 'apple']
    item = 'apple'
    assert count(sequence, item) == 3