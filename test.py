from getAcademic import Get_Academic,Get_name_credit_subject,Academic_1st_table,Academic_2st_table
studenID = "59340500021"
term = "1/2559"

s = Get_Academic(studenID,term)
t = Get_name_credit_subject(studenID,term)
o = Academic_1st_table()
p = Academic_2st_table()

print(o.output_term(s.get_id_subject(),t.get_nameSubject(),t.get_credit(),s.get_grade()))
print(p.output_sum(s.get_this_semester_credit(),s.get_GPA(),s.get_cumulative_credit(),s.get_GPAX()))
