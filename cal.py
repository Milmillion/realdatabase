# def this_semester_credit():
#     sum_this_credit = sum(get_credit())
#     return sum_this_credit
# # print(this_semester_credit())
#
# def cumulative_credit():
#     query = session.query(Academic)
#     list_idSub = []
#     for i in query.filter_by(Student_ID="{}".format(studenID)):
#         list_idSub.append(i.ID_Subject)
#     query = session.query(Subject)
#     d = []
#     for i in list_idSub:
#         for j in query.filter_by(ID_Subject="{}".format(i)):
#             d.append(j.Credit)
#     return sum(d)
# # print(cumulative_credit())





from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from academicSetup import Base, Academic,Gpa,Gpax,Subject
from sqlalchemy import text
engine = create_engine('sqlite:///Academics.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


# studenID = "59340500017"
# term = "1/2559"

class Get_Academic:
    def __init__(self,studenID,term):
        self.studenID = studenID
        self.term = term
    def get_id_subject(self):
        query = session.query(Academic)
        list_idSub = []
        for i in query.filter_by(Student_ID="{}".format(self.studenID),Term="{}".format(self.term)):
            list_idSub.append(i.ID_Subject)
        return list_idSub

    def get_grade(self):
        query = session.query(Academic)
        list_grade = []
        for i in query.filter_by(Student_ID="{}".format(self.studenID),Term="{}".format(self.term)):
            list_grade.append(i.Grade)
        return list_grade
    # print(get_grade())

    def get_this_semester_credit(self):
        query = session.query(Gpa)
        for i in query.filter_by(Student_ID="{}".format(self.studenID),Term="{}".format(self.term)):
            termCredit = (i.sum_credit)
        return termCredit
    # print(get_this_semester_credit())

    def get_cumulative_credit(self):
        query = session.query(Gpax)
        for i in query.filter_by(Student_ID="{}".format(self.studenID)):
            allCredit = (i.sum_all_credit)
        return allCredit
    # print(get_cumulative_credit())

    def get_GPA(self):
        query = session.query(Gpa)
        for i in query.filter_by(Student_ID="{}".format(self.studenID),Term="{}".format(self.term)):
            gpa = (i.GPA)
        return gpa
    # print(get_GPA())

    def get_GPAX(self):
        query = session.query(Gpax)
        for i in query.filter_by(Student_ID="{}".format(self.studenID)):
            gpax = (i.GPAX)
        return gpax
    # print(get_GPAX())

class test:
    def get_nameSubject(self):
        g = Get_Academic(59340500017,"1/2559")
        query = session.query(Subject)
        a = g.get_id_subject()
        b = []
        for i in a:
            for j in query.filter_by(ID_Subject="{}".format(i)):
                b.append(j.name_subject)
        return b

    def get_credit(self):
        g = Get_Academic(59340500017,"1/2559")
        query = session.query(Subject)
        c = g.get_id_subject()
        d = []
        for i in c:
            for j in query.filter_by(ID_Subject="{}".format(i)):
                d.append(j.Credit)
        return d
    # print(get_credit())

class out1:
    def output_term(self,idsub = None,namesub = None,credit = None,grade = None):
        list_output_term = []
        for i in range(len(idsub)):
            dict_output_term = {"ID Subject":idsub[i],"Name Subject":namesub[i],
             "Credit":credit[i],"Academic Regcord":grade[i]}
            list_output_term.append(dict_output_term)
        return list_output_term
class out2:
    


s = Get_Academic(59340500017,"1/2559")
o = out1()
t = test()
print(o.output_term(s.get_id_subject(),t.get_nameSubject(),t.get_credit(),s.get_grade()))
