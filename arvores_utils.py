from sortedcontainers import SortedDict  # Red-Black Tree (aproximada)
from bintrees import FastRBTree  # B-Tree

def popular_estrutura(estrutura, dados):
    for chave, valor in dados:
        estrutura[chave] = valor
    return estrutura

def buscar_chaves(estrutura, chaves):
    encontrados = []
    for chave in chaves:
        if chave in estrutura:
            encontrados.append(estrutura[chave])
    return encontrados