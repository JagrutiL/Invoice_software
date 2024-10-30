from flask import Flask, render_template, request, redirect, url_for, flash
from database import Database as Mydatabase

app = Flask(__name__)
app.secret_key = 'Anjali#123'

name = ''
mail = ''
is_admin = ''
emp = ''

@app.route('/', methods=['GET', 'POST'])
def login():
    global name, mail, is_admin, emp
    connection = Mydatabase.connect_dbs()
    cursor = connection.cursor()

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password))
        
        user = cursor.fetchone()

        cursor.execute('SELECT user_name from user;')
        emp = cursor.fetchall()
    
        connection.commit()
       
        if user:
            name = user[2]
            mail = user[3]
            is_admin = user[6]
            
            return redirect(url_for('dashboard')) 
        else:
            flash('Invalid Credentials!') 
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    global name, mail, is_admin, emp
    dashboard_name = "ADMIN DASHBOARD" if is_admin == 1 else "USER DASHBOARD"
    return render_template('dashboard.html', name=name, mail=mail, dashboard_name=dashboard_name, emp=emp, is_admin=is_admin)  

@app.route('/add_payment', methods=['GET', 'POST'])
def add_payment():
    return render_template('add_payment.html')  # Render the add payment page

@app.route('/detail', methods=['GET', 'POST'])
def detail():
    return render_template('detail.html')  # Render the add payment page

@app.route('/favicon.ico')
def favicon():
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
