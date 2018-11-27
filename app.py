from models import t_shop
from model import Shop, Brand
from geomodel import Shop1, Brand1
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:chaudary007@localhost/test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:chaudary007@localhost/db_shop'
db = SQLAlchemy(app)
db.create_all()
db.session.commit()


'''def sql(rawSql, sqlVars={}):
 "Execute raw sql, optionally with prepared query"
 assert type(rawSql)==str
 assert type(sqlVars)==dict
 res=db.session.execute(rawSql, sqlVars)
 db.session.commit()
 return res'''




@app.route('/')
def main():
    return render_template('index.html')
    #return render_template('map.html')

@app.route('/turfe1')
def turfe1():
    return render_template('turfExample1.html')

@app.route('/turfe2')
def turfe2():
    return render_template('turfExample2.html')

@app.route('/turfgeoJson')
def turfgeoJson():
    return render_template('mapturfgeoJson.html')

@app.route('/turfLeaflet')
def turfLeaflet():
    return render_template('turfLeaflet.html')

@app.route('/turfLeafletv2')
def turfLeafletv2():
    return render_template('turfLeafletv2.html')

@app.route('/turfLeafletv3')
def turfLeafletv3():
    return render_template('turfLeafletv3.html')


@app.route('/turfSample')
def turfSample():
    return render_template('turfSample.html')


#Previous Data Ok
'''
@app.route('/data')
def data():
    myshop = db.session.query(t_shop).all()
    return jsonify(myshop)
'''

@app.route('/data')
def data():
    myshop = db.session.query(t_shop).all()
    all_shop = [{'shop': t_shop.shop, 'brand': t_shop.brand, 'address': t_shop.address, 'latitude': t_shop.latitude, 'longitude': t_shop.longitude} for t_shop in myshop]
    return jsonify(all_shop)

@app.route('/datav2')
def datav2():
    myshop = db.session.query(Shop).all()
    all_shop = [{'shop': Shop.shop, 'brand': Shop.brand, 'address': Shop.address, 'latitude': Shop.latitude, 'longitude': Shop.longitude, 'id': Shop.id, 'brand_id': Shop.brand_id} for Shop in myshop]
    return jsonify(all_shop)

@app.route('/brand')
def brand():
    mybrand = db.session.query(Brand).all()
    all_brand = [{'brand': Brand.name} for Brand in mybrand]
    return jsonify(all_brand)

'''
@app.route('/data')
def data():
    myshop = db.session.query(t_shop).all()
    all_shop = [{'shop': t_shop.shop, 'brand': t_shop.brand, 'address': t_shop.address, 'latitude': t_shop.latitude, 'longitude': t_shop.longitude} for t_shop in myshop]
    return jsonify(all_shop)
'''

'''@app.route("/brand")
def brand():
 shops = sql("SELECT * FROM shop;")
 return render_template("shopdata.html", shops=shops)
 '''

@app.route('/check')
def check():
    return render_template('check.html')

@app.route('/mapbox')
def mapbox():
    return render_template('mapbox.html')

@app.route('/mapfilterv2')
def mapfilterv2():
    return render_template('mapfilterv2.html')

@app.route('/mapfilterv3')
def mapfilterv3():
    return render_template('mapfilterv3.html')

@app.route('/maplf')
def maplf():
    return render_template('maplf.html')

@app.route('/mapfilterfinal')
def mapfilterfinal():
    return render_template('mapfilterfinal.html')

@app.route('/mapfinalpk')
def mapfinalpk():
    return render_template('mapfinalpk.html')

@app.route('/mapcircle')
def mapcircle():
    return render_template('mapcircle.html')

@app.route('/mapcirclev2')
def mapcirclev2():
    return render_template('mapcirclev2.html')

@app.route('/mapcirclev3')
def mapcirclev3():
    return render_template('mapcirclev3.html')

@app.route('/mapcirclev4')
def mapcirclev4():
    return render_template('mapcirclev4.html')

@app.route('/mapfinalzoom')
def mapfinalzoom():
    return render_template('mapfinalzoom.html')

@app.route('/mapfinalgis')
def mapfinalgis():
    return render_template('mapfinalgis.html')

@app.route('/mapall')
def mapall():
    return render_template('mapall.html')

@app.route('/mapfilter')
def mapfilter():
    return render_template('mapfilter.html')

@app.route('/base')
def base():
    myshop = db.session.query(t_shop).all()
    return render_template('base.html', myshop=myshop)

@app.route('/map')
def map():
    return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True)

# Previous code
'''
@app.route('/')
def index():
    myShop = shop.query.all()
    return render_template('add_shop.html', myShop=myShop)

@app.route('/post_shop', methods=['POST'])
def post_shop():
    shop = shop(request.form['shop'], request.form['brand'], request.form['address'], request.form['lat'], request.form['long'])
    db.session.add(shop)
    db.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
'''