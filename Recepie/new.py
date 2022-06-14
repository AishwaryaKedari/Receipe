from flask import *
import pymysql

db = pymysql.connect(
    host="Localhost",
    user="root",
    password="",
    database="aishu"
)

cursor = db.cursor()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/maharashtrian")
def maharashtrian():
    cursor.execute("select * from indian")
    data = cursor.fetchall()
    return render_template("maharashtrian.html", userdata=data)


@app.route("/create", methods=["POST"])
def create():
    name = request.form.get('name')
    ingredients = request.form.get('ingredients')
    process = request.form.get('process')
    category = request.form.get('category')
    insq = "insert into indian(name,ingredients,process,category)values('{}','{}','{}','{}')".format(name, ingredients, process, category)

    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("maharashtrian"))
    except:
        db.rollback()
        return "Error in Query"


@app.route("/edit")
def edit():
    name = request.args.get('name')
    selq="select * from indian where name='{}'".format(name)
    cursor.execute(selq)
    data=cursor.fetchone()
    return render_template("edit.html",row=data)

@app.route("/update",methods=["POST"])
def update():
    ingredients=request.form.get('ingredients')
    process=request.form.get('process')
    category=request.form.get('category')
    name=request.form.get('name')
    insq="update indian set ingredients='{}',process='{}',category='{}' where name='{}'".format(ingredients,process,category,name)
    
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("maharashtrian"))
    except:
        db.rollback()
        return "Error in Query"
    
@app.route("/delete")
def delete():
    name = request.args.get('name')
    delq="Delete from indian where name='{}'".format(name)
    try:
        cursor.execute(delq)
        db.commit()
        return redirect(url_for("maharashtrian"))
    except:
        db.rollback()
        return "Error in Query"
      
@app.route("/Search")
def search():
    return render_template("search.html")

@app.route("/getdata",methods=["POST"])
def getdata():
    name=request.form.get('name')
    selq="select * from indian where name='{}'".format(name)
    cursor.execute(selq)
    data=cursor.fetchone()
    return render_template("search.html",row=data)
    
@app.route("/south")
def south():
    cursor.execute("select * from south")
    data = cursor.fetchall()
    return render_template("south.html",userdata=data)

@app.route("/create1",methods=["POST"])
def create1():
    name = request.form.get('name')
    ingredients = request.form.get('ingredients')
    process = request.form.get('process')
    category = request.form.get('category')
    insq = "insert into south(name,ingredients,process,category)values('{}','{}','{}','{}')".format(name,ingredients,process,category)
    
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("south"))
    except:
        db.rollback()
        return "Error in Query"
    
@app.route("/edit1")
def edit1():
    name = request.args.get('name')
    selq ="select * from south where name = '{}'".format(name)
    cursor.execute(selq)
    data=cursor.fetchone()
    return render_template("edit1.html",row=data)

@app.route("/update1",methods= ["POST"])
def update1():
    ingredients=request.form.get('ingredients')
    process=request.form.get('process')
    category=request.form.get('category')
    name=request.form.get('name')
    insq="update south set ingredients ='{}',process='{}',category='{}'where name='{}'".format(ingredients,process,category,name)
    
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("south"))
    except:
        db.rollback()
        return "Error in Query"
    
@app.route("/delete1")
def delete1():
    name = request.args.get('name')
    delq="delete from south where name='{}'".format(name)
    try:
        cursor.execute(delq)
        db.commit()
        return redirect(url_for("south"))
    except:
        db.rollback()
        return "Error in Query"
    
@app.route("/search1")
def search1():
    return render_template("search1.html")

@app.route("/getdata1",methods=["POST"])
def getdata1():
    name = request.form.get('name')
    selq = "select * from south where name='{}'".format(name)
    cursor.execute(selq)
    data = cursor.fetchone()
    return render_template("search1.html",newrow=data)
    

if __name__ == "__main__":
    app.run(debug=True)
