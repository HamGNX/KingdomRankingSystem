from db_connection import create_connection

def insert_data(season, rank_number, trophies, rank_name):
    connection = create_connection()
    cursor = connection.cursor()

    query = "INSERT INTO season_rankings (season, rank_number, trophies, rank_name) VALUES (%s, %s, %s, %s)"
    values = (season, rank_number, trophies, rank_name)

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

# Example usage
insert_data('Season 3', 200, 7500, 'Elite 2')