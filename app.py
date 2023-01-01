from flask import Flask, render_template, redirect, request


app = Flask(__name__, template_folder='templates', static_folder='static')



SPORTS = [
    "Basketball",
    "Football",
    "Volleyball"
]

REGISTRANTS = {}

@app.route('/')

@app.route('/')
def home():
    return render_template('index.html', sports=SPORTS)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    if not name:
        return render_template('error.html')
    sport = request.form.get('sport')
    REGISTRANTS[name] = sport
    if sport not in SPORTS:
        return render_template('error.html')
    else:
        return render_template('register.html')


@app.route('/registrants')
def regs():
    return render_template('registrants.html', registrants=REGISTRANTS)


if __name__ == '__main__':
    app.run(debug=True)