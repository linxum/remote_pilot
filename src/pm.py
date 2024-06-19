def parse(output):
    # Разбиваем вывод на строки
    lines = output.strip().split('\n')

    # Найти строку с заголовками
    header_line_index = -1
    for i, line in enumerate(lines):
        if '│' in line and not line.startswith('┌') and not line.startswith('└') and not line.startswith('├'):
            header_line_index = i
            break

    if header_line_index == -1:
        return []

    # Извлекаем заголовки из строки заголовков
    headers = lines[header_line_index].split('│')[1:-1]
    headers = [header.strip() for header in headers]

    # Инициализируем список для хранения данных
    data = []

    # Обрабатываем строки данных, которые находятся после строки заголовков и до конца таблицы
    for line in lines[header_line_index + 1:]:
        if '│' not in line or line.startswith('└'):
            continue
        # Разбиваем строку на ячейки данных
        cells = line.split('│')[1:-1]
        cells = [cell.strip() for cell in cells]

        # Создаем словарь для текущей строки данных
        row = {headers[i]: cells[i] for i in range(len(headers))}

        # Добавляем словарь в список данных
        data.append(row)

    return data
