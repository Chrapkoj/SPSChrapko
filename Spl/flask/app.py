from flask import Flask, render_template, url_for, request
import os
import plotly.graph_objects as go
import plotly.io as pio

app = Flask(__name__)

@app.route("/1")
def hello():
    return "Hello World!"

@app.route("/2")
def pozdrva_ze_souboru():
    return render_template("index2.html")

@app.route("/3")
def pozdrva_ze_souboru_CSS():
    return render_template("index3.html")

@app.route("/4")
def pozdrva_z_promenny():
    text = "Ahoj z proměnné"
    return render_template("index4.html", message = text)

@app.route("/5")
def obrazek():
    image_url = url_for('static', filename='images/jew.jpg')
    return render_template("index5.html", image_url=image_url)

@app.route("/6", methods=['GET', 'POST'])
def prvniFormulaCislo():
    result = None
    if request.method == 'POST':
        number = request.form.get('number', type=int)
        if number is not None:
            result = number + 1
    return render_template("index6.html", result=result)

app.config['UPLOAD_FOLDER'] = "static/uploadedFiles/"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
@app.route("/7", methods=['GET', 'POST'])
def nahrani_souboru():
    content = None
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswitch('.txt'):
            file_path = os.path.join(app.config["UPLOAD-FOLDER"], file.filename)
            file.save(file_path)
            file.seek(0)
            content = file.read().decode('utf-8')
    return render_template("index7.html", content=content)

@app.route('/8')
def graph():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[10, 20, 25, 30],
                             mode='lines+markers', name='Data 1'))
    fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[15, 18, 22, 27],
                             mode='lines+markers', name='Data 2'))

    fig.update_layout(
        title="Ukázkový interaktivní graf",
        xaxis_title="X-osa",
        yaxis_title="Y-osa",
        template="plotly_white"
    )

    graph_html = pio.to_html(fig, full_html=False)
    return render_template("index8.html", graph_html=graph_html)

@app.route('/9/<int:id>/<string:name>', methods=['GET'])
def parametry(id, name):
    return render_template("index9.html", id=id, name=name)

if __name__ == "__main__":
    app.run()
