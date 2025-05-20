# utils.py
import pandas as pd

def filtrar_amazonia(df):
    lat_min, lat_max = -20.0, 5.0
    lon_min, lon_max = -75.0, -50.0
    
    filtro = (
        (df['latitude'] >= lat_min) &
        (df['latitude'] <= lat_max) &
        (df['longitude'] >= lon_min) &
        (df['longitude'] <= lon_max)
    )
    return df.loc[filtro]
