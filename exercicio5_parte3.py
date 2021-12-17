import bson.regex
import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client.teste

stringToMatchWithinACity = bson.regex.Regex("United States")

reviews = db.airbnb.count_documents({"address.country": stringToMatchWithinACity})

print(reviews)
