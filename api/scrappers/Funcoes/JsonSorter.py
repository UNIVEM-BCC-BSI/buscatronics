def JsonSorter(value):
    totalGrupos = 0
    jsonRetorno = []

    if len(value) % 50 == 0:
        totalGrupos = len(value) // 50
    else:
        totalGrupos = (len(value) // 50) + 1
    
    for x in range(totalGrupos):
        jsonRetorno.append(value[(x*50) : (x*50)+51])
    
    return jsonRetorno

