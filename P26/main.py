import itertools
def combination(combi_length,parts):    
    combi_tuple = list(itertools.combinations(parts,combi_length));
    combi_list = []
    for i in combi_tuple:
        combi_list.append(list(i))
    return combi_list
         
