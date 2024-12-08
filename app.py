from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Database model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(20), nullable=False)  # Add this line
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    bank_name = db.Column(db.String(100), nullable=False)
    account_number = db.Column(db.String(50), nullable=False)
    emergency_contact_name = db.Column(db.String(100), nullable=False)
    emergency_contact_phone = db.Column(db.String(20), nullable=False)


# Home route - display form
@app.route('/')
def index():
    return render_template('form.html')


# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Collect form data
        new_employee = Employee(
            full_name=request.form['full_name'],
            start_date=request.form['start_date'],
            address=request.form['address'],
            phone=request.form['phone'],
            email=request.form['email'],
            bank_name=request.form['bank_name'],
            account_number=request.form['account_number'],
            emergency_contact_name=request.form['emergency_contact_name'],
            emergency_contact_phone=request.form['emergency_contact_phone']
        )
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('admin'))


# Admin route - review data
@app.route('/admin')
def admin():
    employees = Employee.query.all()
    return render_template('admin.html', employees=employees)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure the database is created
    app.run(debug=True)
