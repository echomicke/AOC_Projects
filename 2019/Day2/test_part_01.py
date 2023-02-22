import part_01 as pt1

example_input = [1, 1, 1, 4, 99, 5, 6, 0, 99]

def test_pre_run():
        expected_value = [1, 12, 2, 4, 99, 5, 6, 0, 99]
        result = pt1.pre_run(example_input)
        assert expected_value == result

def test_process_intcode():
        expected_value = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        result = pt1.process_intcode([1, 1, 1, 4, 99, 5, 6, 0, 99])
        assert expected_value == result
