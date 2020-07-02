import pandas as pd
from pymongo import MongoClient


def get_database():
    client = MongoClient("192.168.1.108", 60000)
    db = client.sharddemo
    return db


def main():
    # insert movies data
    db = get_database()

    movies_data = pd.read_csv("movies_metadata.csv")
    for row in movies_data.to_dict(orient='records'):
        db.movies.insert_one(row)

    # Insert credits data
    movies_data = pd.read_csv("credits.csv")
    for row in movies_data.to_dict(orient='records'):
        db.credits.insert_one(row)


if __name__ == "__main__":
    main()
