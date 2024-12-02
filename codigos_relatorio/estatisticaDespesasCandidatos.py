import pandas as pd

def convert_to_numeric(column):
    return pd.to_numeric(column, errors='coerce')

def show_basic_statistics(data):
    # Converter a coluna VR_DESPESA_CONTRATADA para numérico, coergindo erros
    # data['VR_DESPESA_CONTRATADA'] = convert_to_numeric(data['VR_DESPESA_CONTRATADA'])
    
    # Verificar dados faltantes na coluna VR_DESPESA_CONTRATADA
    
    # missing_despesas = data['VR_DESPESA_CONTRATADA'].isnull().sum()
    # if missing_despesas > 0:
    #     print(f"Atenção: A coluna 'VR_DESPESA_CONTRATADA' contém {missing_despesas} valores faltantes (ou valores convertidos para NaN).")
    # else:
    #     print("A coluna 'VR_DESPESA_CONTRATADA' não contém valores faltantes.")

    # Contar o total de instâncias
    # total_instancias = data.shape[0]

    # Agregar despesas totais por candidato
    # data['VR_DESPESA_CONTRATADA'].fillna(0, inplace=True)
    data['VR_DESPESA_CONTRATADA'] = data['VR_DESPESA_CONTRATADA'].str.replace(',', '.').str.split(',')

    data_exploded = data.explode('VR_DESPESA_CONTRATADA')
    data_exploded['VR_DESPESA_CONTRATADA'] = pd.to_numeric(data_exploded['VR_DESPESA_CONTRATADA'], errors='coerce')
    return data_exploded;

    # despesas_por_candidato = data_exploded.groupby('NR_CANDIDATO')['VR_DESPESA_CONTRATADA'].sum().reset_index()
    # Converter valores de VR_DESPESA_CONTRATADA para inteiro
    # despesas_por_candidato['VR_DESPESA_CONTRATADA'] = despesas_por_candidato['VR_DESPESA_CONTRATADA'].astype(int)
    # # Calcular média e desvio padrão das despesas
    # media_despesa = despesas_por_candidato['VR_DESPESA_CONTRATADA'].mean()
    # desvio_padrao_despesas = despesas_por_candidato['VR_DESPESA_CONTRATADA'].std()

    # # Adicionar coluna com a comparação com a média
    # despesas_por_candidato['DIFERENCA_MEDIA'] = despesas_por_candidato['VR_DESPESA_CONTRATADA'] - media_despesa
    # despesas_por_candidato['DESVIO_PADRAO'] = (despesas_por_candidato['DIFERENCA_MEDIA'] / desvio_padrao_despesas).round(2)

    # pd.set_option('display.max_rows', None)

    # print(f"Total de instâncias: {total_instancias}")
    # print("Despesas por Candidato e Análise Estatística:")
    # print(despesas_por_candidato[['NR_CANDIDATO', 'VR_DESPESA_CONTRATADA', 'DESVIO_PADRAO']])
    # print(f"Média de Despesas por Candidato: {media_despesa}")