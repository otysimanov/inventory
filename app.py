from flask import Flask, render_template, request, redirect, url_for, flash
import datetime
# ===============================================

# Starter Template Flask
# By Makassar Coding

# ================================================
# Menentukan Nama Folder Penyimpanan Asset
app = Flask(__name__, static_folder='static', static_url_path='')
# Untuk Menggunakan flash pada flask
app.secret_key = 'iNiAdalahsecrEtKey'
# Untuk Mentukan Batas Waktu Session
app.permanent_session_lifetime = datetime.timedelta(days=7)
# Menentukan Jumlah Maksimal Upload File
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin':
            if password == 'admin':
                return redirect(url_for('dashboard'))
            else:
                
                flash('Password / Username Salah', 'danger')
                return redirect(url_for('index'))
        else:
            flash('Password / Username Salah', 'danger')
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# Untuk Menjalankan Program Flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)