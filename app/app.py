from flask import Flask,request,render_template,redirect
import pickle

app=Flask(__name__)

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