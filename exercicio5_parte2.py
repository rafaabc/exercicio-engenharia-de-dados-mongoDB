import bson.regex
import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client.teste

stringToMatchWithinAReview1 = bson.regex.Regex("ótimo")
stringToMatchWithinAReview2 = bson.regex.Regex("amazing")
stringToMatchWithinAReview3 = bson.regex.Regex("recomendo")

reviewsComments = "reviews.comments"
reviews = db.airbnb.count_documents({"$and":
                                     [{reviewsComments: stringToMatchWithinAReview1},
                                      {reviewsComments: stringToMatchWithinAReview2},
                                      {reviewsComments: stringToMatchWithinAReview3}
                                      ]
                                     })

print(reviews)
