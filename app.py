fromflaskimportFlask,render_template

app=Flask(__name__)

@app.route("/")#default page of web

defindex():
    returnrender_template('index.html')

@app.route("/about")
defabout():
    returnrender_template('about.html')

if__name__=='__main__':
    app.run()
