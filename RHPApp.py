from flask import Flask,session,redirect, url_for,request,render_template,jsonify  #pip install flask
from datetime import timedelta
import os
import pandas as pd
import numpy as np
import sub_area as sa
import pre2
import math
import ml_extra_tree_


#######
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)
###以上為必須，下方自由發揮

#https://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/ML2')
def ML2():
    return render_template('ML.html')

@app.route('/ML', methods=['POST'])
def ML():
    sub_area_id = request.form.get("sub_area_id")
    sub_area = int(sa.Sa(sub_area_id))
    workplaces_km = request.form.get("workplaces_km")
    workplaces_km=float(workplaces_km)
    area_m = float(request.form.get("area_m"))
    nuclear_reactor_km= float(request.form.get("nuclear_reactor_km"))
    catering_km= float(request.form.get("catering_km"))
    mosque_km= float(request.form.get("mosque_km"))
    feature6=[workplaces_km, area_m, nuclear_reactor_km, sub_area, catering_km, mosque_km]
    feature66=[]
    for f in feature6:
        if f == 0:
            f= 0.1
        feature66.append(np.log(f))
#        print(type(f))
    result = ml_extra_tree_.load_variables(feature66)
#    session['result'] = result
#    session['area'] = sub_area_id
    result = result[0]
    print(type(result),type(sub_area))
#    return redirect(url_for('conclusion'))
    return render_template('conclusion.html',result=[result,sub_area])



########
@app.route('/conclusion')
def conclusion():
    return render_template('conclusion.html')



###以下為必須，上方自由發揮
if __name__ =="__main__":
    app.debug = True
    app.run()