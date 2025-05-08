import price_info as price

def test_total_cost_shipping():
    assert(price.total_cost_shopping() == 46.75)
def test_fruit_cost():
    assert(price.cost_of_fruits('apple', 5) == 6)
    assert(price.cost_of_fruits('orange', 5) == 7)
    assert(price.cost_of_fruits('watermelon', 1) == 6.5)
    assert(price.cost_of_fruits('pineapple', 2) == 5.4)
    assert(price.cost_of_fruits('pear', 10) == 9)
    assert(price.cost_of_fruits('papaya', 1) == 2.95)
    assert(price.cost_of_fruits('pomegranate', 2) == 9.9)
