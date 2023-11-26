# app.py

from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/plot')
def api_plot():
    # Path to the saved plot file
    plot_path = 'plot.png'

    return send_file(plot_path, mimetype='image/png' )

if __name__ == "__main__":
    app.run(debug=True)