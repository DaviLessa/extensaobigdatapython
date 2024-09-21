import pandas as pd
import numpy as np

planilha1 = pd.read_excel('DadosTurmasFinalizadas.xlsx', header=None)
# print(planilha1)

def normalizar_linhas(row):
    nova_linha = []
    for i in range(0, len(row)-1, 1):
        if row[i] == row[i + 1]:
            if row[i] == "P":
                nova_linha.append("P")
            else:
                nova_linha.append("F")
        elif pd.isna(i) or pd.isna(i+1):
            nova_linha.append('F')
        else:
            nova_linha.append('F') 
    return nova_linha    

planilha1 = planilha1.apply(lambda row: normalizar_linhas(row))

planilha1.to_csv('dadosnormalizados.csv', index=True, header=False)
