def expanded_form(data: int | str) -> [str]:
    _data = str(data).strip()
    list = [
        str(val) + '0' * (len(_data) - (i + 1))
        for i, val in enumerate(_data)
        if int(val)
    ]
    return list


print('+'.join(expanded_form(70304)))
