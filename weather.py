import requests

url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 28.6139,
    "longitude": 77.2090,
    "start_date": "2023-01-01",
    "end_date": "2023-01-05",
    "hourly": (
        "temperature_2m,relative_humidity_2m,dew_point_2m,apparent_temperature,"
        "precipitation,precipitation_probability,weather_code,pressure_msl,surface_pressure,"
        "cloudcover,cloudcover_low,cloudcover_mid,cloudcover_high,shortwave_radiation,"
        "direct_radiation,diffuse_radiation,direct_normal_irradiance,evapotranspiration,"
        "et0_fao_evapotranspiration,vapour_pressure_deficit,windspeed_10m,winddirection_10m,"
        "windgusts_10m"
    )
}

response = requests.get(url, params=params)
data = response.json()

print(data.keys())  # Optional: to inspect top-level keys
print(data["hourly"].keys())  # Check what all hourly columns are present

# If you want, you can also convert it into a DataFrame for easier analysis:
import pandas as pd
df = pd.DataFrame(data["hourly"])
print(df.head())
