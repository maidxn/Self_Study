import yate
import cgi
import athletemodel

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value
print(yate.start_response())
print(yate.include_header("Coach Kelly Timing Data"))
all_athletes = athletemodel.get_from_store()
print(yate.include_header("Athlete: " + athlete_name + " DOB: " + all_athletes[athlete_name].dob))
print(yate.para("Top 3:"))
print(yate.u_list(all_athletes[athlete_name].top3))
print(yate.include_footer({"Home": "/index.html", 'Select another athlete': "/cgi-bin/generate_list.py"}))
