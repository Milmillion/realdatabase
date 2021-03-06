from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from academicSetup import Base, Academic,Gpa,Gpax,Subject
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
        termCredit = []
        query = session.query(Gpa)
        for i in query.filter_by(Student_ID="{}".format(self.studenID),Term="{}".format(self.term)):
            termCredit.append(i.sum_credit)
        return termCredit
    # print(get_this_semester_credit())

    def get_cumulative_credit(self):
        allCredit = []
        query = session.query(Gpax)
        for i in query.filter_by(Student_ID="{}".format(self.studenID)):
            allCredit.append(i.sum_all_credit)
        return allCredit
    # print(get_cumulative_credit())

    def get_GPA(self):
        gpa = []
        query = session.query(Gpa)
        for i in query.filter_by(Student_ID="{}".format(self.studenID),Term="{}".format(self.term)):
            gpa.append(i.GPA)
        return gpa
    # print(get_GPA())

    def get_GPAX(self):
        gpax = []
        query = session.query(Gpax)
        for i in query.filter_by(Student_ID="{}".format(self.studenID)):
            gpax.append(i.GPAX)
        return gpax
    # print(get_GPAX())

class Get_name_credit_subject:
    def __init__(self,studenID,term):
        self.studenID = studenID
        self.term = term
    def get_nameSubject(self):

        query = session.query(Subject)
        a = Get_Academic.get_id_subject(self)
        b = []
        for i in a:
            for j in query.filter_by(ID_Subject="{}".format(i)):
                b.append(j.name_subject)
        return b

    def get_credit(self):
        query = session.query(Subject)
        c = Get_Academic.get_id_subject(self)
        d = []
        for i in c:
            for j in query.filter_by(ID_Subject="{}".format(i)):
                d.append(j.Credit)
        return d
    # print(get_credit())

class Academic_1st_table:
    def output_term(self,idsub = None,namesub = None,credit = None,grade = None):
        list_output_term = []
        for i in range(len(idsub)):
            dict_output_term = {"ID Subject":idsub[i],"Name Subject":namesub[i],
             "Credit":credit[i],"Academic Regcord":grade[i]}
            list_output_term.append(dict_output_term)
        return list_output_term

class Academic_2st_table:
    def output_sum(self,this_credit = None,gpa = None,cumulative_credit = None,gpax = None):
        list_sum_output = []
        for i in range(len(cumulative_credit)):
            dict_output_term = {"This semester":this_credit[i],"GPA":gpa[i],
             "Cumulative credit":cumulative_credit[i],"GPAX":gpax[i]}
            list_sum_output.append(dict_output_term)
        return list_sum_output


# studenID = "59340500017"
# term = "1/2559"
#
# s = Get_Academic(studenID,term)
# t = Get_Academic_02(studenID,term)
# o = Academic_1st_table()
#
# print(o.output_term(s.get_id_subject(),t.get_nameSubject(),t.get_credit(),s.get_grade()))
