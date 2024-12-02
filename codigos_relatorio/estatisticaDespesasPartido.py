import pandas as pd

def show_basic_statistics(
    data, 
):
    
    data['VR_DESPESA_CONTRATADA'] = data['VR_DESPESA_CONTRATADA'].str.replace(',', '.').str.split(',')

    data_exploded = data.explode('VR_DESPESA_CONTRATADA')
    data_exploded['VR_DESPESA_CONTRATADA'] = pd.to_numeric(data_exploded['VR_DESPESA_CONTRATADA'], errors='coerce')
    return data_exploded;
    # despesas_por_partido = data_exploded.groupby('SG_PARTIDO')['VR_DESPESA_CONTRATADA'].sum().reset_index()