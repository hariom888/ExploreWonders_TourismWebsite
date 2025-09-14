from flask import Flask, render_template, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

app = Flask(__name__)

# -----------------------------
# Scheduled Task
# -----------------------------
def my_scheduled_task():
    # Example task: just prints for now
    print("Scheduled task executed! You can update DB or cache here.")

# Initialize background scheduler
scheduler = BackgroundScheduler()
# Run task every 5 minutes (adjust as needed)
scheduler.add_job(func=my_scheduled_task, trigger="interval", minutes=2)
scheduler.start()

# Shut down scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

# -----------------------------
# Routes
# -----------------------------
@app.route('/')
def home():
    return render_template('home.html')

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

# -----------------------------
# Run app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
