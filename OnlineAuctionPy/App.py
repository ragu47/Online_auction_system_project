from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
import mysql.connector

import base64, os

app = Flask(__name__)
app.secret_key = 'a'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/AdminLogin')
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route('/UserLogin')
def UserLogin():
    return render_template('UserLogin.html')


@app.route('/NewUser')
def NewUser():
    return render_template('NewUser.html')


@app.route('/SellerLogin')
def SellerLogin():
    return render_template('SellerLogin.html')


@app.route('/NewSeller')
def NewSeller():
    return render_template('NewSeller.html')


@app.route('/NewProduct')
def NewProduct():
    return render_template('NewProduct.html')


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            return render_template('AdminHome.html', data=data)

        else:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)


@app.route('/AdminHome')
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/newproduct", methods=['GET', 'POST'])
def newproduct():
    if request.method == 'POST':
        file = request.files['file']
        file.save("static/upload/" + file.filename)
        pname = request.form['pname']
        ptype = request.form['ptype']
        Price = request.form['Price']
        info = request.form['info']
        ldate = request.form['ldate']
        # file = request.form['file']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO protb VALUES ('','" + pname + "','" + ptype + "','" + Price + "','" + info + "','" + ldate + "','" + file.filename + "','waiting','" +
            session['uname'] + "')")
        conn.commit()
        conn.close()

        alert = 'Record Saved!'
        return render_template('goback.html', data=alert)


@app.route('/ProductInfo')
def ProductInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb ")
    data = cur.fetchall()
    return render_template('ProductInfo.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        uname = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "')")
        conn.commit()
        conn.close()

        alert = 'Record Saved!'
        return render_template('goback.html', data=alert)


@app.route("/newuseller", methods=['GET', 'POST'])
def newuseller():
    if request.method == 'POST':
        uname = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sellertb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "')")
        conn.commit()
        conn.close()

        alert = 'Record Saved!'
        return render_template('goback.html', data=alert)


@app.route("/sellerlogin", methods=['GET', 'POST'])
def sellerlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from sellertb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)
        else:
            session['mob'] = data[2]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM sellertb where username='" + session['uname'] + "'")
            data1 = cur.fetchall()
            return render_template('SellerHome.html', data=data1)


@app.route('/SellerHome')
def SellerHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM sellertb where username='" + session['uname'] + "'")
    data1 = cur.fetchall()
    return render_template('SellerHome.html', data=data1)


@app.route('/SProductInfo')
def SProductInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb where SellerName='" + session['uname'] + "'")
    data1 = cur.fetchall()
    return render_template('SProductInfo.html', data=data1)


@app.route("/Remove")
def Remove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cursor = conn.cursor()
    cursor.execute(
        "delete from protb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Product  info Remove Successfully!')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb where SellerName='" + session['uname'] + "' ")
    data = cur.fetchall()
    return render_template('SProductInfo.html', data=data)


@app.route("/Remove1")
def Remove1():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cursor = conn.cursor()
    cursor.execute(
        "delete from protb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Product  info Remove Successfully!')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  ")
    data = cur.fetchall()
    return render_template('ProductInfo.html', data=data)


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "' ")
        data = cursor.fetchone()
        if data is None:

            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)

        else:
            session['mob'] = data[2]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + session['uname'] + "'")
            data1 = cur.fetchall()
            return render_template('UserHome.html', data=data1)


@app.route('/UserHome')
def UserHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where username='" + session['uname'] + "'")
    data1 = cur.fetchall()
    return render_template('UserHome.html', data=data1)


@app.route('/Search')
def Search():
    import datetime

    date = datetime.datetime.now().strftime('%Y-%m-%d')
    print(date)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb where Status='waiting' and  LastDate >='" + date + "' ")
    data1 = cur.fetchall()
    return render_template('Search.html', data=data1)


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        ptype = request.form['ptype']
        import datetime

        date = datetime.datetime.now().strftime('%Y-%m-%d')
        print(date)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM protb where ProductType like '%" + ptype + "%' and LastDate >='" + date + "' and Status='waiting' ")
        data1 = cur.fetchall()
        return render_template('Search.html', data=data1)


@app.route("/fullInfo", methods=['GET'])
def fullInfo():
    pid = request.args.get('pid')
    session['pid'] = pid
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb where id like '%" + pid + "%'  ")
    data1 = cur.fetchall()
    return render_template('FullInfo.html', data=data1)


# amount


