from flask import Flask, render_template, send_from_directory, request, redirect
import os
import csv

app = Flask (__name__)


@app.route('/<string:page_name>')
def my_home(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode='a') as db:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = db.write(f'{email},{subject},{message}\n')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as db2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        content = [email, subject, message]
        csv_writer = csv.writer(
            db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(content)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():

    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. try again'
