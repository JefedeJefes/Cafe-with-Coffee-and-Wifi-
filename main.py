from flask import Flask , render_template , url_for , request , flash , redirect
import pandas as pd 


app = Flask(__name__)
app.secret_key="arjunvyas"

data = pd.read_csv("./cafe-data.csv")
cafes = data.to_dict(orient='records')
# print(cafes)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/cafes')
def all_cafes():
    
    

    return render_template("cafe.html",cafes=cafes)



@app.route('/add',methods=["POST","GET"])
def add_cafes():
    if request.method == "POST":
        
        cafe_name = request.form.get("cafe_name")
        location = request.form.get("location")
        open = request.form.get("open")
        close = request.form.get("close")
        coffee = request.form.get("coffee")
        wifi = request.form.get("wifi")
        power = request.form.get("power")

        new_cafe = {
            "Cafe Name":cafe_name,
            "Location":location,
            "Open":open,
            "Close":close,
            "Coffee":coffee,
            "Wifi":wifi,
            "Power":power
        }
        updated_cafes = cafes.append(new_cafe)
        updated_cafes= pd.DataFrame(cafes)
        updated_cafes.to_csv("./cafe-data.csv", index=False)
        return redirect(url_for("all_cafes"))

    return render_template("add.html")

if __name__ == ("__main__"):
    app.run(debug=True, host='0.0.0.0')