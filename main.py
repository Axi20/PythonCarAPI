from flask import *
import json
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/view")
def view():
    con = sqlite3.connect("CarRentDB.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Vehicle")
    rows = cur.fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route("/savedetails/", methods=["POST"])
def saveDetails():
    msg = "msg"
    try:
        data = request.get_json(force=True)
        print(data)
        RegNumber = data["regNumber"]
        Brand = data["brand"]
        Model = data["model"]
        Year = data["year"]
        Hp = data["hp"]
        Color = data["color"]
        Fuel = data["fuel"]
        #Consumption = data["consumption"]
        ShiftType = data["shiftType"]
        DailyPrice = data["dailyPrice"]
        with sqlite3.connect("CarRentDB.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into Vehicle (RegNumber, Brand, Model, Year, Hp, Color, Fuel, ShiftType, DailyPrice) values (?,?,?,?,?,?,?,?,?)", (RegNumber, Brand, Model,Year,Hp,Color,Fuel,ShiftType,DailyPrice))
            con.commit()
            msg = "Vehicle successfully Added"
    except:
        con.rollback()
        msg = "We can not add the vehicle to the list"
    finally:
        return Brand
        con.close()

@app.route("/deleterecord/", methods=["POST"])
def deleterecord():
    data = request.get_json(force=True)
    regNumber = str(data["regNumber"])
    print(regNumber)
    with sqlite3.connect("CarRentDB.db") as con:
        try:
            cur = con.cursor()
            cur.execute(f"delete from Vehicle where RegNumber = {regNumber}")
            msg = "record successfully deleted"
            return msg
        except:
            msg = "can't be deleted"
            return msg


@app.route("/updatedetails/", methods=["POST"])
def updaterecord():
    try:
        data = request.get_json(force=True)
        print(data)
        id = data["regNumber"]
        listItem = data["listItem"]
        valueToUpdate = data["valueToUpdate"]
        #RegNumber = data["regNumber"]

        if(listItem == "Brand"):
            with sqlite3.connect("CarRentDB.db") as con:
                cur = con.cursor()
                query = f"UPDATE Vehicle SET Brand='{valueToUpdate}' WHERE RegNumber={id}"
                print(query)
                cur.execute(query)
                con.commit()
                msg = "Vehicle successfully Updated"
        elif (listItem == "Model"):
            with sqlite3.connect("CarRentDB.db") as con:
                cur = con.cursor()
                query = f"UPDATE Vehicle SET Model='{valueToUpdate}' WHERE RegNumber={id}"
                print(query)
                cur.execute(query)
                con.commit()
                msg = "Vehicle successfully Updated"
        elif (listItem == "Year"):
            with sqlite3.connect("CarRentDB.db") as con:
                cur = con.cursor()
                query = f"UPDATE Vehicle SET Year='{valueToUpdate}' WHERE RegNumber={id}"
                print(query)
                cur.execute(query)
                con.commit()
                msg = "Vehicle successfully Updated"
        elif (listItem == "Hp"):
            with sqlite3.connect("CarRentDB.db") as con:
                cur = con.cursor()
                query = f"UPDATE Vehicle SET Hp='{valueToUpdate}' WHERE RegNumber={id}"
                print(query)
                cur.execute(query)
                con.commit()
                msg = "Vehicle successfully Updated"
        elif (listItem == "Color"):
            with sqlite3.connect("CarRentDB.db") as con:
                cur = con.cursor()
                query = f"UPDATE Vehicle SET Color='{valueToUpdate}' WHERE RegNumber={id}"
                print(query)
                cur.execute(query)
                con.commit()
                msg = "Vehicle successfully Updated"
        elif (listItem == "Fuel"):
            with sqlite3.connect("CarRentDB.db") as con:
                cur = con.cursor()
                query = f"UPDATE Vehicle SET Fuel='{valueToUpdate}' WHERE RegNumber={id}"
                print(query)
                cur.execute(query)
                con.commit()
                msg = "Vehicle successfully Updated"
        elif (listItem == "ShiftType"):
            with sqlite3.connect("CarRentDB.db") as con:
                cur = con.cursor()
                query = f"UPDATE Vehicle SET ShiftType='{valueToUpdate}' WHERE RegNumber={id}"
                print(query)
                cur.execute(query)
                con.commit()
                msg = "Vehicle successfully Updated"
        elif (listItem == "DailyPrice"):
            with sqlite3.connect("CarRentDB.db") as con:
                cur = con.cursor()
                query = f"UPDATE Vehicle SET DailyPrice='{valueToUpdate}' WHERE RegNumber={id}"
                print(query)
                cur.execute(query)
                con.commit()
                msg = "Vehicle successfully Updated"
    except:
        con.rollback()
        msg = "We can not update vehicle to the list"
    finally:
        return msg
        con.close()

if __name__ == "__main__":
    app.run(debug=True)