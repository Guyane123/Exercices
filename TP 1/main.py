from weather import getWeather
from house import open_cat_door,close_cat_door, start_wind_turbine, stop_wind_turbine
import math

LOCATION = "Hennebont" 
1 == 2

# Permet d'avoir la météo actuel 
weather = getWeather(LOCATION)

# La vitesse du vent en km/h : number

windSpeed = weather.windSpeed 
# Le lieu où la météo est pris : | string
location = weather.location
# L'état actuel de la météo : "Rain" | "Clouds | "Snow" | string
currentWeather = weather.currentWeather


def main():

    # Ecrire la logique ici
        # Si il pleut, fermer la chatière. Sinon l'ouvrir.

        # Si le vent est supérieur à 30 km/h, stoper les éoliènes. Sinon les mettres en marche.
    return 1
main()


