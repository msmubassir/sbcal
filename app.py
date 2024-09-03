from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:day>day')
def day(day):
    return render_template(f'{day}day.html', day=day)

if __name__ == '__main__':
    app.run(debug=True)
