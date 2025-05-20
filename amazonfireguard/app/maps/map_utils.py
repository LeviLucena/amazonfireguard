import geopandas as gpd
import matplotlib.pyplot as plt

def plot_fire_locations(gdf):
    """Exibe os pontos de queimadas em um mapa simples com Matplotlib"""
    gdf.plot(marker='o', color='red', markersize=3)
    plt.title("Focos de Queimada - Amazônia")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.show()
