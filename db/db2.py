from db1 import db,test 

#create the tables
db.create_all() 

#new rows as objects 
stu1 = test('Ritu',1) 
stu2 = test('Nath',69) 

# db.session.add_all([stu1,stu2])
# # or db.add(stu1) ; db.add(stu2)
# db.session.delete(test.query.all()) 

x=test.query.get(5) #passed the id 
y=test.query.filter_by(name = 'Ritu')
 
# print(test.query.all())
print(y.all())


# see 81