@app.route("/amount", methods=['GET', 'POST'])
def amount():
    if request.method == 'POST':
        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')

        pid = session['pid']
        uname = session['uname']
        amount = request.form['amount']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM protb  where  id='" + pid + "'")
        data = cursor.fetchone()

        if data:
            ProductName = data[1]
            Producttype = data[2]
            price = data[3]

            Image = data[6]
            sname = data[8]

        else:
            return 'No Record Found!'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO booktb VALUES ('','" + uname + "','" + session['mob'] + "','" + pid + "','" + str(
                ProductName) + "','" + str(price) + "','" + str(amount) + "','" +
            Image + "','" + date + "','waiting','" + sname + "')")
        conn.commit()
        conn.close()

        flash('Amount quotation   Successfully')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM booktb  where username='" + uname + "' ")
        data = cur.fetchall()
        return render_template('AuctionResult.html', data=data)


@app.route("/AuctionResult")
def AuctionResult():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where   username='" + uname + "' and Status='waiting' or Status='Reject'   ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where   username='" + uname + "' and Status='Select'   ")
    data1 = cur.fetchall()

    return render_template('AuctionResult.html', data=data, data1=data1)


@app.route("/AuctionInfo", methods=['GET'])
def AuctionInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where  Status='waiting'  ")
    data1 = cur.fetchall()
    return render_template('AuctionInfo.html', data=data1)


@app.route("/select", methods=['GET'])
def select():
    pid = request.args.get('pid')
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cursor = conn.cursor()
    cursor.execute(
        "update protb set Status='Close' where  id='" + pid + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cursor = conn.cursor()
    cursor.execute(
        "update booktb set Status='Select' where  id='" + id + "' ")
    conn.commit()

    conn.close()
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM booktb where  id='" + id + "'")
    data = cursor.fetchone()

    if data:
        mobile = data[2]
        unm = data[1]
        sendmsg(mobile, "Accept Your Quotation")


    else:
        return 'Incorrect username / password !'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cursor = conn.cursor()
    cursor.execute(
        "update booktb set Status='Reject' where  ProductId='" + pid + "' and id !='" + id + "'  ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM booktb where  ProductId='" + pid + "' and id !='" + id + "'")
    data1 = cursor.fetchall()
    for item1 in data1:
        mobile = str(item1[2])
        print(mobile)
        sendmsg(mobile, "Quotation Not Accept Select for" + str(unm))

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where  Status='waiting'  ")
    data1 = cur.fetchall()
    return render_template('AuctionInfo.html', data=data1)


def sendmsg(targetno, message):
    import requests
    requests.post(
        "http://smsserver9.creativepoint.in/api.php?username=fantasy&password=596692&to=" + targetno + "&from=FSSMSS&message=Dear user  your msg is " + message + " Sent By FSMSG FSSMSS&PEID=1501563800000030506&templateid=1507162882948811640")


@app.route("/pay", methods=['GET'])
def pay():
    id = request.args.get('id')

    amt = request.args.get('amt')

    session['payid'] = id

    return render_template('Payment.html', amt=amt)


@app.route("/ppayment", methods=['GET', 'POST'])
def ppayment():
    if request.method == 'POST':
        bid = session['payid']
        uname = session['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
        cursor = conn.cursor()
        cursor.execute(
            "update booktb set Status='Payment' where  id='" + bid + "'  ")
        conn.commit()
        conn.close()
        flash('Payment   Successfully')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM booktb where  Status='Payment' and username='" + uname + "' ")
        data1 = cur.fetchall()
        return render_template('PaymentInfo.html', data=data1)


@app.route("/PaymentInfo", methods=['GET', 'POST'])
def PaymentInfo():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where  Status='Payment' and username='" + uname + "' ")
    data1 = cur.fetchall()
    return render_template('PaymentInfo.html', data=data1)


@app.route("/Report", methods=['GET', 'POST'])
def Report():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where  Status='Payment'  ")
    data1 = cur.fetchall()
    return render_template('AdminReport.html', data=data1)


@app.route("/SReport", methods=['GET', 'POST'])
def SReport():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2onlineauctiondb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where  Status='Payment'  and SellerName='" + session['uname'] + "' ")
    data1 = cur.fetchall()
    return render_template('SReport.html', data=data1)


if __name__ == '__main__':
    # app.run(host='0.0.0.0',debug = True, port = 5000)
    app.run(debug=True, use_reloader=True)
