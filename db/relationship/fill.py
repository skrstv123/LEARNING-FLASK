from basics import db,Student,Subjects,mentor

a=Student('Ritu')
b=Student('Raj')

db.session.add_all([a,b])
db.session.commit()

print(Student.query.all())

c=Student.query.filter_by(name='Ritu').all()[0]



s1= Subjects('maths',a.id)
s2=Subjects('dsa',a.id)

me = mentor('skrstv',a.id)

db.session.add_all([me,s1,s2])
db.session.commit()

print(a) #should show mentor
cc=Student.query.filter_by(name='Ritu').all()[0]
cc.report_subjects()