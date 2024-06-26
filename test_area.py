import pytest  
from src.area import calculate_area_square  
  
def test_calculate_area_square():  
    assert calculate_area_square(2) == 4  
    assert calculate_area_square(2.5) == 6.25
    #last 4 digits of student id 
    #add last 4 
    assert calculate_area_square(3) == 9
    assert calculate_area_square(31) == 961
  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-2)  
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([2])
