import pytest

def fuzzy_math(num1, operator, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception("We need to do fuzzy math on ints only")
    
    if operator == '+':
        result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    else:
        raise Exception(f"I don't know how to do math with '{operator}'")
    
    if result < 0:
        return "A negative number, what does that even mean?"
    elif result < 10:
        return "A small number. I can deal with that"
    elif result < 20:
        return "A medium sized number. OK"
    else:
        return "A really big number, way too big for me"
    
#Class created for test. IT NEEDS TO SAY 'Test' within
#the class to be found by pytest
class TestFuzzyMath:
    def test_non_int_input_for_num1(self):
        ''' Manual implementation for error handling tests
        error = None
        try:
            fuzzy_math('hi', '+', 2)
        except Exception as e:
            error = e   
        assert error is not None
        '''
        with pytest.raises(Exception) as exc_info:
            fuzzy_math('hi', '+', 2)
        assert 'fuzzy math on ints' in str(exc_info)

    def test_non_int_input_for_num2(self):
        with pytest.raises(Exception) as exc_info:
            fuzzy_math(2, '+', 'hi')
        assert 'fuzzy math on ints' in str(exc_info)

    def test_addition_with_small_result(self):
        assert "small number" in fuzzy_math(2, '+', 2)
        #assert fuzzy_math(2, '+', 2) == "A small number. I can deal with that"

    def test_addition_with_medium_result(self):
        assert "medium sized" in fuzzy_math(7, '+', 7)
        #assert fuzzy_math(7, '+', 7) == "A medum sized number. OK"

    def test_addition_with_large_result(self):
        assert "really big" in fuzzy_math(15, '+', 10)

    def test_addition_with_negative_result(self):
        pass

    def test_multiplication_with_small_result(self):
        pass

    def test_multiplication_with_medium_result(self):
        pass

    def test_multiplication_with_large_result(self):
        pass

    def test_multiplication_with_negative_result(self):
        pass

    def test_invalid_operator(self):
        pass