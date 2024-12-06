def test_sum_of_numbers():
    x = 0
    for i in range(1, 100):
        x += i
    
    expected_sum = 99 * (99 + 1) // 2
    assert x == expected_sum, f"Test failed: x = {x}, expected = {expected_sum}"
