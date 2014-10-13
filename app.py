from flask import Flask,render_template,request
from utils import BS, Parser



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():

    searchTerm = request.args.get("searchbox",None)

    return render_template("search.html")


@app.route("/results", methods=['GET', 'POST'])
def results():
    lastSearch = ""
    searchTerm = request.args.get("searchbox",None)

    if searchTerm != "":
        lastSearch = searchTerm
    return render_template("results.html",
                           SearchPlaceholder=searchTerm,
                           )



if __name__=="__main__":
    app.debug=True
    app.run()
