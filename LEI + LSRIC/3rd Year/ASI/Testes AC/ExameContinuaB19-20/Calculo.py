import json

import LerFicheiro


def ModalidadeSocios(dictionary):
    # Modalidade -> { Modalidade: { NSocio: [(ValorPagar,DataPagamento ), (), ...] }}
    # ModalidadesSocio -> { Modalidade: Nº de sócios }
    modalidadesSocio = {}
    for modalidade in dictionary.keys():
        modalidadesSocio[modalidade] = len(dictionary[modalidade].keys())

    return modalidadesSocio


def ModalidadesPagar(dictionary):
    # Modalidade -> { Modalidade: { NSocio: [(ValorPagar,DataPagamento ), (), ...] }}
    # SociosSemPagar -> { NSocio: ValorAtraso}
    sociosSemPagar = {}
    for modalidade in dictionary.keys():
        for socio in dictionary[modalidade].keys():
            for infoPag in dictionary[modalidade][socio]:
                if infoPag[1] == "":
                    if socio in sociosSemPagar.keys():
                        sociosSemPagar[socio] += float(infoPag[0])
                    else:
                        sociosSemPagar[socio] = float(infoPag[0])
    return sociosSemPagar
