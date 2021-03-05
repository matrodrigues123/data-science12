import pandas as pd
df = pd.read_csv('pokemon_data.csv')

### Percorre todos os rows um por um e escreve na tela os lendários ###

# count = 0
# for index, row in df.iterrows():
#     if row['Legendary']:
#         print(index, row['Name'])
#         count += 1
# print(f'Há um total de {count} pokemons lendários')


### Localiza as rows que possuem um dado específico na colula Type 1 ###

# print(df.loc[df['Type 1'] == "Fire"])


### Organiza a tabela com base no dado Sp. Atk e escreve em ordem crescente ###

# spAtk = df.sort_values(['Sp. Atk'])
# for index, row in spAtk.iterrows():
#     print(row['Name'], row['Sp. Atk'])


### Soma os stats do pokemon, cria uma nova coluna com esse dado e diz qual o melhor pokemon com base nessa informação ###

## Jeito bronco de somar
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

## Jeito safo de somar
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# maisForte = df.sort_values(['Total'], ascending=False)
# print(maisForte.head(5))


### Mudar posição de uma coluna ###

## Jeito bronco(está incompleto)
#df = df[['Total', 'HP', 'Defense']]

## Jeito safo
# cols = list(df.columns.values)
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# print(df.head(5))
# df.to_csv('modified.csv', sep='\t')

### Localiza várias condições específicas de cada row ###
# print(df.loc[(df['Type 1'] == 'Grass') & (df['Legendary'])])

### Localizar informação específica no nome ###

# print(df.loc[~df['Name'].str.contains('Mega')])

### Modificar dado ###
# df.loc[df['Type 1'] == 'Fire', 'Type 1'] == 'Flamer'
# print(df)


### Estatísticas de grupo ###
df.groupby(['Type 1']).mean()
print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))





