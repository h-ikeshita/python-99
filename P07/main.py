def flatten(nasted_list):
    flaten_list =[]
    x = [nasted_list]

    while len(x) > 0:

        dep = x.pop(0)

        if isinstance(dep,list):
            x = dep + x

        else:
            flaten_list.append(dep)

    return flaten_list

