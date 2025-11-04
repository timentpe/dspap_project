import pandas as pd

import numpy as np
from scipy import linalg
from numpy import dot
#import matplotlib.pyplot as plt
import warnings
#import geopandas as gpd



def get_od_points(df):
    df = df.sort_values(by='datetime')
    origin = df.iloc[0]
    destination = df.iloc[-1]
    return pd.Series({
        'deviceID': origin['deviceID'],
        'origin_lon': origin['lon'],
        'origin_lat': origin['lat'],
        'destination_lon': destination['lon'],
        'destination_lat': destination['lat'],
        'start_time': origin['datetime'],
        'end_time': destination['datetime']
    })


def df_od(df, min_duration_trip=0, hour_first=0, hour_last=23):
    # Copie du DataFrame 
    tempo = df.copy()
    #Convertie en timestamp
    tempo['datetime'] = pd.to_datetime(tempo['datetime'], errors='coerce')
    #Sélectionne le créneau horaire
    tempo = tempo[(tempo['datetime'].dt.hour >= hour_first) & (tempo['datetime'].dt.hour < hour_last)]
    
    
    # Groupement par deviceID
    df_od = (
        tempo.groupby('deviceID')
        .agg({
            'lon': ['first', 'last'],
            'lat': ['first', 'last'],
            'datetime': ['first', 'last'],
            'speed_orig' : ['first', 'last', 'mean']
        })
    )
    
    # Aplatir les colonnes multi-index
    df_od.columns = ['lon_first', 'lon_last', 'lat_first', 'lat_last', 'time_first', 'time_last', 'speed_first', 'speed_last','mean_speed']
    df_od = df_od.reset_index()

    # Calcul de la durée en minutes
    df_od['duration_min'] = (df_od['time_last'] - df_od['time_first']).dt.total_seconds() / 60

    # Filtrer les trajets de plus de 10 minutes
    df_od = df_od[df_od['duration_min'] > min_duration_trip]

    return df_od



