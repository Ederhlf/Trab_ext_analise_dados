import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class AnaliseDesempenho:
    def __init__(self, df):
        self.df = df

    def grafico_frequencia(self):
        """ Gera um histograma da frequência escolar dos alunos """
        plt.figure(figsize=(8, 5))
        sns.histplot(self.df["Frequência (%)"], bins=5, kde=True, color="blue")
        plt.xlabel("Frequência Escolar (%)")
        plt.ylabel("Número de Alunos")
        plt.title("Distribuição da Frequência Escolar")
        plt.show()

   

    def grafico_barras_medias(self):
        """ Gera um gráfico de barras com a média das disciplinas """
        medias = self.df[["Média Matemática", "Média Português", "Média História", "Média Ciências"]].mean()
        plt.figure(figsize=(8, 5))
        sns.barplot(x=medias.index, y=medias.values, palette="viridis")
        plt.ylabel("Nota Média")
        plt.title("Médias das Disciplinas")
        plt.show()

    def grafico_dispersao(self):
        """ Gera um gráfico de dispersão relacionando frequência e notas """
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=self.df["Frequência (%)"], y=self.df["Média Matemática"], label="Matemática", color="red")
        sns.scatterplot(x=self.df["Frequência (%)"], y=self.df["Média Português"], label="Português", color="blue")
        sns.scatterplot(x=self.df["Frequência (%)"], y=self.df["Média História"], label="História", color="green")
        sns.scatterplot(x=self.df["Frequência (%)"], y=self.df["Média Ciências"], label="Ciências", color="purple")
        plt.xlabel("Frequência Escolar (%)")
        plt.ylabel("Notas Médias")
        plt.title("Relação entre Frequência e Notas")
        plt.legend()
        plt.show()


    def grafico_barras_medias_por_renda(self):
        medias_por_renda = self.df.groupby("Renda Familiar")[["Média Matemática", "Média Português", "Média História", "Média Ciências"]].mean()
        plt.figure(figsize=(10, 5))
        medias_por_renda.plot(kind="bar", colormap="viridis", alpha=0.8)
        plt.title("Média das Notas por Faixa de Renda")
        plt.ylabel("Nota Média")
        plt.xticks(rotation=0)
        plt.legend(title="Disciplinas")
        plt.show()

    def grafico_dispersao_frequencia_por_renda_matematica(self):
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=self.df["Frequência (%)"], y=self.df["Média Matemática"], hue=self.df["Renda Familiar"], palette="coolwarm", s=100)
        plt.xlabel("Frequência Escolar (%)")
        plt.ylabel("Nota em Matemática")
        plt.title("Frequência x Notas por Renda Familiar")
        plt.legend(title="Renda Familiar")
        plt.show()

    def grafico_dispersao_frequencia_por_renda_portugues(self):
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=self.df["Frequência (%)"], y=self.df["Média Português"], hue=self.df["Renda Familiar"], palette="coolwarm", s=100)
        plt.xlabel("Frequência Escolar (%)")
        plt.ylabel("Nota em Português")
        plt.title("Frequência x Notas por Renda Familiar")
        plt.legend(title="Renda Familiar")
        plt.show()

    def grafico_dispersao_frequencia_por_renda_historia(self):
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=self.df["Frequência (%)"], y=self.df["Média História"], hue=self.df["Renda Familiar"], palette="coolwarm", s=100)
        plt.xlabel("Frequência Escolar (%)")
        plt.ylabel("Nota em História")
        plt.title("Frequência x Notas por Renda Familiar")
        plt.legend(title="Renda Familiar")
        plt.show()

    def grafico_dispersao_frequencia_por_renda_ciencias(self):
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=self.df["Frequência (%)"], y=self.df["Média Ciências"], hue=self.df["Renda Familiar"], palette="coolwarm", s=100)
        plt.xlabel("Frequência Escolar (%)")
        plt.ylabel("Nota em Ciências")
        plt.title("Frequência x Notas por Renda Familiar")
        plt.legend(title="Renda Familiar")
        plt.show()

    def grafico_barras_medias_por_escolaridade_pais(self):
        """Gera um gráfico de barras mostrando a média das notas dos filhos agrupadas pela escolaridade dos pais."""
        medias_por_escolaridade = self.df.groupby("Escolaridade dos Pais")[
            ["Média Matemática", "Média Português", "Média História", "Média Ciências"]
        ].mean()

        plt.figure(figsize=(10, 5))
        medias_por_escolaridade.plot(kind="bar", colormap="coolwarm", alpha=0.8)
        plt.title("Média das Notas dos Filhos por Escolaridade dos Pais")
        plt.ylabel("Nota Média")
        plt.xlabel("Escolaridade dos Pais")
        plt.xticks(rotation=15)
        plt.legend(title="Disciplinas")
        plt.show()



  
    def grafico_densidade(self, coluna):
        """ Gera um gráfico de densidade (KDE) para uma determinada coluna """
        plt.figure(figsize=(8, 5))
        sns.kdeplot(self.df[coluna], fill=True, color='blue')
        plt.xlabel(coluna)
        plt.ylabel('Densidade')
        plt.title(f'Gráfico de Densidade (KDE) - {coluna}')
        plt.show()

    def grafico_correlacao(self):
        """ Gera um heatmap para mostrar a correlação entre variáveis """
        plt.figure(figsize=(8, 6))
        df_numerico = self.df.select_dtypes(include=['float64', 'int64'])

        sns.heatmap(df_numerico.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Gráfico de Correlação (Heatmap)')
        plt.show()

    
    def diagrama_pareto(self, coluna):
        """ Gera um diagrama de Pareto para uma coluna categórica """
        sorted_data = self.df[coluna].value_counts().sort_values(ascending=False)
        cumulative_percentage = sorted_data.cumsum() / sorted_data.sum() * 100
        
        fig, ax = plt.subplots(figsize=(10, 5))
        sorted_data.plot(kind='bar', color='b', ax=ax, label="Frequência")
        
        ax2 = ax.twinx()
        cumulative_percentage.plot(marker='o', color='r', ax=ax2, label="Porcentagem Acumulada")
        ax2.axhline(80, color='gray', linestyle='dashed', label="Regra 80/20")
        
        ax.set_ylabel('Frequência')
        ax2.set_ylabel('Porcentagem Acumulada')
        ax.set_xlabel(coluna)
        plt.title(f'Diagrama de Pareto - {coluna}')
        
        ax.legend(loc='upper left')
        ax2.legend(loc='upper right')
        plt.show()

# Criando um DataFrame de exemplo
dados = {
    "Nome do Aluno": [
        "Ana Silva", "Bruno Souza", "Carla Mendes", "Daniel Rocha", "Eduarda Farias", "Felipe Alves", "Gabriela Nunes",
        "Henrique Lopes", "Isabela Martins", "João Pereira", "Karina Duarte", "Lucas Santos", "Julio Augusto", "Leticia Cavas",
        "Lucia Martinelli", "Pedro Alcantara", "Lory Pontes", "Liliam Almeida", "Simone Alvez", "Alberto Cunha"
    ],
    "Frequência (%)":   [85, 70, 92, 80, 88, 75, 90, 65, 78, 82, 95, 73, 92, 75, 80, 87, 92, 55, 69, 85],
    "Média Matemática": [7.0, 6.2, 7.5, 6.9, 7.1, 6.5, 8.2, 6.8, 6.4, 7.0, 8.9, 5.9, 8.0, 8.2, 8.0, 8.5, 8.2, 8.4, 9.5, 7.0],
    "Média Português":  [7.0, 4.8, 8.3, 6.5, 7.0, 6.1, 8.0, 7.4, 6.2, 6.8, 7.7, 5.7, 5.5, 6.8, 6.8, 7.0, 7.7, 7.0, 7.0, 7.8],
    "Média História":   [8.1, 6.4, 8.7, 7.0, 6.3, 6.3, 7.4, 8.6, 6.6, 7.2, 9.0, 7.0, 6.7, 8.5, 7.8, 9.8, 7.0, 7.7, 8.0, 7.0],
    "Média Ciências":   [6.8, 5.2, 8.3, 6.2, 6.9, 6.0, 7.1, 6.5, 6.3, 6.7, 8.8, 5.7, 5.5, 6.8, 6.8, 7.0, 7.7, 7.0, 7.0, 7.8],
    "Renda Familiar": ["1 SM", "2 SM", "3 SM", "2 SM", "2 SM", "1 SM", "3 SM", "1 SM", "2 SM", "2 SM", "3 SM", "1 SM", 
                       "1 SM", "1 SM", "3 SM", "2 SM", "2 SM", "2 SM", "2 SM", "1 SM"
    ],
    "Escolaridade dos Pais": [
        "Ensino Fundamental", "Ensino Médio Incompleto", "Ensino Superior", "Ensino Médio Completo",
        "Ensino Médio Completo", "Ensino Fundamental", "Ensino Superior", "Ensino Médio Incompleto",
        "Ensino Médio Completo", "Ensino Médio Completo", "Ensino Superior", "Ensino Fundamental",
        "Ensino Médio Completo", "Ensino Fundamental", "Ensino Superior", "Ensino Médio Incompleto",
        "Ensino Médio Completo", "Ensino Médio Completo", "Ensino Superior", "Ensino Fundamental"
    ]
   
}

df = pd.DataFrame(dados)

# Criando a isnstância da classe e chamando as funções
analise = AnaliseDesempenho(df)
analise.grafico_frequencia()
analise.grafico_barras_medias()
analise.grafico_dispersao()
analise.grafico_dispersao_frequencia_por_renda_portugues()
analise.grafico_dispersao_frequencia_por_renda_matematica()
analise.grafico_dispersao_frequencia_por_renda_historia()
analise.grafico_dispersao_frequencia_por_renda_ciencias()
analise.grafico_barras_medias_por_renda()
analise.grafico_barras_medias_por_escolaridade_pais()
analise.grafico_densidade('Média Matemática')
analise.grafico_correlacao()
analise.diagrama_pareto('Escolaridade dos Pais')



# python3 analise_dados.py
# pip install pandas numpy matplotlib seaborn
