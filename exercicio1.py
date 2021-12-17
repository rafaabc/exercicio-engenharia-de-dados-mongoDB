import bson.regex
import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client.teste

wordToMatchWithinAReview = bson.regex.Regex("perfect")
reviews = db.airbnb.count_documents({"reviews.comments": wordToMatchWithinAReview})

print(reviews)
