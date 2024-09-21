import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

turmas_finalizadas = pd.read_csv('dadosnormalizados.csv', header=None, index_col=0)
# print(turmas_finalizadas)
# Código para verificar o carregamento correto do csv.

#Alterando String para Dados Numericos para poder fazer calculos e contagem
turmas_finalizadas = turmas_finalizadas.replace({'P':1, 'F':0})
turmas_finalizadas['total_presencas'] = turmas_finalizadas.sum(axis=1)
num_modulos = (turmas_finalizadas.shape[1])
turmas_finalizadas['total_faltas'] = num_modulos - turmas_finalizadas['total_presencas']
turmas_finalizadas['taxa_presenca'] = (turmas_finalizadas['total_presencas']/num_modulos)*100
turmas_finalizadas['aprovação'] = turmas_finalizadas['taxa_presenca']>=70

# Codigo para agrupar os alunos por turmas
turma1=18
turma2=19
turma3=10
turma4=4
turma5=18
turma6=11
turma7=12

limites_turmas = np.cumsum([0, turma1, turma2, turma3, turma4, turma5, turma6])
def get_turma(index, limites_turmas):
    for i, limite in enumerate(limites_turmas):
        if index < limite:
            return i
    return len(limites_turmas)
turmas_finalizadas['turma'] = turmas_finalizadas.index.map(lambda x: get_turma(x, limites_turmas))

# Criação das visualizações em gráficos
# Histograma da presença de todos os alunos
sns.histplot(data=turmas_finalizadas, x='taxa_presenca', bins=20)
plt.title('Distribuição da Taxa de Presença')
plt.xlabel('Taxa de Presença (%)')
plt.ylabel('Número de Alunos')
plt.show()

# Boxplot para visualização de distribuição
sns.boxplot(x='turma', y='taxa_presenca', data=turmas_finalizadas)
plt.title('Comparação da Taxa de Presença por Turma')
plt.xlabel('Turma')
plt.ylabel('Taxa de Presença (%)')
plt.show()

media_por_turma = turmas_finalizadas.groupby('turma')['taxa_presenca'].mean()
plt.bar(media_por_turma.index, media_por_turma.values)
plt.xlabel('Turma')
plt.ylabel('Taxa de Presença Média (%)')
plt.title('Comparação da Taxa de Presença Média por Turma')
plt.show()

# Criar novas colunas com as médias de presença para cada disciplina (4 em 4 colunas para cada aluno)
turmas_finalizadas['media_disciplina_1'] = turmas_finalizadas.iloc[:, :4].mean(axis=1)
turmas_finalizadas['media_disciplina_2'] = turmas_finalizadas.iloc[:, 4:8].mean(axis=1)
turmas_finalizadas['media_disciplina_3'] = turmas_finalizadas.iloc[:, 8:12].mean(axis=1)
turmas_finalizadas['media_disciplina_4'] = turmas_finalizadas.iloc[:, 12:16].mean(axis=1)
turmas_finalizadas['media_disciplina_5'] = turmas_finalizadas.iloc[:, 16:20].mean(axis=1)
turmas_finalizadas['media_disciplina_6'] = turmas_finalizadas.iloc[:, 20:24].mean(axis=1)
turmas_finalizadas['media_disciplina_7'] = turmas_finalizadas.iloc[:, 24:28].mean(axis=1)
turmas_finalizadas['media_disciplina_8'] = turmas_finalizadas.iloc[:, 28:32].mean(axis=1)
turmas_finalizadas['media_disciplina_9'] = turmas_finalizadas.iloc[:, 32:36].mean(axis=1)
turmas_finalizadas['media_disciplina_10'] = turmas_finalizadas.iloc[:, 36:40].mean(axis=1)
turmas_finalizadas['media_disciplina_11'] = turmas_finalizadas.iloc[:, 40:44].mean(axis=1)
turmas_finalizadas['media_disciplina_12'] = turmas_finalizadas.iloc[:, 44:48].mean(axis=1)
turmas_finalizadas['media_disciplina_13'] = turmas_finalizadas.iloc[:, 48:52].mean(axis=1)
turmas_finalizadas['media_disciplina_14'] = turmas_finalizadas.iloc[:, 52:56].mean(axis=1)
turmas_finalizadas['media_disciplina_15'] = turmas_finalizadas.iloc[:, 56:60].mean(axis=1)
turmas_finalizadas['media_disciplina_16'] = turmas_finalizadas.iloc[:, 60:64].mean(axis=1)
turmas_finalizadas['media_disciplina_17'] = turmas_finalizadas.iloc[:, 64:68].mean(axis=1)
turmas_finalizadas['media_disciplina_18'] = turmas_finalizadas.iloc[:, 68:72].mean(axis=1)

df_medias_por_turma = turmas_finalizadas.groupby('turma')[['media_disciplina_1', 'media_disciplina_2', 'media_disciplina_3','media_disciplina_4','media_disciplina_5','media_disciplina_6','media_disciplina_7','media_disciplina_8','media_disciplina_9','media_disciplina_10','media_disciplina_11','media_disciplina_12','media_disciplina_13','media_disciplina_14','media_disciplina_15','media_disciplina_16','media_disciplina_17','media_disciplina_18']].mean()
df_medias_por_turma_transposto = df_medias_por_turma.T

df_medias_por_turma_transposto.plot(kind='line')
plt.xlabel('Disciplina')
plt.ylabel('Média de Presença')
plt.title('Média de Presença por Disciplina e Turma')
plt.legend(title='Turma')
plt.xticks(range(18), range(1, 19))
plt.show()
