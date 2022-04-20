from flask import Flask,render_template,request,redirect

app=Flask(__name__)

@app.route('/')
def home():
    return "<h3>this is my  website home page</h3>"

@app.route('/welcome')
def welcome():
    user='naresh'
    return render_template('welcome.html',user=user)

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method=='get':
        username=request.form['username']
        password=request.form.get('password')
        print(username)

        if username=='prince123' and password=='prince456':
            msg="login success"
            return redirect('welcome.html',msg=msg)
        else:
            msg='username or password is incorrect'
            return render_template('login.html',msg=msg)
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)