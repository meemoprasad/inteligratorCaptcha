from flask import Flask, render_template, session, redirect, url_for
from api.captcha import captcha_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session tracking

app.register_blueprint(captcha_bp, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')

# Example of a protected page
@app.route('/dashboard')
def dashboard():
    if not session.get('captcha_verified'):
        return redirect(url_for('index'))
    return render_template('dashboard.html')  # Create dashboard.html for real content

if __name__ == '__main__':
    app.run(debug=True)
