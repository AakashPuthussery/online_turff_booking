from flask import Flask, render_template, request,redirect,session
import datetime
from Dbconnection import Db
import demjson

app = Flask(__name__)
app.secret_key="abc"

@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route('/logout')
def logout():
    session['lin']=""
    return redirect('/')

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
            session['lin'] = "lo"
            return '''<script>alert('successfully login');window.location="/admin_home"</script>'''
        elif ss['utype']=='prop':
            session['lid']=ss['login_id']
            session['lin'] = "lo"
            return '''<script>alert('successfully login');window.location="/prop_home"</script>'''
        elif ss['utype']=='user':
            session['lid']=ss['login_id']
            session['lin'] = "lo"
            return '''<script>alert('successfully login');window.location="/user_home"</script>'''
        else:
            return '''<script>alert('user not found');window.location="/"</script>'''
    else:
        return '''<script>alert('invalid username and password');window.location="/"</script>'''



@app.route("/admin_home")
def admin_home():
    if session['lin'] == "lo":
        return render_template("ADMIN/admin home.html")
    else:
        return redirect('/')






@app.route("/adm_court_request")
def adm_court_request():
    if session['lin'] == "lo":
        return render_template("admin/court request.html")
    else:
        return redirect('/')


@app.route("/adm_prop_approval")
def adm_prop_approval():
    if session['lin'] == "lo":
        db = Db()
        ss = db.select("select * from prop,login where login.login_id=prop.login_id and login.utype='pending'")
        print(ss)
        return render_template("admin/prop.html",data=ss)
    else:
        return redirect('/')


@app.route("/approve_prop/<p_id>")
def approve_prop(p_id):
    if session['lin'] == "lo":
        db = Db()
        ss = db.update("update login set utype = 'prop' where login_id = '"+p_id+"'")
        print(ss)
        return '''<script>alert('APPROVED');window.location="/adm_prop_approval"</script>'''
    else:
        return redirect('/')


@app.route("/reject_prop/<p_id>")
def reject_prop(p_id):
    if session['lin'] == "lo":
        db = Db()
        ss = db.update("update login set utype = 'rejected' where login_id = '"+p_id+"'")
        print(ss)
        db.delete("delete from prop where prop.login_id='" + p_id + "'")
        return '''<script>alert('REJECTED');window.location="/adm_prop_approval"</script>'''
    else:
        return redirect('/')


@app.route("/adm_viewapprovedprop")
def adm_viewapprovedprop():
    if session['lin'] == "lo":
        db = Db()
        ss = db.select("select * from prop,login where login.login_id=prop.login_id and login.utype!='pending'")
        print(ss)
        return render_template("admin/viewapprovedprop.html", data=ss)
    else:
        return redirect('/')


@app.route("/adm_block_prop/<id>")
def adm_block_prop(id):
    if session['lin'] == "lo":
        db = Db()
        ss = db.update("update login set utype = 'block' where login_id = '" + id + "'")
        return '''<script>alert('BLOCKED');window.location="/adm_viewapprovedprop"</script>'''
    else:
        return redirect('/')


@app.route('/adm_unblock_prop/<id>')
def adm_unblock_prop(id):
    if session['lin'] == "lo":
        db=Db()
        ss=db.update("update login set utype='prop' where login_id='"+id+"'")
        return '''<script>alert("UNBLOCKED");window.location="/adm_viewapprovedprop"</script>'''
    else:
        return redirect('/')


@app.route("/adm_View_users")
def adm_View_users():
    if session['lin'] == "lo":
        db = Db()
        ss = db.select("select * from users")
        print(ss)
        return render_template("admin/View users.html",data = ss)
    else:
        return redirect('/')


@app.route("/view_prop_and_court")
def view_prop_and_court():
    if session['lin'] == "lo":
        db=Db()
        ss=db.select("select * from court,prop where court.prop_id=prop.login_id")
        return render_template("admin/view_court.html", data=ss)
    else:
        return redirect('/')

# @app.route("/adm_delete/<k>")
# def adm_delete(k):
#     db = Db()
#     db.delete("DELETE FROM COURT WHERE court_id='"+str(k)+"'")
#     return '<script>alert("court deleted");window.location="/view_prop_and_court"</script>'



