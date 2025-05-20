import geopandas as gpd
from shapely.geometry import Point

def df_to_geodf(df, lon_col='longitude', lat_col='latitude'):
    geometry = [Point(xy) for xy in zip(df[lon_col], df[lat_col])]
    return gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
