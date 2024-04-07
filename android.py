
from flask import Flask, render_template, request,redirect,session
import datetime
from Dbconnection import Db
import demjson

app = Flask(__name__)
app.secret_key="abc"





@app.route('/user_home')
def user_home():
    if session['lin'] == "lo":
        return render_template('USER/User_home.html')
    else:
        return redirect('/')


@app.route('/user_register',methods=['get','post'])
def user_register():
    if request.method=="POST":
        name=request.form['textfield']
        phone=request.form['textfield2']
        email = request.form['textfield3']
        place = request.form['textfield5']
        image=request.files['fileField']
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        image.save(r"C:\Users\HP\Downloads\turfbookin\static\pic\\" + date + '.jpg')
        ss = '/static/pic/' + date + '.jpg'
        pin = request.form['textfield6']
        district=request.form['select']
        password=request.form['textfield4']
        db=Db()
        res=db.insert("insert into login VALUES('','" + email + "','" +password+ "','user')")
        db.insert("insert into users VALUES ('"+str(res)+"','"+name+"','"+phone+"','"+email+"','"+place+"','"+str(ss)+"','"+pin+"','"+district+"')")
        return '''<script>alert("USER REGISTERD");window.location="/"</script>'''
    else:
        return render_template('USER/user_register.html')


@app.route('/update_user_profile',methods=['get','post'])
def update_user_profile():
    if session['lin'] == "lo":
        if request.method=="POST":
            name=request.form['textfield']
            phone=request.form['textfield2']
            email = request.form['textfield3']
            place = request.form['textfield5']
            image=request.files['fileField']
            date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            image.save(r"C:\Users\HP\Downloads\turfbookin\static\pic\\" + date + '.jpg')
            ss = '/static/pic/' + date + '.jpg'
            pin = request.form['textfield6']
            district=request.form['select']
            db=Db()
            if request.files!=None:
                if image.filename!="":
                        db.update("update users set user_name='"+name+"',phone_no='"+phone+"',email='"+email+"',place='"+place+"',profile_pic='"+str(ss)+"',pin='"+pin+"',district='"+district+"' where users.login_id='"+str(session['lid'])+"'" )
                        return '''<script>alert('SUCCESSFULLY UPDATED');window.location="/update_user_profile"</script>'''

                else:
                    db.update("update users set user_name='"+name+"',phone_no='"+phone+"',email='"+email+"',place='"+place+"',pin='"+pin+"',district='"+district+"' where users.login_id='"+str(session['lid'])+"' " )
                    return '''<script>alert('SUCCESSFULLY UPDATED');window.location="/update_user_profile"</script>'''


            else:
                db.update("update users set user_name='"+name+"',phone_no='"+phone+"',email='"+email+"',place='"+place+"',pin='"+pin+"',district='"+district+"' where users.login_id='"+str(session['lid'])+"' ")
                return '''<script>alert('SUCCESSFULLY UPDATED');window.location="/update_user_profile"</script>'''
        else:
            db=Db()
            res=db.selectOne("select * from users,login where users.login_id='"+str(session['lid'])+"'")
            return render_template('USER/update_profile.html',loop=res)
    else:
        return redirect('/')


@app.route('/user_view_court')
def user_view_court():
    if session['lin'] == "lo":
        db=Db()
        res=db.select("select court.email as e,court.*,prop.*  from court,prop where court.prop_id=prop.login_id")
        return render_template('USER/view_court.html',data=res)
    else:
        return redirect('/')


@app.route('/book_court/<aa>',methods=['get','post'])
def book_court(aa):
    if session['lin'] == "lo":
        if request.method=="POST":
            date=request.form['textfield4']
            start_time=request.form['textfield2']
            end_time=request.form['textfield3']
            db=Db()
            db.insert("insert into court_booking VALUES ('','"+str(aa)+"','"+date+"','"+start_time+"','"+end_time+"','"+str(session['lid'])+"','pending')")
            return "ok"
        else:
            return render_template('USER/book_court.html')
    else:
        return redirect('/')


@app.route('/view_status')
def view_status():
    if session['lin'] == "lo":
        db=Db()
        res=db.select("select court_booking.status as s,court_booking.*,court.*,users.* from court_booking,court,users where court_booking.court_id=court.court_id and court_booking.user_id=users.login_id and users.login_id='"+str(session['lid'])+"' ")
        return render_template('USER/view_status.html',data=res)
    else:
        return redirect('/')


