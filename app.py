from flask import Flask,request,render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('/registration.html')
@app.route('/registration.html',methods=['post'])
def registration():
    name=request.form['name']
    password=request.form['password']
    email=request.form['email']
    return render_template('/successful.html',name=name,email=email)
if __name__== '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)