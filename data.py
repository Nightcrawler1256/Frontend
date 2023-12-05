from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nightcrawler:aVqhSmwu0navMJBp@cloudmachine.oiegdo7.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    
    atlas_db=client.get_database("edtech")
    ed_admin=atlas_db.admin
    # ed_admin.insert_many([{"name":"tom","age":19, "address":{"location":"delhi"}},{"name":"devesh","age":23,"address":{"location":"mumbai"}}])
    
    # ed_admin.insert_one({"name":"Nishant","age":25,"address":"punjab"})

    # ed_admin.insert_one({"name":"nishant", "age":28, "address":"Kolkata"})
    # ed_admin.update_one({"age":29},{"$set":{"age":27}})
    # ed_admin.update_many({"age":27},{"$set":{"age":30}})
    # ed_admin.replace_one({"age":30},{"set":{"age":32}})
    ed_admin.insert_many([{"name":"kushal","age":78}])





    print('SUCCESS')





except Exception as e:
    print(e)