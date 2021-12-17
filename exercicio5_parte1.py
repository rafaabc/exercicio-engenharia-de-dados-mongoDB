import bson.regex
import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client.teste

stringToMatchWithinAReview = bson.regex.Regex("best place to be")

reviews = db.airbnb.find_one({"reviews": {"$elemMatch": {"comments": stringToMatchWithinAReview}}},
                             {"address": 1, "price": 1, "reviews.comments": 1, "_id": 0})

print(reviews)
