import numpy as np
from scipy.interpolate import interp1d
from db_connection import create_connection

def calculate_seasonal_approximation(season):
    connection = create_connection()
    cursor = connection.cursor()

    query = f"SELECT rank_number, trophies FROM season_rankings WHERE season = '{season}' ORDER BY rank_number"
    cursor.execute(query)
    rows = cursor.fetchall()

    rank_numbers = [row[0] for row in rows]
    trophies = [row[1] for row in rows]

    cursor.close()
    connection.close()

    # Create an interpolation model for this season
    interpolation_function = interp1d(rank_numbers, trophies, fill_value="extrapolate")
    return interpolation_function

# Example usage to estimate trophies for a given rank in 'Season 3'
season = 'Season 3'
rank_to_estimate = 5000

approximation_function = calculate_seasonal_approximation(season)
estimated_trophies = approximation_function(rank_to_estimate)
print(f"Estimated trophies for rank {rank_to_estimate} in {season}: {estimated_trophies:.2f}")