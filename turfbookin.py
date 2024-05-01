import datetime
from flask import Flask, render_template, request,redirect,session
from Dbconnection import Db

app = Flask(__name__)
app.secret_key="abc"

@app.route('/')
def hello_world():
    return render_template("login.html")


@app.route("/login_post", methods=['post'])
def login_post():
    username=request.form['textfield']
    password=request.form['textfield2']
    print(username,password)
    db=Db()
    ss=db.selectOne("select * from login where username='"+username+"' and password='"+password+"'")
    print(ss)
    if ss is not None:
        if ss['utype']=='admin':
            return '''<script>alert('successfully login');window.location="/adm_admin_home"</script>'''
        elif ss['utype']=='prop':
            session['lid']=ss['login_id']
            return '''<script>alert('successfully login');window.location="/pr_prop_home"</script>'''


        else:
            return '''<script>alert('user not found');window.location="/"</script>'''
    else:
        return '''<script>alert('invalid username and password');window.location="/"</script>'''



@app.route("/adm_admin_home")
def adm_admin_home():
    return render_template("admin/admin home.html")





@app.route("/adm_court_block")
def adm_court_block():
    return render_template("admin/court block.html")

@app.route("/adm_court_request")
def adm_court_request():
    return render_template("admin/court request.html")

@app.route("/adm_court")
def adm_court():

    db=Db()
    ss=db.select("select * from court,prop where court.prop_id=prop.prop_id")
    return render_template("admin/Court.html",data=ss)

@app.route("/adm_prop_approval")
def adm_prop_approval():
    db = Db()
    ss = db.select("select * from prop,login where login.login_id=prop.prop_id and login.utype='pending'")
    print(ss)
    return render_template("admin/prop.html",data=ss)




@app.route("/approve_prop/<p_id>")
def approve_prop(p_id):
    db = Db()
    ss = db.update("update login set utype = 'prop' where login_id = '"+p_id+"'")
    print(ss)
    return '''<script>alert('approved');window.location="/adm_prop_approval"</script>'''




@app.route("/reject_prop/<p_id>")
def reject_prop(p_id):
    db = Db()
    ss = db.update("update login set utype = 'rejected' where login_id = '"+p_id+"'")
    print(ss)
    return '''<script>alert('rejected');window.location="/adm_prop_approval"</script>'''


@app.route("/adm_viewapprovedprop")
def adm_viewapprovedprop():
    db = Db()
    ss = db.select("select * from prop,login where login.login_id=prop.prop_id and login.utype='prop'")
    print(ss)
    return render_template("admin/viewapprovedprop.html", data=ss)

@app.route("/adm_delete/<k>")
def adm_delete(k):
    db = Db()
    db.delete("DELETE FROM COURT WHERE court_id='"+str(k)+"'")
    return '<script>alert("court deleted");window.location="/adm_court"</script>'


@app.route("/adm_View_users")
def adm_View_users():
    db = Db()
    ss = db.select("select * from users")
    print(ss)
    return render_template("admin/View users.html",data = ss)


@app.route("/adm_view_rating/<k>")
def adm_view_rating(k):
    db = Db()
    ss = db.select("SELECT * FROM rating,users WHERE rating.user_id=users.user_id and court_name='"+str(k)+"'")
    print(ss)
    return render_template("admin/view Rating.html", data=ss)


@app.route("/adm_view_review/<k>")
def adm_view_review(k):
    db = Db()
    ss = db.select("SELECT * FROM review,users WHERE review.user_id=users.user_id and court_id='"+str(k)+"'")
    print(ss)
    return render_template("admin/view Review.html", data=ss)


# ----------------------------------------------------------------------------------------------------------------------------------------------
#                                         PROP MODULE
# ----------------------------------------------------------------------------------------------------------------------------------------------


@app.route("/pr_prop_home")
def pr_prop_home():
    return render_template('Props/Prop home.html')

