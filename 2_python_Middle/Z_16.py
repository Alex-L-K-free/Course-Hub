# Занятие 16. Работаем с Excel
# 1. Работа с датами через datetime
# 2. Создаём эксель файл
# 3. Создаём листы в эксель файле
# 4. Записываем данные в эксель файл
# 5. Пишем жирным текстом в эксель


import datetime
date_now = datetime.datetime.now()
print(date_now)
print(f'год: {date_now.year}')
print(f'месяц: {date_now.month}')
print(f'число: {date_now.day}')
print(f'часы: {date_now.hour}')
print(f'минуты: {date_now.minute}')
print(f'секунды: {date_now.second}')
print(date_now - datetime.timedelta(days=3, hours=5))
print(date_now + datetime.timedelta(days=3))

#
# pip install XlsxWriter

import xlsxwriter
# # Create an new Excel file and add a worksheet.
# workbook = xlsxwriter.Workbook('text_file.xlsx')
# worksheet = workbook.add_worksheet()
#
# # Widen the first column to make the text clearer.
# worksheet.set_column('A:A', 20)
#
# # Add a bold format to use to highlight cells.
# bold = workbook.add_format({'bold': True})
#
# # Write some simple text.
# worksheet.write('A1', 'Hello')
#
# # Text with formatting.
# worksheet.write('A2', 'World', bold)
#
# # Write some numbers, with row/column notation.
# worksheet.write(2, 0, 123)
# worksheet.write(3, 0, 123.456)
#
# # Insert an image.
# #worksheet.insert_image('B5', 'logo.png')
#
# workbook.close()



import datetime


date_now = datetime.datetime.now()
students = {
    'Петров': {
        'Математика': [
            (date_now - datetime.timedelta(days=5), 9),
            (date_now - datetime.timedelta(days=3), 3),
            (date_now, 8)
        ],
        'Физика': [
            (date_now - datetime.timedelta(days=10), 5),
            (date_now - datetime.timedelta(days=3), 7),
            (date_now, 8)
        ]
    },
    'Сидорова': {
        'Математика': [
            (date_now - datetime.timedelta(days=5), 6),
            (date_now - datetime.timedelta(days=3), 8),
            (date_now, 8)
        ],
        'Физика': [
            (date_now - datetime.timedelta(days=10), 3),
            (date_now - datetime.timedelta(days=3), 7),
            (date_now - datetime.timedelta(days=1), 8),
            (date_now, 10),
        ]
    }
}

workbook = xlsxwriter.Workbook('test_file.xlsx')
worksheet = workbook.add_worksheet('Петров')
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Дата', bold)
worksheet.write('B1', 'Математика', bold)
worksheet.write('C1', 'Физика', bold)

# Запись дат
worksheet.write('A2', str(date_now - datetime.timedelta(days=10))[:10])
worksheet.write('A3', str(date_now - datetime.timedelta(days=5))[:10])
worksheet.write('A4', str(date_now - datetime.timedelta(days=3))[:10])
worksheet.write('A5', str(date_now)[:10])

# Запись отметок
worksheet.write('B3', 9)
worksheet.write('B4', 3)
worksheet.write('B5', 8)


# Запись отметок
worksheet.write('C2', 9)
worksheet.write('C4', 7)
worksheet.write('C5', 8)

workbook.close()