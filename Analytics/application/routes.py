from application.models import (GCC,COLL,Result)
from application import app
from flask import render_template, request
from flask import url_for
from application.email import send_email
from config import ADMINS


from flask_paginate import Pagination, get_page_parameter
def CallData():
    from sqlalchemy import select
    from sqlalchemy import create_engine
    engine = create_engine(
        "mysql+pymysql://kubak182:hellas123@localhost/PythonTutorial",
    )
    with engine.connect() as conn:
        result = conn.execute(select([GCC])).fetchall()
        result2 = conn.execute(select([COLL])).fetchall()

    return result, result2

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')




@app.route('/monitor')
def monitor():
    from application.report import Report

    if request.args.get('analyse', None)=='Monitor':
        data = CallData()
        a = Report(data[0], data[1])
        a.Monitoring()
        from datetime import datetime
        gra = Result.query.order_by("total desc").filter(Result.total>=100).all()
        send_email('Monitoring',ADMINS[0],ADMINS,render_template('email.html', date=datetime.now(),gra=gra))


    graph =None
    stats= [0,0]


    page = request.args.get(get_page_parameter(), type=int, default=1)

    pagination = Pagination(css_framework='bootstrap4', page=page, total=Result.query.count(), search=False,
                            record_name='Ingot', stats=stats)
    id_ = request.args.get('nxgrapx', None)
    if id_ is not None:
        data = CallData()
        a = Report(data[0], data[1])
        stats = a.PrintGraph((int(id_) - 1))
        graph = True


    return render_template('monitor.html',stats=stats ,gra=Result.query.order_by("total desc").limit(10).offset((page-1)*10).all(),pagination=pagination,page=page, graph=graph,nxgrapx=None)
