from my_functions import read_sales_data, total_sales_per_product, sales_over_time
import matplotlib.pyplot as plt 
import seaborn as sns 

# Считываем данные из текстового файла
sales_data = read_sales_data('Python_task_de_course/data.txt')
# Создаем словарь с выручкой по продуктам
sales_per_product_dict = total_sales_per_product(sales_data)
# Создаем словарь с выручкой по датам
sales_per_date_dict = sales_over_time(sales_data)

# Определяем продукт и дату с наибольшей выручкой 
most_value_product = max(sales_per_product_dict.items(), key=lambda x: x[1])[0]
most_value_date = max(sales_per_date_dict.items(), key=lambda x: x[1])[0]

# Отсортируем словарь с датами по возрастанию для лучшего отображения на графике
sales_per_date_dict = dict(sorted(sales_per_date_dict.items()))

# Выводим текст на экран
print("В ходе анализа определено следующее:\n")
print(f"Продукт, принесший наибольшую выручку: {most_value_product}")
print(f"Наибольшую выручка была получена: {most_value_date}\n")

# Задаем фигуру и ее размер
fig, axes = plt.subplots(1, 2, figsize=(20, 10))

# Строим столбчатую диаграмму
bar = sns.barplot(x=list(sales_per_product_dict.keys()), y=list(sales_per_product_dict.values()), ax=axes[0]);
bar.set_title('Распределение выручки по продуктам')
bar.set_xlabel('Продукты')
bar.set_ylabel('Выручка')

# Строим линейный график
line = sns.lineplot(x=list(sales_per_date_dict.keys()), y=list(sales_per_date_dict.values()), ax=axes[1]);
line.set_title('Распределение выручки в разрезе дат')
line.set_xlabel('Дата')
line.set_ylabel('Выручка')

# Сохраняем графики в специально созданную для этого папку
plt.savefig('./Python_task_de_course/plots/plot.png')