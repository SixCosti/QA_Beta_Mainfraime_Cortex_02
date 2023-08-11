
def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum

def test_count_integers():
    sequence = [1, 2, 3, 4, 1, 1, 5]
    item = 1
    assert count(sequence, item) == 3

def test_count_strings():
    sequence = ['apple', 'banana', 'apple', 'orange', 'apple']
    item = 'apple'
    assert count(sequence, item) == 3