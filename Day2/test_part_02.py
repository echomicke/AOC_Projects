import part_02 as pt2

def test_process_intcode():
        expected_value = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        result = pt2.process_intcode([1, 1, 1, 4, 99, 5, 6, 0, 99])
        assert expected_value == result