@app.route("/adm_view_rating/<k>")
def adm_view_rating(k):
    if session['lin'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM rating,users WHERE rating.user_id=users.login_id and rating.court_id='"+str(k)+"'")
        print(ss)
        return render_template("admin/view Rating.html", data=ss)
    else:
        return redirect('/')


@app.route("/adm_view_review/<k>")
def adm_view_review(k):
    if session['lin'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM review,users WHERE review.user_id=users.login_id and review.court_id='"+str(k)+"'")
        print(ss)
        return render_template("admin/view Review.html", data=ss)
    else:
        return redirect('/')

# ----------------------------------------------------------------------------------------------------------------------------------------------
#                                         PROP MODULE
# ----------------------------------------------------------------------------------------------------------------------------------------------


@app.route("/prop_home")
def prop_home():
    if session['lin'] == "lo":
        return render_template('Props/Prop home.html')
    else:
        return redirect('/')


@app.route('/prop_register',methods=['get','post'])
def prop_register():
        if request.method=="POST":
            name=request.form['textfield']
            phone=request.form['textfield2']
            image=request.files['fileField']
            date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            image.save(r"D:\turfbookin\static\pic\\" + date + '.jpg')
            ss = '/static/pic/' + date + '.jpg'
            district=request.form['select']
            email=request.form['textfield3']
            password=request.form['textfield4']
            db=Db()
            res=db.insert("insert into login VALUES('','" + email + "','" +password+ "','pending')")
            db.insert("insert into prop VALUES ('"+str(res)+"','"+name+"','"+email+"','"+phone+"','"+str(ss)+"','"+district+"')")
            return '''<script>alert("PROP REGISTERD");window.location="/"</script>'''
        else:
            return render_template('Props/registerpage.html')


@app.route("/pr_addcourt",methods=['get','post'])
def pr_addcourt():
    if session['lin'] == "lo":
        if request.method=="POST":
            court_name=request.form['textfield2']
            place = request.form['textfield3']
            image = request.files['fileField']
            date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            image.save(r"D:\turfbookin\static\pic\\" + date + '.jpg')
            ss = '/static/pic/' + date + '.jpg'
            district = request.form['select']
            phone=request.form['textfield4']
            email = request.form['textfield5']
            latitude = request.form['textfield6']
            longitude = request.form['textfield7']
            fee = request.form['textfield8']
            db=Db()
            db.insert("insert into court VALUES ('','"+court_name+"','"+place+"','"+district+"','"+fee+"','"+str(session['lid'])+"','"+latitude+"','"+longitude+"','"+phone+"','"+email+"','"+str(ss)+"','pending')")
            return '''<script>alert("COURT ADDED");window.location="/prop_home"</script>'''
        else:
            return render_template("Props/Addcourt.html")
    else:
        return redirect('/')


@app.route("/view_court")
def view_court():
    if session['lin'] == "lo":
        db=Db()
        ss=db.select("select court.district as d,court.*,prop.* from court,prop where court.prop_id=prop.login_id and prop.login_id='"+str(session['lid'])+"'")
        return render_template("Props/Viewcourt.html",data=ss)
    else:
        return redirect('/')


@app.route('/update_court/<mid>')
def update_court(mid):
    if session['lin'] == "lo":
        db=Db()
        res=db.selectOne("select * from court where court_id='"+mid+"'")
        return render_template('Props/update_court.html',loop=res,id=mid)
    else:
        return redirect('/')


@app.route('/update_court_action/<mid>',methods=['post'])
def update_court_action(mid):
    if session['lin'] == "lo":
        court_name = request.form['textfield2']
        place = request.form['textfield3']
        image = request.files['fileField']
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        image.save(r"D:\turfbookin\static\pic\\" + date + '.jpg')
        ss = '/static/pic/' + date + '.jpg'
        district = request.form['select']
        phone = request.form['textfield4']
        email = request.form['textfield5']
        fee = request.form['textfield8']
        db=Db()
        if request.files!=None:
            if image.filename!="":
                    db.update("update court set court_name='"+court_name+"',place='"+place+"',district='"+district+"',fee='"+fee+"',contact_no='"+phone+"',email='"+email+"',court_image='"+str(ss)+"' where court_id='"+mid+"'")
                    return '''<script>alert('SUCCESSFULLY UPDATED');window.location="/view_court"</script>'''

            else:
                db.update("update court set court_name='"+court_name+"',place='"+place+"',district='"+district+"',fee='"+fee+"',contact_no='"+phone+"',email='"+email+"' where court_id='"+mid+"'")
                return '''<script>alert('SUCCESSFULLY UPDATED');window.location="/view_court"</script>'''


        else:
            db.update("update court set court_name='"+court_name+"',place='"+place+"',district='"+district+"',fee='"+fee+"',contact_no='"+phone+"',email='"+email+"' where court_id='"+mid+"'")
            return '''<script>alert('SUCCESSFULLY UPDATED');window.location="/view_court"</script>'''
    else:
        return redirect('/')


@app.route('/delete_court/<cid>')
def delete_court(cid):
    if session['lin'] == "lo":
        db = Db()
        db.delete("delete  from court where court_id='" + cid + "'")
        return redirect('/view_court')
    else:
        return redirect('/')



@app.route("/pr_viewrequest_allocation")
def pr_viewrequest_allocation():
    if session['lin'] == "lo":
        db=Db()
        ss=db.select("select * from court_booking,court,users,prop where court_booking.court_id=court.court_id and court_booking.user_id=users.login_id and court.prop_id=prop.login_id and prop.login_id='"+str(session['lid'])+"' and court_booking.status='pending'")
        return render_template("Props/view_courtrequestprop.html", data=ss)
    else:
        return redirect('/')


@app.route("/approve_court_req/<p_id>")
def approve_court_req(p_id):
    if session['lin'] == "lo":
        db = Db()
        ss = db.update("update court_booking set status = 'approved' where booking_id = '"+p_id+"'")
        print(ss)
        return '''<script>alert('APPROVED');window.location="/pr_viewrequest_allocation"</script>'''
    else:
        return redirect('/')


@app.route("/reject_court_req/<p_id>")
def reject_court_req(p_id):
    if session['lin'] == "lo":
        db = Db()
        ss = db.update("update court_booking set status = 'rejected' where booking_id = '"+p_id+"'")
        print(ss)
        return '''<script>alert('REJECTED');window.location="/pr_viewrequest_allocation"</script>'''
    else:
        return redirect('/')


# @app.route("/pr_viewuser")
# def pr_viewuser():
#
#     db=Db()
#     ss=db.select("SELECT * FROM users")
#     return render_template("Props/View users.html.html.html",data=ss)


# @app.route("/pr_viewrating")
# def pr_viewrating():
#
#     db=Db()
#     ss=db.select("SELECT * FROM rating")
#     return render_template("Props/view Rating.html",data=ss)
#
#
# @app.route("/pr_viewreview")
# def pr_viewreview():
#
#     db=Db()
#     ss=db.select("SELECT * FROM review")
#     return render_template("Props/view Review.html",data=ss)
@app.route('/view_members')
def view_members():
    if session['lin'] == "lo":
        db=Db()
        res=db.select("select * from users")
        return render_template('Props/View users.html',data=res)
    else:
        return redirect('/')


@app.route("/view_court_rating_review")
def view_court_rating_review():
    if session['lin'] == "lo":
        db=Db()
        ss=db.select("select * from court,prop where court.prop_id=prop.login_id and prop.login_id='"+str(session['lid'])+"'")
        return render_template("Props/View_court_rating_review.html",data=ss)
    else:
        return redirect('/')


@app.route("/prop_view_rating/<a>")
def prop_view_rating(a):
    if session['lin'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM rating,users,court,prop WHERE rating.user_id=users.login_id and rating.court_id=court.court_id and court.prop_id=prop.login_id and rating.court_id='"+str(a)+"' and prop.login_id='"+str(session['lid'])+"' ")
        print(ss)
        return render_template("Props/view Rating.html", data=ss)
    else:
        return redirect('/')


@app.route("/prop_view_review/<b>")
def prop_view_review(b):
    if session['lin'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM review,users,court,prop WHERE review.user_id=users.login_id and review.court_id=court.court_id and court.prop_id=prop.login_id and review.court_id='"+str(b)+"' and prop.login_id='"+str(session['lid'])+"' ")
        print(ss)
        return render_template("Props/view Review.html", data=ss)
    else:
        return redirect('/')


# @app.route("/pr_addtournament")
# def pr_addtournament():
#     if request.method=="POST":
#
#     db=Db()
#     ss=db.select("SELECT * FROM tournament")
#     return render_template("Props/Add_Tournament.html", data=ss)



@app.route("/pr_addtournament",methods=['get','post'])
def pr_addtournament():
    if session['lin'] == "lo":
        if request.method=="POST":
            court_name=request.form['select']
            tournament_name=request.form['textfield3']
            no_of_team = request.form['textfield4']
            start_date = request.form['textfield5']
            entry_fee = request.form['textfield6']
            winning_price=request.form['textfield7']
            dead_line = request.form['textfield8']
            maximum_teams = request.form['textfield9']
            db=Db()
            db.insert("insert into tournament VALUES ('','"+tournament_name+"','"+court_name+"','"+no_of_team+"','"+start_date+"','"+entry_fee+"','"+winning_price+"','"+dead_line+"','"+maximum_teams+"')")
            return '''<script>alert("TOURNAMENT ADDED");window.location="/prop_home"</script>'''
        else:
            db=Db()
            res=db.select("select * from court,prop where court.prop_id=prop.login_id and prop.login_id='"+str(session['lid'])+"'")
            print(res)
            return render_template("Props/Add_Tournament.html",data=res)
    else:
        return redirect('/')


@app.route('/prop_view_tournament')
def prop_view_tournament():
    if session['lin'] == "lo":
        db=Db()
        res=db.select("select * from tournament,court where tournament.court_id=court.court_id AND court.prop_id='"+str(session['lid'])+"'")
        return render_template('Props/view_tournament.html',data=res)
    else:
        return redirect('/')


@app.route("/update_tournament/<tid>",methods=['get','post'])
def update_tournament(tid):
    if session['lin'] == "lo":
        if request.method=="POST":
            court_name=request.form['select']
            tournament_name=request.form['textfield3']
            no_of_team = request.form['textfield4']
            start_date = request.form['textfield5']
            entry_fee = request.form['textfield6']
            winning_price=request.form['textfield7']
            dead_line = request.form['textfield8']
            maximum_teams = request.form['textfield9']
            db=Db()
            db.update("update tournament set tournament_name= '"+tournament_name+"',court_id='"+court_name+"',no_of_teams='"+no_of_team+"',start_date='"+start_date+"',entry_fee='"+entry_fee+"',winning_prize='"+winning_price+"',deadline='"+dead_line+"',maximum_teams='"+maximum_teams+"' where tournament_id='"+tid+"' ")
            return '''<script>alert("TOURNAMENT UPDATED");window.location="/prop_view_tournament"</script>'''
        else:
            db=Db()
            res=db.select("select * from court,prop where court.prop_id=prop.login_id and prop.login_id='"+str(session['lid'])+"'")
            ss=db.selectOne("select * from tournament,court where tournament.court_id=court.court_id and tournament_id='"+tid+"'")
            print("h",ss)
            print("kkkkk",res)
            print(tid)
            return render_template("Props/UpdateTournament.html",data=res,l=ss)
    else:
        return redirect('/')


@app.route('/delete_tournament/<tid>')
def delete_tournament(tid):
    if session['lin'] == "lo":
        db=Db()
        db.delete("delete from tournament where tournament_id='"+tid+"'")
        return redirect('/prop_view_tournament')
    else:
        return redirect('/')


@app.route("/pr_addschedule/<aa>",methods=['get','post'])
def pr_addschedule(aa):
    if session['lin'] == "lo":
        if request.method=="POST":
            game_type=request.form['select']
            date=request.form['textfield']
            time = request.form['textfield2']
            duration = request.form['textfield4']
            team1 = request.form['select2']
            team2 = request.form['select3']
            breaks = request.form['textfield3']
            db=Db()
            db.insert("insert into tournament_schedule VALUES ('','"+str(aa)+"','"+game_type+"','"+date+"','"+time+"','"+duration+"','"+team1+"','"+team2+"','"+breaks+"','')")
            return '''<script>alert("TIME SHEDULED");window.location="/prop_home"</script>'''
        else:
            db=Db()
            res=db.select("select * from tournament,court,prop where tournament.court_id=court.court_id and court.prop_id=prop.login_id and prop.login_id='"+str(session['lid'])+"'")
            return render_template("Props/Addschedule.html",data=res)
    else:
        return redirect('/')


@app.route("/pr_viewschedule/<aa>")
def pr_viewschedule(aa):
    if session['lin'] == "lo":
        db=Db()
        ss=db.select("select * from tournament_schedule where tournament_schedule.tournament_id='"+str(aa)+"'")
        return render_template("props/viewtournamentshedule.html",data=ss)
    else:
        return redirect('/')


@app.route('/delete_schedule/<sid>')
def delete_schedule(sid):
    if session['lin'] == "lo":
        db=Db()
        db.delete("delete from tournament_schedule where tournament_schedule_id='"+sid+"'")
        return redirect('/prop_view_tournament')
    else:
        return redirect('/')


@app.route("/update_schedule/<sid>",methods=['get','post'])
def update_schedule(sid):
    if session['lin'] == "lo":
        if request.method=="POST":
            game_type = request.form['select']
            date = request.form['textfield']
            time = request.form['textfield2']
            duration = request.form['textfield4']
            team1 = request.form['select2']
            team2 = request.form['select3']
            breaks = request.form['textfield3']
            db=Db()
            db.update("update tournament_schedule set game_type= '"+game_type+"',match_date='"+date+"',match_time='"+time+"',duration='"+duration+"',team1='"+team1+"',team2='"+team2+"',break='"+breaks+"' where tournament_schedule_id='"+sid+"'  ")
            return '''<script>alert("TOURNAMENT UPDATED");window.location="/prop_view_tournament"</script>'''
        else:
            db=Db()
            res=db.select("select * from tournament_request,tournament,users where tournament_request.tournament_id=tournament.tournament_id and tournament_request.user_id=users.login_id and tournament_request.status='approved'")
            ss=db.selectOne("select * from tournament_schedule,tournament,court,prop where tournament_schedule.tournament_id=tournament.tournament_id and tournament.court_id=court.court_id and court.prop_id=prop.login_id and prop.login_id='"+str(session['lid'])+"' and tournament_schedule_id='"+sid+"'")
            print("kjhgf"+str(ss))
            print("ffff"+str(res))

            print("okok",str(session['lid']))
            if len(res)>0 :
                return render_template("Props/Upadateschedule.html",data=res,aa=ss)
            else:
                res1 = db.select("select * from tournament_request,tournament,users where tournament_request.tournament_id=tournament.tournament_id and tournament_request.user_id=users.login_id and tournament_request.status='pending'")
                ss = db.selectOne("select * from tournament_schedule,tournament,court,prop where tournament_schedule.tournament_id=tournament.tournament_id and tournament.court_id=court.court_id and court.prop_id=prop.login_id and prop.login_id='" + str(session['lid']) + "'  ")

                return render_template("Props/Upadateschedule.html",data1=res1,aa=ss)
    else:
        return redirect('/')


@app.route('/add_winners/<tid>/<tsid>/<t1>/<t2>/<g>',methods=['get','post'])
def add_winners(tid,tsid,t1,t2,g):
    if session['lin'] == "lo":
        if request.method=="POST":
            round1winner=request.form['RadioGroup1']
            db=Db()
            if g=='Semi Finals':
                db.update("update tournament_schedule set winner='"+round1winner+"' where tournament_schedule_id='"+tsid+"' ")
            else:
                db.update("update tournament_schedule set winner='" + round1winner + "' where tournament_schedule_id='" + tsid + "' ")
                res=db.insert("insert into winners_list VALUES ('','"+str(tid)+"','"+round1winner+"')")
                print(tid)
            return '''<script>alert("WINNERS LIST ADDED");window.location="/prop_home"</script>'''
        else:
            return render_template('Props/Add__winners.html',t1=t1,t2=t2)
    else:
        return redirect('/')



@app.route("/pr_tournamentrequest")
def pr_tournamentrequest():
    if session['lin'] == "lo":
        db=Db()
        ss=db.select("select * from tournament_request,tournament,users,court,prop where tournament_request.tournament_id=tournament.tournament_id and tournament_request.user_id=users.login_id and tournament.court_id=court.court_id and tournament_request.status='pending' and court.prop_id=prop.login_id and prop.login_id='"+str(session['lid'])+"'")
        return render_template("Props/ViewTournmentRequest.html",data=ss)
    else:
        return redirect('/')


@app.route("/approve_tournament_req/<rid>")
def approve_tournament_req(rid):
    if session['lin'] == "lo":
        db = Db()
        ss = db.update("update tournament_request set status = 'approved' where tournament_req_id = '"+rid+"'")
        print(ss)
        return '''<script>alert('APPROVED');window.location="/pr_tournamentrequest"</script>'''
    else:
        return redirect('/')


@app.route("/reject_tournament_req/<trid>")
def reject_tournament_req(trid):
    if session['lin'] == "lo":
        db = Db()
        ss = db.update("update tournament_request set status = 'rejected' where tournament_req_id = '"+trid+"'")
        print(ss)
        # db.delete("delete from prop where prop.login_id='" + p_id + "'")
        return '''<script>alert('REJECTED');window.location="/pr_tournamentrequest"</script>'''
    else:
        return redirect('/')





@app.route("/pr_viewwinnerslist")
def pr_viewwinnerslist():
    if session['lin'] == "lo":
        db=Db()
        ss=db.select("select * from winners_list,tournament,court,prop where winners_list.tournament_id=tournament.tournament_id and tournament.court_id=court.court_id and court.prop_id=prop.login_id and prop.login_id='"+str(session['lid'])+"'")

        return render_template("props/view_winnerslist.html", data=ss)
    else:
        return redirect('/')


@app.route('/delete_winner_list/<wid>')
def delete_winner_list(wid):
    if session['lin'] == "lo":
        db=Db()
        db.delete("delete from winners_list where winner_id='"+wid+"'")
        return redirect('/pr_viewwinnerslist')
    else:
        return redirect('/')




############################################################################

@app.route('/and_login',methods=['post'])
def and_login():
    print("hi")
    username=request.form['u']
    password=request.form['p']
    db=Db()
    ss=db.selectOne("select * from login where username='"+username+"' and password='"+password+"'")
    print(ss)
    res={}
    if ss:
        res['status']="ok"
        res['lid']=ss['login_id']
        res['type']=ss['utype']
        return demjson.encode(res)
    else:
        res['status']=""
        return demjson.encode(res)
@app.route('/and_public_view_court',methods=['post'])
def and_public_view_court():
    db=Db()
    ss=db.select("select * from rating,court where rating.court_id=court.court_id")
    res = {}
    if ss:
        res['status'] = "ok"
        res['data'] = ss
        return demjson.encode(res)
    else:
        res['status'] = ""
        return demjson.encode(res)


@app.route('/and_public_view_review',methods=['post'])
def and_public_view_review():
    cid=request.form['c']
    db=Db()
    ss=db.select("select * from review,users where review.user_id=users.login_id and review.court_id='"+cid+"'")
    res = {}
    if ss:
        res['status'] = "ok"
        res['data'] = ss
        return demjson.encode(res)
    else:
        res['status'] = ""
        return demjson.encode(res)

@app.route('/and_add_review',methods=['post'])
def and_add_review():
    id=request['id']
    r=request['r']
    c=request['cid']
    db=Db()
    ss=db.insert("insert into review VALUE ('','"+id+"','"+r+"',curdate(),'"+c+"') ")
    res = {}
    if ss:
        res['status'] = "ok"
        return demjson.encode(res)
    else:
        res['status'] = ""
        return demjson.encode(res)


@app.route('/and_add_rating',methods=['post'])
def and_add_rating():
    id=request['id']
    r=request['r']
    c=request['cid']
    db=Db()
    ss=db.insert("insert into rating VALUE ('','"+id+"','"+r+"',curdate(),'"+c+"') ")
    res = {}
    if ss:
        res['status'] = "ok"
        return demjson.encode(res)
    else:
        res['status'] = ""
        return demjson.encode(res)
@app.route('/and_tournament_req',methods=['post'])
def and_tournament_req():
    id=request['id']
    r=request['r']
    c=request['cid']
    db=Db()
    ss=db.insert("insert into tournament_request VALUE ('','"+id+"','"+r+"',curdate(),'"+c+"') ")
    res = {}
    if ss:
        res['status'] = "ok"
        return demjson.encode(res)
    else:
        res['status'] = ""
        return demjson.encode(res)

@app.route('/and_search_court',methods=['post'])
def and_search_court():
    db=Db()
    ss=db.select("select * from rating,court where rating.court_id=court.court_id")
    res = {}
    if ss:
        res['status'] = "ok"
        res['data'] = ss
        return demjson.encode(res)
    else:
        res['status'] = ""
        return demjson.encode(res)

@app.route('/and_view_tournament',methods=['post'])
def and_view_tournament():
    db=Db()
    ss=db.select("select * from tournament,court where tournament.court_id=court.court_id")
    print(ss)
    res = {}
    if ss:
        res['status'] = "ok"
        res['data'] = ss
        return demjson.encode(res)
    else:
        res['status'] = ""
        return demjson.encode(res)




if __name__ == '__main__':
    app.run(port=4000,host="0.0.0.0")
