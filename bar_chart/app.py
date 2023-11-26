from flask import Flask, render_template, request
import plotly.express as px
import plotly.io as pio
from io import BytesIO
import base64

app = Flask(__name__)

# Sample data for demonstration
sample_data = {
    'Category': ['A', 'B', 'C'],
    'Value': [25, 40, 30]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_chart', methods=['POST'])
def generate_chart():
    # Get user inputs from the form
    category_values = request.form.getlist('category')
    value_values = request.form.getlist('value')

    # Convert values to appropriate types (e.g., integers)
    values = list(map(int, value_values))

    # Create a Plotly bar chart
    fig = px.bar(x=category_values, y=values, labels={'x': 'Category', 'y': 'Value'})

    # Convert the figure to HTML for rendering
    chart_html = pio.to_html(fig, full_html=False)

    return render_template('index.html', chart_html=chart_html)

if __name__ == '__main__':
    app.run(debug=True)
