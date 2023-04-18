from flask import Flask, render_template, flash, request, redirect
import requests

app = Flask(_name__)
app.secret_key = 'your_secret_key'

# Route for the landing page
@app.route('/', methods=['GET', 'POST'])
def arithmetic_microservice():
    if request.method == 'POST':
        #number_1 = 10
        #number_2 = 20
        number_1 = int(request.form['first'])
        number_2 = int(request.form['second'])
        operation =  request.form.get('operation')
        #if number_1 is not None and number_2 is not None:
            #number_1 = int(number_1)
            #number_2 = int(number_2)
            
        if operation == 'add':
            result = requests.get(f'http://addition-service:5051/Addition?param1={number_1}&param2={number_2}') # Send GET request to addition service
            if result.status_code == 200:
                flash(f'Result: {result.json()["result"]}') # Flash the result message from addition service
            else:
                flash('Error: Addition service failed') # Flash an error message
        elif operation == 'minus':
            result = requests.get(f'http://subtraction-service:5052/Subtraction?param1={number_1}&param2={number_2}') # Send GET request to subtraction service
            if result.status_code == 200:
                flash(f'Result: {result.json()["result"]}') # Flash the result message from subtraction service
            else:
                flash('Error: Subtraction service failed') # Flash an error message
        elif operation == 'multiply':
            result = requests.get(f'http://multiplication-service:5053/Multiplication?param1={number_1}&param2={number_2}') # Send GET request to multiplication service
            if result.status_code == 200:
                flash(f'Result: {result.json()["result"]}') # Flash the result message from multiplication service
            else:
                flash('Error: Multiplication service failed') # Flash an error message
        elif operation == 'divide':
            result = requests.get(f'http://division-service:5054/Division?param1={number_1}&param2={number_2}') # Send GET request to division service
            if result.status_code == 200:
                flash(f'Result: {result.json()["result"]}') # Flash the result message from division service
            else:
                flash('Error: Division service failed') # Flash an error message
        elif operation == 'modulus':
            result = requests.get(f'http://modulus-service:5055/Modulus?param1={number_1}&param2={number_2}') # Send GET request to modulus service
            if result.status_code == 200:
                flash(f'Result: {result.json()["result"]}') # Flash the result message from modulus service
            else:
                flash('Error: Modulus service failed') # Flash an error message
        elif operation == 'exponent':
            result = requests.get(f'http://exponent-service:5056/Exponent?param1={number_1}&param2={number_2}') # Send GET request to exponent service
            if result.status_code == 200:
                flash(f'Result: {result.json()["result"]}') # Flash the result message from exponent service
            else:
                flash('Error: Exponent service failed') # Flash an error message
        elif operation == 'greaterthan':
            result = requests.get(f'http://greaterthan-service:5057/Greaterthan?param1={number_1}&param2={number_2}') # Send GET request to greater_than service
            if result.status_code == 200:
                flash(f'Result: {result.json()["result"]}') # Flash the result message from greater_than service
            else:
                flash('Error: Greater_than service failed') # Flash an error message
       
    return render_template('index.html')

if _name__ == '__main__':
    app.run(
        debug=True,
        port = 5050,
        host="0.0.0.0"
    )
