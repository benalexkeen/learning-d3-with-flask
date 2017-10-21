import json
import os

from flask import Flask, render_template
import pandas as pd

__here__ = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(__here__, 'data')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/simple-line/")
def simple_line():
    df = pd.read_csv(os.path.join(data_dir, 'simple_line.csv'))
    records = df.to_dict(orient='records')
    data = {
        'graph_data': json.dumps(records)
    }
    return render_template("simple_line.html", data=data)


@app.route("/simple-step/")
def simple_step():
    df = pd.read_csv(os.path.join(data_dir, 'simple_line.csv'))
    records = df.to_dict(orient='records')
    data = {
        'graph_data': json.dumps(records)
    }
    return render_template("simple_step.html", data=data)


@app.route("/simple-spline/")
def simple_spline():
    df = pd.read_csv(os.path.join(data_dir, 'simple_line.csv'))
    records = df.to_dict(orient='records')
    data = {
        'graph_data': json.dumps(records)
    }
    return render_template("simple_spline.html", data=data)


@app.route("/multiple-line/")
def multiple_line():
    df = pd.read_csv(os.path.join(data_dir, 'multiple_line.csv'))
    records = df.to_dict(orient='records')
    data = {
        'graph_data': json.dumps(records)
    }
    return render_template("multiple_line.html", data=data)


@app.route("/simple-area/")
def simple_area():
    df = pd.read_csv(os.path.join(data_dir, 'simple_line.csv'))
    records = df.to_dict(orient='records')
    data = {
        'graph_data': json.dumps(records)
    }
    return render_template("simple_area.html", data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)