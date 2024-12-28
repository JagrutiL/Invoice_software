from flask import Flask, render_template, request, redirect, url_for, flash, session,jsonify
from database import Database as Mydatabase
from datetime import datetime
import random
import string






app = Flask(__name__)
app.secret_key = 'Anjali#123'

@app.route('/', methods=['GET', 'POST'])
def login():
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
            # Store information in session instead of global variables
            session['name'] = user[2]
            session['mail'] = user[3]
            session['is_admin'] = user[6]
            session['emp'] = emp  
            session['user_id'] = user[1]
            print('sessiondata',session['name'],session['mail'],session['is_admin'],session['emp'],session['user_id'])
            return redirect(url_for('dashboard')) 
        else:
            flash('Invalid Credentials!') 
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))
    

def get_session_data():
    name = session.get('name')
    mail = session.get('mail')
    is_admin = session.get('is_admin')
    emp = session.get('emp')
    user_id = session.get('user_id')
    print('session getdata',name,mail,is_admin,emp)
    dashboard_name = "ADMIN DASHBOARD" if is_admin == 1 else "USER DASHBOARD"
    return name, mail, is_admin, emp, dashboard_name,user_id


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    from datetime import datetime
    from flask import request

    # Get the status filter from the request
    status_filter = request.args.get('status', None)  # 'pending' or 'All Except Pending'
    print('status_filter:', status_filter)

    name, mail, is_admin, emp, dashboard_name, user_id = get_session_data()
    connection = Mydatabase.connect_dbs()
    cursor = connection.cursor()

    # Query to fetch payments based on user role and status filter
    if is_admin == 1:
        if status_filter == "all":
            query = "SELECT item_name, timestamp, amount, status, invoice_no FROM payment_details WHERE status != 0;"
        elif status_filter == "pending":
            query = "SELECT item_name, timestamp, amount, status, invoice_no FROM payment_details WHERE status = 0;"
        else:
            query = "SELECT item_name, timestamp, amount, status, invoice_no FROM payment_details;"
        cursor.execute(query)
    elif is_admin == 2:
        if status_filter == "all":
            query = """
                SELECT item_name, timestamp, amount, status, invoice_no 
                FROM payment_details 
                WHERE user_id = %s AND status != 0;
            """
        elif status_filter == "pending":
            query = """
                SELECT item_name, timestamp, amount, status, invoice_no 
                FROM payment_details 
                WHERE user_id = %s AND status = 0;
            """
        else:
            query = """
                SELECT item_name, timestamp, amount, status, invoice_no 
                FROM payment_details 
                WHERE user_id = %s;
            """
        cursor.execute(query, (user_id,))

    result = cursor.fetchall()
    print('Raw result:', result)

    # Mapping for status
    status_mapping = {
        0: 'Pending',
        1: 'Waiting for Payment',
        2: 'Payment Done - Upload Invoice',
        3: 'Completed',
        4: 'Rejected',
        5: 'all'
    }

    # Format results
    formatted_result = [
        (
            item[0],
            item[1].strftime('%b %d, %Y %H:%M:%S') if isinstance(item[1], datetime) else item[1],
            item[2],
            status_mapping.get(item[3], 'Unknown'),
            item[3],
            item[4],
        )
        for item in result
    ]
    print('Formatted result:', formatted_result)

    return render_template(
        'dashboard.html',
        name=name,
        mail=mail,
        dashboard_name=dashboard_name,
        emp=emp,
        is_admin=is_admin,
        user_id=user_id,
        result=formatted_result
    )




# @app.route('/dashboard', methods=['GET', 'POST'])
# def dashboard():
#     from datetime import datetime

#     name, mail, is_admin, emp, dashboard_name, user_id = get_session_data()
#     connection = Mydatabase.connect_dbs()
#     cursor = connection.cursor()

#     # Query to fetch payments based on user role
#     if is_admin == 1:
        
#         query = "SELECT item_name, timestamp, amount, status,invoice_no FROM payment_details;"
#         cursor.execute(query)
#     elif is_admin == 2 :
#         query = "SELECT item_name, timestamp, amount, status,invoice_no FROM payment_details WHERE user_id = %s;"
#         cursor.execute(query, (user_id,))
    
