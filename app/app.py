from flask import Flask,request,render_template,redirect
import pickle
import mysql.connector as  mysql

sql=mysql.connect(user='root',password='786786',host='localhost',database='spam_detector')

cur=sql.cursor()


app=Flask(__name__)
app.secret_key='hawk'

vect_f=open('vectorizer.pkl','rb')
model_f=open('spam_model.pkl','rb')

vectorizer=pickle.load(vect_f)
model=pickle.load(model_f)

@app.route('/',methods=['GET','POST'])
def check():

    if(request.method =='POST'):
        msg=request.form.get('message')
        msg=[msg]
        msg_fin=vectorizer.transform(msg)

        res=model.predict(msg_fin)

        if(res[0]==1):
            return render_template('index.html',prediction='Spam')
        else:
            return render_template('index.html',prediction='Not Spam')
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():

    if(request.method=='POST'):
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')

        cur.execute("select username from users where email=%s",(email,))

        check=cur.fetchone()

        if check:
            return redirect('/register')
        else:
            return redirect('/')

    return render_template('register.html')