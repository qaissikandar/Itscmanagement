import MySQLdb.cursors
from flask import Flask,flash, render_template, request,redirect
import flask
from flask_mysqldb import MySQL
app = Flask(__name__)
app.secret_key = "super secret key"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "12345"
app.config["MYSQL_DB"] = "project"
mysql=MySQL(app)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['uname']
        password = userDetails['password']
        confirmpass=userDetails['confirmpass']
        userid= userDetails["userid"]
        print(confirmpass)
        if confirmpass == password:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO user(name, password,userid) VALUES(%s, %s,%s)",(name, password , userid))
            mysql.connection.commit()
            cur.close()
            return redirect("/login")
    return render_template('index1.html')
@app.route('/Allposts',  methods=['GET', 'POST'])
def Allposts():
    if request.method == 'POST':
        title = request.form['title']
        comment = request.form['comment']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO posts VALUES ( % s, % s)', (title, comment))
        mysql.connection.commit()
        return redirect('/posts')
    return render_template('posts.html')
@app.route('/posts')
def posts():
        cursor = mysql.connection.cursor()
        account = cursor.execute('SELECT * FROM posts')
        if account > 0:
            all_posts = cursor.fetchall()
        return render_template('showPosts.html', posts = all_posts)
@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['uname']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        okay=cur.execute("Select userid  from user where  (name=%s and password=%s)",(name,password))
        if okay>0:
            userid = cur.fetchall()
            global current_user_id 
            current_user_id = userid[0][0]
            return redirect("/design")
        else:
            flash("Username or password incorrect.") 
        mysql.connection.commit()
        cur.close()
    return render_template('login.html')


@app.route('/administrator', methods=['GET', 'POST'])
def administrator():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        password = userDetails['password']
        cur = mysql.connection.cursor()
        okay = cur.execute("Select name, password from admin where  (name=%s and password=%s)", (name, password))
        if okay > 0:
            userid = cur.fetchall()
            global current_user_id
            current_user_id = userid[0][0]
            return redirect("/Allposts")
        else:
            flash("Username or password incorrect.")
        mysql.connection.commit()
        cur.close()
    return render_template("/administrator.html")
@app.route('/design', methods=['GET', 'POST'])
def design():
    if request.method == 'GET':
        return render_template('design.html')
@app.route('/records', methods=['GET', 'POST'])
def records():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        things=cursor.execute("Select * from records")
        record = cursor.fetchall()
        title,number=[],[]
        print(record)
        for i in range(len(record)):
            title.append(record[i][0])
            number.append(record[i][1])
        length=len(number)
        return render_template('records.html',title=title,number=number,length=length)
@app.route('/music',methods=['GET','POST'])
def music_system():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        things=cursor.execute("Select * from issued")
        music_system1 = cursor.fetchall()
        Name,number,reg=[],[],[]
        print(music_system1)
        for i in range(len(music_system1)):
            Name.append(music_system1[i][0])
            number.append(music_system1[i][1])
            reg.append(music_system1[i][2])
        length=len(number)
        return render_template('music.html',Name=Name,number=number,reg=reg,length=length)
@app.route('/IT_MEMBERS',methods=['GET','POST'])
def IT_MEMBERS():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        things=cursor.execute("Select * from IT_MEMBERS")
        IT_persons = cursor.fetchall()
        Name,REG_NO=[],[]
        print(IT_persons)
        for i in range(len(IT_persons)):
            Name.append(IT_persons[i][0])
            REG_NO.append(IT_persons[i][1])
        length=len(REG_NO)
        return render_template('IT_MEMBERS.html',Name=Name,REG_NO=REG_NO,length=length)
    
    

@app.route('/issued',methods=['GET', 'POST'])
def issued():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['uname']
        Roll = userDetails['Roll']
        Equipments = userDetails['Equipments']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO issued VALUES ( % s, % s, % s)', (name, Roll,Equipments))
        mysql.connection.commit()
        return redirect("/design")
    return render_template('issued.html')   
    
if "__name__==__main__":
    app.run(debug=True)
