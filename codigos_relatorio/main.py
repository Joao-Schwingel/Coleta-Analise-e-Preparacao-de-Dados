import os
import pandas as pd
import estatistica
import estatisticaDespesasCandidatos
import estatisticaDespesasPartido
import estatisticaVotacaoCandidato

def main():
    print("Iniciando Análise e Pré-Processamento de Dados")
    
    file_path = 'votacao_partido_munzona_2022_BRASIL.csv'
    file_path2 = 'despesas_contratadas_candidatos_2022_BRASIL.csv'
    file_path3 = 'despesas_contratadas_orgaos_partidarios_2022_BRASIL.csv'
    file_path4 = 'votacao_candidato_munzona_2022_BRASIL.csv'

    dataExplodeDespesa = estatisticaDespesasCandidatos.show_basic_statistics(pd.read_csv(file_path2, encoding='latin1', on_bad_lines='skip', delimiter=";"))
    despesas_por_candidato = dataExplodeDespesa.groupby('NR_CANDIDATO').agg(
        VR_DESPESA_CONTRATADA=('VR_DESPESA_CONTRATADA', 'sum'),
        SG_PARTIDO=('SG_PARTIDO', 'first')
    ).reset_index()
    despesas_por_candidato['VR_DESPESA_CONTRATADA'] = despesas_por_candidato['VR_DESPESA_CONTRATADA'].round(2)

    votacaoCandidato = pd.read_csv(file_path4, encoding='latin1', on_bad_lines='skip', delimiter=";")
    votos_por_candidato = votacaoCandidato.groupby('NR_CANDIDATO').agg(
        QT_VOTOS_NOMINAIS_VALIDOS=('QT_VOTOS_NOMINAIS_VALIDOS', 'sum'),
        SG_PARTIDO=('SG_PARTIDO', 'first')
    ).reset_index()

    df_candidato = pd.merge(votos_por_candidato, despesas_por_candidato, on='NR_CANDIDATO', how='inner')
    df_candidato.to_csv('df_candidato.csv', index=False, encoding='utf-8')
    print("Arquivo df_candidato.csv salvo com sucesso.")

    dataExplodeDespesaPartido = estatisticaDespesasPartido.show_basic_statistics(pd.read_csv(file_path3, encoding='latin1', on_bad_lines='skip', delimiter=";"))
    despesas_por_partido = dataExplodeDespesaPartido.groupby('SG_PARTIDO')['VR_DESPESA_CONTRATADA'].sum().reset_index()
    despesas_por_partido['VR_DESPESA_CONTRATADA'] = despesas_por_partido['VR_DESPESA_CONTRATADA'].round(2)

    votacaoPartido = pd.read_csv(file_path, encoding='latin1', on_bad_lines='skip', delimiter=";")
    votos_por_partido = votacaoPartido.groupby('SG_PARTIDO')['QT_VOTOS_NOMINAIS_VALIDOS'].sum().reset_index()
    
    media_votos_por_partido = votacaoPartido.groupby('SG_PARTIDO')['QT_VOTOS_NOMINAIS_VALIDOS'].mean().reset_index()
    media_votos_por_partido.rename(columns={'QT_VOTOS_NOMINAIS_VALIDOS': 'MEDIA_VOTOS_PARTIDO'}, inplace=True)
    media_votos_por_partido['MEDIA_VOTOS_PARTIDO'] = media_votos_por_partido['MEDIA_VOTOS_PARTIDO'].round()

    # Junção dos DataFrames
    df_partido = pd.merge(votos_por_partido, despesas_por_partido, on='SG_PARTIDO', how='inner')
    df_partido = pd.merge(df_partido, media_votos_por_partido, on='SG_PARTIDO', how='inner')
    df_partido.rename(columns={'SG_PARTIDO': 'SG_PARTIDO_partido'}, inplace=True)
    df_partido.to_csv('df_partido.csv', index=False, encoding='utf-8')
    print("Arquivo df_partido.csv salvo com sucesso.")
    
    
    
    # df_partido['MEDIA_VOTOS_PARTIDO'] = (df_partido['QT_VOTOS_NOMINAIS_VALIDOS'] / df_candidato['NR_CANDIDATO'].count())    
    

if __name__ == "__main__":
    main()
