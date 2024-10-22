from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for security

def get_db_connection():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host='localhost',        # e.g., 'localhost' or an IP address
        user='root',            # Your MySQL username
        password='Root',        # Your MySQL password
        database='invoice'      # Your database name
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)  # Use dictionary for row factory
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password))
        user = cursor.fetchone()
        cursor.close()  # Close the cursor
        conn.close()    # Close the connection

        if user:
            return redirect(url_for('dashboard'))  # Redirect to the dashboard
        else:
            flash('Invalid Credentials!')  # Show flash message for invalid credentials
            return redirect(url_for('login'))

    return render_template('login.html')  # Render the login page

@app.route('/dashboard')
def dashboard():
    return render_template('invoice_dashboard copy.html')  # Render the dashboard page

@app.route('/add_payment')
def add_payment():
    return render_template('add_payment.html')  # Render the add payment page

@app.route('/payment_detail')
def payment_detail():
    return render_template('detail.html')  # Render the add payment page


if __name__ == '__main__':
    app.run(debug=True)
