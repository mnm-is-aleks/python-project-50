

def make_dict(key, action, value):
    result = {'name': key, 'action': action,
              'value': value}
    return result


def compare_dct(f_1, f_2):
    result_lines = []
    for key in sorted(f_1 | f_2):
        if f_1.get(key) == f_2.get(key):
            result_lines.append(make_dict(key, 'same', f_1[key]))
        elif key not in f_2:
            result_lines.append(make_dict(key, 'remove', f_1[key]))
        elif f_1.get(key) != f_2.get(key):
            if f_1.get(key):
                result_lines.append(make_dict(key, 'update', f_1[key]))
            result_lines.append(make_dict(key, 'add', f_2[key]))
    return result_lines
