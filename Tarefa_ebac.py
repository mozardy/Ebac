import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Ler o arquivo
df = pd.read_csv(r'D:\EBAC\Exercicios\ecommerce_preparados.csv')
print(df.head().to_string())

# Mostrar colunas
print(df.columns)

# Grafico de Dispersão
sns.jointplot(x='Preço', y='Desconto', data=df, kind='scatter')
plt.show()

# Mapa de calor
df_corr = df[['Preço', 'Qtd_Vendidos_Cod', 'Temporada_Cod']].corr()
sns.heatmap(df_corr, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.show()

# Gráfico de barra
plt.figure(figsize=(10, 6))
df['Gênero'].value_counts().plot(kind='bar', color='#59ff7a')
plt.title('Gênero')
plt.xlabel('Números')
plt.ylabel('Quantidade')
plt.xticks(rotation=35)
plt.show()

x = df['Temporada'].value_counts().index
y = df['Temporada'].value_counts().values

# Gráfico de Pizza
plt.figure(figsize=(18, 8))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=0)
plt.title('Temporadas do ano')
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(18, 8))
sns.kdeplot(df['Nota'], fill=True, color='#1d75f0')
plt.title('Densidade das Notas')
plt.xlabel('Nota')
plt.show()