@app.route('/prop_reg',methods=['get','post'])
def prop_reg():
    if request.method=="POST":
        db=Db()
        name=request.form['textfield']
        Phoneno=request.form['textfield2']
        photo=request.files['fileField']
        date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(r"F:\turfbookin project\turfbookin\static\prop_img\\"+date+".jpg")
        path="/static/prop_img/"+date+".jpg"
        district=request.form['select']
        email=request.form['textfield3']
        password=request.form['textfield4']
        confirmpassword=request.form['textfield8']
        res=db.insert("insert into login values('','"+email+"','"+confirmpassword+"','pending')")
        db.insert("insert into prop VALUES ('"+str(res)+"','"+name+"','"+email+"','"+Phoneno+"','"+path+"','"+district+"')")
        return '''<script>alert('Successfully Registerd');window.location="/"</script>'''

    else:
        return render_template("Props/registerpage.html")



@app.route("/pr_courtmanagement")
def pr_courtmanagement():
    db=Db()
    ss=db.select("SELECT * FROM court where prop_id='"+str(session['lid'])+"'")
    print(session['lid'])
    print (ss)
    return render_template("Props/Viewcourt.html",data=ss)

@app.route("/pr_updatecourt/<id>", methods=['get', 'post'])
def pr_updatecourt(id):
        if request.method == "POST":
            db = Db()
            courtname = request.form['textfield2']
            place = request.form['textfield3']
            courtimage = request.files['fileField']
            contactnumber = request.form['textfield4']
            date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            courtimage.save(r"F:\turfbookin project\turfbookin\static\photos\\" + date + ".jpg")
            path = "static/photos/" + date + ".jpg"
            district = request.form['select1']
            status = request.form['select']
            email = request.form['textfield5']
            latitude = request.form['textfield6']
            longitude = request.form['textfield7']
            fee = request.form['textfield8']
            if request.files != None:
                if courtimage.filename != "":
                    db.update(
                        "update court set court_name='" + courtname + "',place='" + place + "',district='" + district + "',fee='" + fee + "',prop_id='" + str(
                            session[
                                'lid']) + "',status='" + status + "',latitude='" + latitude + "',longtitude='" + longitude + "',contact_no='" + contactnumber + "',email='" + email + "',court_image='" + str(
                            path) + "' where court_id='" + str(id) + "'")
                    return '''<script>alert('Successfully court updated');window.location="/pr_courtmanagement"</script>'''

                else:
                    db.update(
                        "update court set court_name='" + courtname + "',place='" + place + "',district='" + district + "',fee='" + fee + "',prop_id='" + str(
                            session[
                                'lid']) + "',status='" + status + "',latitude='" + latitude + "',longtitude='" + longitude + "',contact_no='" + contactnumber + "',email='" + email + "' where court_id='" + str(
                            id) + "'")

                    return '''<script>alert('Successfully court updated');window.location="/pr_courtmanagement"</script>'''
            else:
                db.update(
                    "update court set court_name='" + courtname + "',place='" + place + "',district='" + district + "',fee='" + fee + "',prop_id='" + str(
                        session[
                            'lid']) + "',status='" + status + "',latitude='" + latitude + "',longtitude='" + longitude + "',contact_no='" + contactnumber + "',email='" + email + "' where court_id='" + str(
                        id) + "'")

                return '''<script>alert('Successfully court updated');window.location="/pr_courtmanagement"</script>'''

        else:
            db = Db()
            ss = db.selectOne("SELECT * FROM court WHERE court_id= '"+id+"'")
            return render_template("Props/updatecourt.html",data=ss)


