def abbrev_name(name):
    separate_name = name.split()
    first_name = str(separate_name[0])
    second_name = str(separate_name[1])
    return f"{first_name[0].upper()}.{second_name[0].upper()}"