#     result = cursor.fetchall()
#     print('result-------------',result)

#     # Mapping for status
#     status_mapping = {
#         0: 'Pending',
#         1: 'Waiting for Payment',
#         2: 'Payment Done - Upload Invoice',
#         3: 'Completed',
#         4: 'Rejected',
#     }

#     # Format results
#     formatted_result = [
#         (
#             item[0],
#             item[1].strftime('%b %d, %Y %H:%M:%S') if isinstance(item[1], datetime) else item[1],
#             item[2],
#             status_mapping.get(item[3], 'Unknown'),
#             item[3],
#             item[4]
#         )
#         for item in result
#     ]
#     print('ttttt',formatted_result)

#     return render_template(
#         'dashboard.html',
#         name=name,
#         mail=mail,
#         dashboard_name=dashboard_name,
#         emp=emp,
#         is_admin=is_admin,
#         user_id=user_id,
#         result=formatted_result
#     )


# @app.route('/dashboard', methods=['GET', 'POST'])
# def dashboard():
#     from datetime import datetime

#     name, mail, is_admin, emp, dashboard_name, user_id = get_session_data()
#     connection = Mydatabase.connect_dbs()
#     cursor = connection.cursor()

#     # Query to fetch payments based on user role
#     if is_admin == 1:
#         # Fetch entries for "All Payments" (exclude Pending)
#         query_all_payments = """
#             SELECT item_name, timestamp, amount, status, invoice_no 
#             FROM payment_details 
#             WHERE status != 0;"""
#         cursor.execute(query_all_payments)
#         all_payments = cursor.fetchall()

#         # Fetch entries for "All Requests" (Pending status only)
#         query_all_requests = """
#             SELECT item_name, timestamp, amount, status, invoice_no 
#             FROM payment_details 
#             WHERE status = 0;"""
#         cursor.execute(query_all_requests)
#         all_requests = cursor.fetchall()
#     elif is_admin == 2:
#         # Fetch entries for "All Payments" for a specific user (exclude Pending)
#         query_all_payments = """
#             SELECT item_name, timestamp, amount, status, invoice_no 
#             FROM payment_details 
#             WHERE user_id = %s"""
#         cursor.execute(query_all_payments, (user_id,))
#         all_payments = cursor.fetchall()
#         all_requests = []  

#     # Mapping for status
#     status_mapping = {
#         0: 'Pending',
#         1: 'Waiting for Payment',
#         2: 'Payment Done - Upload Invoice',
#         3: 'Completed',
#         4: 'Rejected',
#     }

#     # Format results
#     def format_results(results):
#         return [
#             (
#                 item[0],
#                 item[1].strftime('%b %d, %Y %H:%M:%S') if isinstance(item[1], datetime) else item[1],
#                 item[2],
#                 status_mapping.get(item[3], 'Unknown'),
#                 item[3],
#                 item[4]
#             )
#             for item in results
#         ]

#     formatted_all_payments = format_results(all_payments)
#     formatted_all_requests = format_results(all_requests)
#     print('eureyueyeyrue',formatted_all_payments)

#     return render_template(
#         'dashboard.html',
#         name=name,
#         mail=mail,
#         dashboard_name=dashboard_name,
#         emp=emp,
#         is_admin=is_admin,
#         user_id=user_id,
#         result=formatted_all_payments,
#         requests=formatted_all_requests
#     )





def generate_invoice_number():
    # Generate 4 random digits
    digits = ''.join(random.choices(string.digits, k=4))
    # Generate 4 random uppercase letters
    letters = ''.join(random.choices(string.ascii_uppercase, k=4))
    # Combine and shuffle them
    invoice_number = ''.join(random.sample(digits + letters, len(digits + letters)))
    return invoice_number


