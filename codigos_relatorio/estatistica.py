import pandas as pd
# from sklearn.preprocessing import MinMaxScaler

def show_basic_statistics(
    data, 
    columns_to_remove=None, 
    columns_to_normalize=None
):
    if columns_to_remove:
        data.drop(columns=columns_to_remove, inplace=True)
    
    # Contar o total de instâncias
    total_instancias = data.shape[0]

    # Acho que nao precisa normalizar
    # if columns_to_normalize:
    #     columns_to_normalize = [col for col in columns_to_normalize if col != 'QT_VOTOS_NOMINAIS_VALIDOS']
    #     scaler = MinMaxScaler()
    #     data[columns_to_normalize] = scaler.fit_transform(data[columns_to_normalize])

    # Agregar votos totais por partido
    votos_por_partido = data.groupby('SG_PARTIDO')['QT_VOTOS_NOMINAIS_VALIDOS'].sum().reset_index()

    # Calcular média e desvio padrão entre os partidos
    media_votos = votos_por_partido['QT_VOTOS_NOMINAIS_VALIDOS'].mean()
    desvio_padrao_votos = votos_por_partido['QT_VOTOS_NOMINAIS_VALIDOS'].std()

    # Adicionar coluna com a comparação com a média
    votos_por_partido['DIFERENCA_MEDIA'] = votos_por_partido['QT_VOTOS_NOMINAIS_VALIDOS'] - media_votos
    votos_por_partido['DESVIO_PADRAO'] = (votos_por_partido['DIFERENCA_MEDIA'] / desvio_padrao_votos).round(2)

    print(f"Total de instâncias: {total_instancias}")
    print("Votos Totais por Partido e Análise Estatística:")
    print(votos_por_partido[['SG_PARTIDO', 'QT_VOTOS_NOMINAIS_VALIDOS', 'DIFERENCA_MEDIA', 'DESVIO_PADRAO']])
    print(f"Média de Votos por Partido: {media_votos}")
