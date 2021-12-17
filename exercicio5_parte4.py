import bson.regex
import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client.teste

stringToMatchWithinACity = bson.regex.Regex("New York")

reviews = db.airbnb.find_one({"address.market": stringToMatchWithinACity})

print(reviews)