@app.route('/view_recent_booking')
def view_recent_booking():
    if session['lin'] == "lo":
        db=Db()
        res=db.select("select * from court_booking,court,users where court_booking.court_id=court.court_id and court_booking.user_id=users.login_id and users.login_id='"+str(session['lid'])+"'")
        return render_template('USER/View_recent_booking.html',data=res)
    else:
        return redirect('/')


@app.route('/view_recent_tournament')
def view_recent_tournament():
    if session['lin'] == "lo":
        db=Db()
        res=db.select("select * from tournament,court where tournament.court_id=court.court_id")
        return render_template('USER/View_recent_tournament.html',data=res)
    else:
        return redirect('/')


@app.route('/send_tournament_req',methods=['get','post'])
def send_tournament_req():
    if session['lin'] == "lo":
        if request.method=="POST":
            tournament_name=request.form['select']
            team_name=request.form['textfield']
            logo=request.files['fileField']
            date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            logo.save(r"C:\Users\HP\Downloads\turfbookin\static\pic\\" + date + '.jpg')
            ss = '/static/pic/' + date + '.jpg'
            db=Db()
            db.insert("insert into tournament_request VALUES ('','"+tournament_name+"','"+str(session['lid'])+"','"+team_name+"','"+str(ss)+"','pending',curdate())")
            return "ok"
        else:
            db=Db()
            res=db.select("select * from tournament ")
            return render_template('USER/send_tournament_request.html',data=res)
    else:
        return redirect('/')


@app.route('/view_tournament_schedule')
def view_tournament_schedule():
    if session['lin'] == "lo":
        db=Db()
        res=db.select("select * from tournament_schedule,tournament,court where tournament_schedule.tournament_id=tournament.tournament_id and tournament.court_id=court.court_id")
        return render_template('USER/view_tournament_shedule.html',data=res)
    else:
        return redirect('/')

@app.route('/view_winner_list')
def view_winner_list():
    if session['lin'] == "lo":
        db=Db()
        res=db.select("select * from winners_list,tournament,court where winners_list.tournament_id=tournament.tournament_id and tournament.court_id=court.court_id")
        return render_template('USER/view_winnerslist.html',data=res)
    else:
        return redirect('/')


@app.route('/add_rating',methods=['get','post'])
def add_rating():
    if session['lin'] == "lo":
        if request.method=="POST":
            court_name=request.form['select']
            rating=request.form['textfield']
            db=Db()
            db.insert("insert into rating VALUES ('','"+str(session['lid'])+"','"+rating+"','"+court_name+"',curdate())")
            return '''<script>alert("RATING ADDED");window.location="/user_home"</script>'''
        else:
            db=Db()
            res=db.select("select * from court, prop where court.prop_id=prop.login_id")
            return render_template('USER/add_rating.html',data=res)
    else:
        return redirect('/')


@app.route('/add_review',methods=['get','post'])
def add_review():
    if session['lin'] == "lo":
        if request.method=="POST":
            court_name=request.form['select']
            review=request.form['textfield']
            db=Db()
            db.insert("insert into review VALUES ('','"+str(session['lid'])+"','"+review+"',curdate(),'"+court_name+"')")
            return '''<script>alert("REVIEW ADDED");window.location="/user_home"</script>'''
        else:
            db=Db()
            res=db.select("select * from court,prop where court.prop_id=prop.login_id")
            return render_template('USER/add_review.html',data=res)
    else:
        return redirect('/')

# /////////////////////////////////////////////////////PUBLIC//////////////////////////////////////////////////////////




@app.route("/public_view_court")
def public_view_court():
    db=Db()
    ss=db.select("select * from court,prop where court.prop_id=prop.login_id")
    return render_template("Public/view_court.html", data=ss)



@app.route("/public_view_rating/<k>")
def public_view_rating(k):
    if session['lin'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM rating,users WHERE rating.user_id=users.login_id and rating.court_id='"+str(k)+"'")
        print(ss)
        return render_template("Public/view Rating.html", data=ss)
    else:
        return redirect('/')

@app.route("/public_view_review/<k>")
def public_view_review(k):
    if session['lin'] == "lo":
        db = Db()
        ss = db.select("SELECT * FROM review,users WHERE review.user_id=users.login_id and review.court_id='"+str(k)+"'")
        print(ss)
        return render_template("Public/view Review.html", data=ss)
    else:
        return redirect('/')















if __name__ == '__main__':
    app.run()
