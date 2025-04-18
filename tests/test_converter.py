from Main import convert_meters

def test_convert_meters():
    result = convert_meters(1000)
    
    assert round(result['Километры'], 4) == 1.0
    assert result['Метры'] == 1000.0
    assert result['Сантиметры'] == 100000.0
    assert result['Миллиметры'] == 1000000.0

    assert round(result['Дюймы'], 2) == 39370.10
    assert round(result['Футы'], 2) == 3280.84
    assert round(result['Мили'], 6) == 0.621371