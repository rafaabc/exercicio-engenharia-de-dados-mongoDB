import bson.regex
import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client.teste

stringToMatchWithinAReview = bson.regex.Regex("best place to be")

reviewsComments = "comments"
reviews = db.airbnb.count_documents({"reviews": {"$elemMatch": {reviewsComments: stringToMatchWithinAReview}}})

print(reviews)
