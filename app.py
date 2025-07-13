from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Portfolio details page
@app.route('/portfolio-details')
def portfolio_details():
    return render_template('portfolio-details.html')

@app.route('/portfolio-details1')
def portfolio_details1():
    return render_template('portfolio-details1.html')

@app.route('/portfolio-details2')
def portfolio_details2():
    return render_template('portfolio-details2.html')

@app.route('/portfolio-details3')
def portfolio_details3():
    return render_template('portfolio-details3.html')

@app.route('/portfolio-details4')
def portfolio_details4():
    return render_template('portfolio-details4.html')

@app.route('/portfolio-details5')
def portfolio_details5():
    return render_template('portfolio-details5.html')

@app.route('/portfolio-details6')
def portfolio_details6():
    return render_template('portfolio-details6.html')


# Service details page
@app.route('/service-details')
def service_details():
    return render_template('service-details.html')

@app.route('/service-details1')
def service_details1():
    return render_template('service-details1.html')

@app.route('/service-details2')
def service_details2():
    return render_template('service-details2.html')


# Contact page with form handling
@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Optional: Save to a text file
        with open('messages.txt', 'a') as f:
            f.write(f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}\n---\n")

        flash('Your message has been sent successfully!', 'success')
        return redirect('/contacts')

    return render_template('contacts.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