@app.route('/add_payment', methods=['GET', 'POST'])
def add_payment():
    
    name, mail, admin, emp, dashboard_name, user_id = get_session_data()

    if request.method == 'POST':
       
        invoice_number = generate_invoice_number()

        # Retrieve form data
        item_name = request.form.get('item_name')
        item_details = request.form.get('item_details')
        vendor_name = request.form.get('vendor_name')
        quantity = request.form.get('quantity')
        amount = request.form.get('amount')
        payment_method = request.form.get('payment_method')

        print('Received:', vendor_name, item_name, item_details)

        # Database connection
        connection = Mydatabase.connect_dbs()
        cursor = connection.cursor()

        # Insert query
        query_insert = """
        INSERT INTO payment_details (
            item_name, details, vendor_name, quantity, amount, payment, 
            user_id, admin, status, invoice_no
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Determine status based on the user role
        if admin == 2:
            status = 0  # Admin
        else:
            status = 0  # Non-admin


        # Values to insert
        values = (
            item_name, item_details, vendor_name, quantity, amount, 
            payment_method, user_id, admin, status, invoice_number
        )
        

        try:
            # Execute the query
            cursor.execute(query_insert, values)
            connection.commit()
            print('Data Inserted Successfully')

            # Render template with success message
            return render_template(
                'add_payment.html',
                name=name,
                mail=mail,
                dashboard_name=dashboard_name,
                emp=emp,
                admin=admin,
                invoice_number=invoice_number,
                success="Payment details saved successfully."
            )
        except Exception as e:
            # Rollback in case of an error
            connection.rollback()
            print("Failed to insert data:", e)

            # Render template with error message
            return render_template(
                'add_payment.html',
                name=name,
                mail=mail,
                dashboard_name=dashboard_name,
                emp=emp,
                admin=admin,
                error="Failed to save payment details. Please try again."
            )
        finally:
            # Close cursor and connection
            cursor.close()
            connection.close()

    # Render template for GET request
    return render_template(
        'add_payment.html',
        name=name,
        mail=mail,
        dashboard_name=dashboard_name,
        emp=emp,
        admin=admin
    )


@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.get_json()
    invoice_number = data.get('invoice_number')
    action = data.get('action')  
    
    if not invoice_number:
        return jsonify({"error": "Missing invoice number"}), 400

    connection = Mydatabase.connect_dbs()
    cursor = connection.cursor()

    # Determine the new status based on the action
    new_status = 1 if action == 'accept' else 4  # 1: Approved, 4: Rejected

    try:
        # Update the status in the database
        query = "UPDATE payment_details SET status = %s WHERE invoice_no = %s;"
        cursor.execute(query, (new_status, invoice_number))
        connection.commit()
        return jsonify({"success": True, "status": new_status}), 200
    except Mydatabase.Error as e:
        connection.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()




@app.route('/detail/<string:invoice_number>', methods=['GET', 'POST'])
def detail(invoice_number):
    print('invoice', invoice_number)
    # Fetch session data
    try:
        name, mail, is_admin, emp, dashboard_name, user_id = get_session_data()
        
    except ValueError as e:
        print("Session data format mismatch:", e)
        return "Error: Invalid session data format.", 500

    # Initialize payment details
    payment_details = {}

    if invoice_number:
        connection = Mydatabase.connect_dbs()
        cursor = connection.cursor()

        query = """
        SELECT 
            item_name, 
            details, 
            vendor_name, 
            quantity, 
            amount,
            payment, 
            status, 
            invoice_no, 
            DATE_FORMAT(timestamp, '%%Y-%%m-%%d') AS issued_date,
            CONCAT(YEAR(timestamp), '-', MONTH(timestamp), '-25') AS due_date
        FROM 
            payment_details
        WHERE 
            invoice_no = %s
        """
        cursor.execute(query, (invoice_number,))
        payment_details = cursor.fetchone()
        print('payment11----', payment_details)
        try:
            if payment_details:
                    # Convert result to a dictionary for easy access in the template
                columns = [col[0] for col in cursor.description]
                payment_details = dict(zip(columns, payment_details))
            else:
                payment_details = {'error': 'No details found for the provided invoice number.'}
        except Exception as e:
            print("Failed to fetch payment details:", e)
            payment_details = {'error': 'Error fetching payment details.'}
        finally:
            cursor.close()
            connection.close()    
    # Render template with payment details
    return render_template(
        'detail.html',
        name=name,
        mail=mail,
        dashboard_name=dashboard_name,
        emp=emp,
        admin=is_admin,
        payment_details=payment_details
    )



@app.route('/favicon.ico')
def favicon():
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)