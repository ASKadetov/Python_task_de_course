# Функция для считывания файла
def read_sales_data(file_path):
    # Создаем список ключей для словарей
    keys = ['product_name', 'quantity', 'price', 'date'] 
    with open(file_path, "r", encoding="utf-8") as f:
        # Создаем список покупок, каждую покупку преобразуем в словарь
        sales_data = [dict(zip(keys, s.strip().split(', '))) for s in f.readlines()]
    return sales_data 

# Функция для подсчета суммы продаж по продуктам
def total_sales_per_product(sales_data):
    # Создаем пустой словарь
    result_dict = {}
    for d in sales_data:
        # Если ключ присутствует в словаре, то добавляем значение к общей сумме
        if d['product_name'] in result_dict:
            result_dict[d['product_name']] += int(d['quantity']) * int(d['price'])
        # В противном случае создаем новый ключ и присваиваем ему значение
        else:
            result_dict[d['product_name']] = int(d['quantity']) * int(d['price'])
    return result_dict

# Функция для подсчета суммы продаж в разрезе дат
def sales_over_time(sales_data):
    # Создаем пустой словарь
    result_dict = {}
    for d in sales_data:
        # Если ключ присутствует в словаре, то добавляем значение к общей сумме
        if d['date'] in result_dict:
            result_dict[d['date']] += int(d['quantity']) * int(d['price'])
        # В противном случае создаем новый ключ и присваиваем ему значение
        else:
            result_dict[d['date']] = int(d['quantity']) * int(d['price'])
    return result_dict