
def format_value(value):
    if isinstance(value, dict):
        formatted_items = {k: format_value(v) for k, v in value.items()}
        return formatted_items
    if isinstance(value, list):
        formatted_list = [format_value(i) for i in value]
        return formatted_list
    if isinstance(value, bool):
        return str(value).lower()
    return value


def make_string(lst):
    new_lst = []
    actions = {'same': ' ', 'remove': '-', 'update': '-', 'add': '+'}
    for i in lst:
        symbol = actions.get(i['action'])
        formatted_line = (f'{symbol} '
                          f'{i.get("name")}: {format_value(i.get("value"))}')
        new_lst.append(formatted_line)
    result_string = '{\n  ' + '\n  '.join(new_lst) + '\n}'
    return result_string
