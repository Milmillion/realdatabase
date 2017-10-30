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