@app.route("/pr_addcourt",methods=['get','post'])
def pr_addcourt():
    if request.method == "POST":
        db = Db()
        courtname = request.form['textfield2']
        place = request.form['textfield3']
        courtimage= request.files['fileField']
        contactnumber = request.form['textfield4']
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        courtimage.save(r"D:\New folder (2)\turfbookin\static\photos/" + date + ".jpg")
        path = "static/photos/" + date + ".jpg"
        district = request.form['select1']
        status = request.form['select']
        email = request.form['textfield5']
        latitude= request.form['textfield6']
        longitude = request.form['textfield7']
        fee = request.form['textfield8']

        db.insert("insert into court VALUES ('','" + courtname + "','" + place + "','" + district +"','" + fee + "','" + str(session['lid']) + "','" + status + "','" + latitude +"','" + longitude + "','" + contactnumber +"','" + email +"','" + str(path) +"')")
        return '''<script>alert('Successfully court added');window.location="/pr_prop_home"</script>'''

    else:

        return render_template("Props/Addcourt.html")



@app.route("/pr_CreateTournament",methods=['get','post'])
def pr_CreateTournament():
    if request.method == "POST":
        db = Db()

        tournamentname = request.form['textfield2']
        courtname = request.form['select']
        noofteams = request.form['textfield4']
        startdate = request.form['textfield5']
        entryfee = request.form['textfield6']
        winningprize = request.form['textfield7']
        deadline= request.form['textfield8']
        limit = request.form['textfield9']
        db.insert("insert into tournament VALUES ('','" + tournamentname + "','" + courtname + "','" + str(session['lid']) + "','" + noofteams +"','" + startdate + "','" + entryfee + "','" + winningprize + "','" + deadline +"','" + limit + "')")
        return '''<script>alert('Successfully Tournament Created');window.location="/pr_prop_home"</script>'''
    else:
        db=Db()
        pid = session['lid']
        res=db.select("select * from court where prop_id='"+ str(pid) +"'")
        return render_template("Props/CreateTournament.html",data=res)




@app.route("/pr_UpdateTournament/<d>",methods=['get','post'])
def  pr_UpdateTournament(d):
    if request.method == "POST":
        db = Db()
        tournamentname = request.form['textfield3']
        courtname = request.form['select']
        noofteams = request.form['textfield4']
        startdate = request.form['textfield5']
        entryfee = request.form['textfield6']
        winningprize = request.form['textfield7']
        deadline1= request.form['textfield8']
        limit2 = request.form['textfield9']
        db.update("update tournament set tournament_name='"+tournamentname+"',court_id='"+courtname+"',no_of_teams='"+noofteams+"',start_date='"+startdate+"',entry_fee='"+entryfee+"',winning_prize='"+winningprize+"',deadline='"+deadline1+"',limit1='"+limit2+"' WHERE tournament_id='"+str(d)+"' ")
        return '''<script>alert('Successfully Updated');window.location="/pr_prop_home"</script>'''

    else:
        db = Db()
        ss = db.selectOne("SELECT * FROM tournament,court where tournament.court_id=court.court_id and court.prop_id='" + str(session['lid'])+ "'AND tournament_id= '" + d + "'")
        sk=db.select("select * from court ")

        return render_template("Props/UpdateTournament.html", data=ss,loop1=sk)




@app.route("/pr_viewrequest_allocation")
def pr_viewrequest_allocation():

    db=Db()
    ss=db.select("SELECT * FROM court request")
    return render_template("Props/Courtrequestprop.html",data=ss)


@app.route("/pr_deletecourt/<id>")
def pr_deletecourt(id):

    db = Db()
    ss = db.delete("delete from court where court_id= '"+id+"'")
    return render_template("Props/Viewcourt.html", data=ss)
    return '''<script>alert('Successfully court deleted');window.location="/pr_courtmanagement"</script>'''




@app.route("/pr_viewuser")
def pr_viewuser():

    db=Db()
    ss=db.select("SELECT * FROM users")
    return render_template("Props/View users.html",data=ss)

@app.route("/pr_viewrating")
def pr_viewrating():
    db=Db()
    ss=db.select("SELECT * FROM rating,users where rating.user_id=users.user_id")
    return render_template("Props/view Rating.html",data=ss)


@app.route("/pr_viewreview")
def pr_viewreview():
    db=Db()
    ss=db.select("SELECT * FROM review,users where review.user_id=users.user_id")
    return render_template("Props/view Review.html",data=ss)



