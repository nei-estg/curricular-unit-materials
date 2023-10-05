def Totais(dictionary):
    # Cartao -> { NCliente: { Mes: [ValorGasto, ValorAcumulado] } }
    # ClientesInfo -> {NCliente: { TotalGasto: , TotalAcumulado: } }
    clientesInfo = {}
    for client in dictionary.keys():
        totalGasto = 0
        totalAcumulado = 0
        for clientMonth in dictionary[client].keys():
            totalGasto += int(dictionary[client][clientMonth][0][0])
            totalAcumulado += int(dictionary[client][clientMonth][0][1])

            # if client in clientesInfo.keys():
            #     clientesInfo[client].update({"TotalGasto": totalGasto, "TotalAcumulado": totalAcumulado})
            # else:
            clientesInfo[client] = {"TotalGasto": totalGasto, "TotalAcumulado": totalAcumulado}

    return clientesInfo


def TopCliente(dictionary):
    # Cartao -> { NCliente: { Mes: [ValorGasto, ValorAcumulado] } }
    # ClientesMes -> {NCliente :[ meses ]
    clienteMes = {}
    for client in dictionary.keys():
        for clientMonth in dictionary[client].keys():
            totalGasto = int(dictionary[client][clientMonth][0][0])
            totalAcumulado = int(dictionary[client][clientMonth][0][1])
            if totalAcumulado > totalGasto:
                if client in clienteMes.keys():
                    clienteMes[client].append(clientMonth)
                else:
                    clienteMes[client] = [clientMonth]
    return clienteMes
