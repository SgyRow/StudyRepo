def convert_meters(value_meters):
    conversion_units = {
        'Километры': 0.001,
        'Метры': 1,
        'Сантиметры': 100,
        'Миллиметры': 1000,
        'Дюймы': 39.3701,
        'Футы': 3.28084,
        'Ярды': 1.09361,
        'Чейны': 0.049709695,
        'Фурлонги': 0.0049709695,
        'Мили': 0.000621371,
        'Древнеримские мили': 0.0006747638,
        'Сухопутные лье': 0.0002250023,
        'Русские мили': 0.0001339118


    }
    return {unit: value_meters * factor for unit, factor in conversion_units.items()}

def print_results(meters, converted):
    print(f"\nРезультаты конвертации {meters} м:")
    print("="*35)
    print("Метрическая система:")
    print(f"  Километры: {converted['Километры']:.4f}")
    print(f"  Метры:     {converted['Метры']:.4f}")
    print(f"  Сантиметры: {converted['Сантиметры']:.2f}")
    print(f"  Миллиметры: {converted['Миллиметры']:.2f}")
    print("\nИмперская система:")
    print(f"  Дюймы: {converted['Дюймы']:.2f}")
    print(f"  Футы:  {converted['Футы']:.2f}")
    print(f"  Ярды:  {converted['Ярды']:.2f}")
    print(f"  Чейны:  {converted['Чейны']:.2f}")
    print(f"  Фурлонги:  {converted['Фурлонги']:.4f}")
    print(f"  Мили:  {converted['Мили']:.6f}")
    print("\nПрочие единицы измерения длины:")
    print(f"  Древнеримские мили: {converted['Древнеримские мили']:.6f}")
    print(f"  Русские мили:  {converted['Русские мили']:.6f}")
    print("="*35 + "\n")

def main():
    print("Конвертер метров (для выхода введите 'exit')")
    print("-------------------------------------------")
    
    while True:
        input_value = input("\nВведите количество метров: ").strip().lower()
        
        if input_value in ['exit', 'выход']:
            print("Завершение работы конвертера...")
            break
            
        try:
            meters = float(input_value)
            converted = convert_meters(meters)
            print_results(meters, converted)
            
        except ValueError:
            print("Ошибка: Введите числовое значение или 'exit' для выхода")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

