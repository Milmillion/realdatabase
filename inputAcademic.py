from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from academicSetup import Base, Academic,Gpa,Gpax,Subject

engine = create_engine('sqlite:///Academics.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

#---------------------------add subject and grade------------------------------#
# studenID = "59340500017"
# term = "1/2559"
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA141",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA161",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN101",Grade = "3" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "LNG101",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "MTH101",Grade = "2.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "PHY103",Grade = "3" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "PHY191",Grade = "3.5" )
# session.add(student)
# session.commit()

# studenID = "59340500021"
# term = "1/2559"
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA141",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA161",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN101",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "LNG101",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "MTH101",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "PHY103",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "PHY191",Grade = "4" )
# session.add(student)
# session.commit()

# studenID = "59340500035"
# term = "1/2559"
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA141",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA161",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN101",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "LNG102",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "MTH101",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "PHY103",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "PHY191",Grade = "3.5" )
# session.add(student)
# session.commit()
#-------------------------------------------------------------------#
# studenID = "59340500017"
# term = "2/2559"
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA121",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA142",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA162",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA163",Grade = "3" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN111",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN121",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "MTH102",Grade = "2.5" )
# session.add(student)
# session.commit()

# studenID = "59340500021"
# term = "2/2559"
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA121",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA142",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA162",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA163",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN111",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN121",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "MTH102",Grade = "3.5" )
# session.add(student)
# session.commit()

# studenID = "59340500035"
# term = "2/2559"
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA121",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA142",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA162",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "FRA163",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN111",Grade = "3.5" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "GEN121",Grade = "4" )
# session.add(student)
# student = Academic(Student_ID = studenID,Term = term,
#  ID_Subject = "MTH102",Grade = "3.5" )
# session.add(student)
# session.commit()

#--------------------------------add GPA---------------------------------------#
# term = "1/2559"
# gpa = Gpa(Student_ID = "59340500017",Term =term,sum_credit =17,GPA ="3.38")
# session.add(gpa)
# gpa = Gpa(Student_ID = "59340500021",Term =term,sum_credit =17,GPA ="3.82")
# session.add(gpa)
# gpa = Gpa(Student_ID = "59340500035",Term =term,sum_credit =17,GPA ="3.76")
# session.add(gpa)
# session.commit()

# term = "2/2559"
# gpa = Gpa(Student_ID = "59340500017",Term =term,sum_credit =17,GPA ="3.47")
# session.add(gpa)
# gpa = Gpa(Student_ID = "59340500021",Term =term,sum_credit =17,GPA ="3.76")
# session.add(gpa)
# gpa = Gpa(Student_ID = "59340500035",Term =term,sum_credit =17,GPA ="3.79")
# session.add(gpa)
# session.commit()

#------------------------------add GPAX----------------------------------------#
# gpaxx = Gpax(Student_ID ="59340500017",sum_all_credit =34,GPAX ="3.42")
# session.add(gpaxx)
# gpaxx = Gpax(Student_ID ="59340500021",sum_all_credit =34,GPAX ="3.79")
# session.add(gpaxx)
# gpaxx = Gpax(Student_ID ="59340500035",sum_all_credit =34,GPAX ="3.77")
# session.add(gpaxx)
# session.commit()

#----------------------------add subject---------------------------------------#

# sub = Subject(ID_Subject ="FRA141",name_subject ="COMPUTER PROGRAMMING",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="FRA161",name_subject ="ROBOTICS EXPLORATION",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="GEN101",name_subject ="PHYSICAL EDUCATION",
#  Credit =1)
# session.add(sub)
# sub = Subject(ID_Subject ="LNG101",name_subject ="GENERAL ENGLISH",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="LNG102",name_subject ="TECHNICAL ENGLISH",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="MTH101",name_subject ="MATHEMATICS I",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="PHY103",name_subject ="GENERAL PHYSICS",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="PHY191",name_subject ="GENERAL PHYSICS LABORATORY I",
#  Credit =1)
# session.add(sub)
# sub = Subject(ID_Subject ="FRA121",name_subject ="ELECTRONIC CIRCUITS",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="FRA142",name_subject ="COMPUTER PROGRAMMING",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="FRA162",name_subject ="ROBOTICS AND AUTOMATION",
#  Credit =1)
# session.add(sub)
# sub = Subject(ID_Subject ="FRA163",name_subject ="ROBOTICS MACHINE SHOP",
#  Credit =1)
# session.add(sub)
# sub = Subject(ID_Subject ="GEN111",name_subject ="MAN AND ETHICS OF LIVING",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="GEN121",name_subject ="LEARNING AND PROBLEM SOLVING SKILLS",
#  Credit =3)
# session.add(sub)
# sub = Subject(ID_Subject ="MTH102",name_subject ="MATHEMATICS II",
#  Credit =3)
# session.add(sub)
# session.commit()
#-------------------------------------------------------------------#
