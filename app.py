from flask import Flask,render_template,request



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    lastSearch = ""
    searchTerm = request.args.get("searchbox",None)

    if searchTerm != "":
        lastSearch = searchTerm
    return render_template("search.html",
                           lastSearch=lastSearch,
                           )


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
