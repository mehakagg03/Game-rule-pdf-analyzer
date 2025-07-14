from flask import Flask, render_template, request
from query_data import query_rag

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    sources = []
    if request.method == "POST":
        query = request.form["query"]
        response, sources = query_rag(query, return_sources=True)
    return render_template("index.html", response=response, sources=sources)

if __name__ == "__main__":
    app.run(debug=True)