@app.route("/pr_tournamentrequest")
def pr_tournamentrequest():

    db=Db()
    ss=db.select("SELECT * FROM tournament")
    return render_template("Props/ViewTournmentRequest.html",data=ss)

@app.route("/pr_tournamentview")
def pr_tournamentview():

    db=Db()
    ss=db.select("SELECT * FROM tournament,court WHERE tournament.court_id=court.court_id and court.prop_id='"+ str(session['lid']) +"'")
    return render_template("props/tournamentview.html",data=ss)

@app.route("/pr_delete/<g>")
def pr_delete(g):
    db = Db()
    ss = db.delete("delete from tournament where tournament_id='"+g+"'")
    return redirect('/pr_tournamentview')



@app.route("/pr_addschedule",methods=['get','post'])
def pr_addschedule():
    db = Db()
    if request.method == "POST":
        tournamentname = request.form['select']
        teamname = request.form['select1']
        matchdate = request.form['textfield3']
        matchtime = request.form['textfield4']
        db.insert("insert into tournament_schedule VALUES ('','" + tournamentname + "','" + teamname + "','" + matchdate + "','" + matchtime +"')")
        return '''<script>alert('Successfully sheduled');window.location="/pr_addschedule"</script>'''
    else:
        ss=db.select("select * from tournament,court where tournament.court_id=court.court_id and court.prop_id='"+str(session['lid'])+"'")
        print(ss)
        qry=db.select("select * from tournament,tournament_request,court where tournament_request.tournament_id=tournament.tournament_id and tournament.court_id=court.court_id and court.prop_id='"+str(session['lid'])+"'")
        return render_template("Props/Addschedule.html",data1=ss,data=qry)


@app.route("/pr_viewschedule")
def pr_viewschedule():

    db=Db()
    ss=db.select("SELECT * FROM tournament_schedule,tournament where tournament_schedule.tournament_id=tournament.tournament_id group by tournament.tournament_name")
    return render_template("props/viewtournamentshedule.html",data=ss)

@app.route("/pr_deleteschedule/<k>")
def pr_deleteschedule(k):
    db = Db()
    ss = db.delete("delete from tournament_schedule where tournament_schedule_id='"+k+"'")
    return redirect('/pr_viewschedule')




@app.route('/view_team/<b>')
def view_team(b):
    db=Db()
    ss=db.select("select * from tournament_schedule,tournament where tournament_schedule.tournament_id=tournament.tournament_id and tournament.tournament_id='"+b+"'")
    return render_template('props/view_team.html',data=ss)
    # db.Delete()

@app.route("/pr_addwinnerslist",methods=['get','post'])
def pr_addwinnerslist():
    db=Db()
    if request.method == "POST":
        tournamentname = request.form['select']
        round1winners = request.form['textfield2']
        round2winners = request.form['textfield3']
        champions = request.form['textfield4']
        db.insert("insert into winners_list VALUES ('','"+tournamentname+"','" + round1winners + "','" + round2winners + "','" + champions + "')")
        return '''<script>alert('Successfully Added');window.location="/pr_prop_home"</script>'''
    else:
        ss=db.select("SELECT * FROM winners_list")
        qry=db.select("select * from tournament,court,prop where tournament.court_id=court.court_id and court.prop_id=prop.prop_id and prop.prop_id='"+str(session['lid'])+"'")
        return render_template("props/Addwinnerslist.html",data=ss,data1=qry)

@app.route("/pr_viewwinnerslist")
def pr_viewwinnerslist():

    db=Db()
    ss=db.select("select * from winners_list,tournament where winners_list.tournament_id=tournament.tournament_id")
    return render_template("props/Winnerslist.html",data=ss)


@app.route("/pr_deletewinnerslist/<w>")
def pr_deletewinnerslist(w):
    db = Db()
    ss = db.delete("delete from winners_list where winner_id='"+w+"'")
    return redirect('/pr_viewwinnerslist')


if __name__ == '__main__':
    app.run(port=3000)
