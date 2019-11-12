from pymongo import MongoClient

client = MongoClient()

print("Connected to MongoDB Server\n") 

db = client.test_database 		#getting database

collection = db.test_database		#getting collection

#inserting single document

posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print("Inserted id of single document is")
print('{0}\n'.format(result.inserted_id))

#inserting multiple documents

post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}
new_result = posts.insert_many([post_1, post_2, post_3])
print("Inserted id of multiple documents are")
print('{0}\n'.format(new_result.inserted_ids))


#Finding documents
bills_post = posts.find_one({'author': 'Bill'})
print("Found document is")
print(bills_post)
