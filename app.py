from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Other pages
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/destinations')
def destinations():
    return render_template('destinations.html')

@app.route('/login')
def loginpage():
    return render_template('loginpage.html')

@app.route('/register')
def registerpage():
    return render_template('registerpage.html')

@app.route('/resetpassword')
def resetpassword():
    return render_template('resetpassword.html')

@app.route('/services')
def services():
    return render_template('services.html')

# Example backend API route
@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_json() or {}
    return jsonify({"status": "ok", "received": data})

if __name__ == "__main__":
    app.run(debug=True)
