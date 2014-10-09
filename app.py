from flask import Flask,render_template,request



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("search.html",
                           SearchPlaceholder="Search..."
                           )




if __name__=="__main__":
    app.debug=True
    app.run()
