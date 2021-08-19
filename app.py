from enum import unique
from operator import methodcaller
from flask import Flask, render_template, request, jsonify, json, redirect, url_for
from wtforms import Form
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import BigInteger, Column, JSON, Text, engine, Integer, String, DateTime, Table, ForeignKey
import pandas as pd
from pandas import DataFrame
import numpy as np
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import functions as f
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark import SparkConf, SparkContext
from pyspark.sql.dataframe import DataFrame
from sqlalchemy.sql.sqltypes import TIMESTAMP, Time
from sqlalchemy import create_engine
import random
import psycopg2
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time
import datetime
from flask.ext.heroku import Heroku


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Smartmind1920@localhost/flasksql'
app.debug=True
heroku= Heroku(app)
db = SQLAlchemy(app)
#spark = SparkSession.builder.master("local").appName("ALS Reco").getOrCreate()
#metadata = MetaData()
#DATABASEURI="postgresql+psycopg2://postgres:Smartmind1920@localhost/flasksql"
#engine= create_engine(DATABASEURI)
#Base= declarative_base()

class selfstudy(db.Model):
    __tablename__='selfstudy'
    index=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, unique=False)
    lt_id=db.Column(db.Integer, ForeignKey('learningtheorytitle.lt_id'))
    lt_rating=db.Column(db.Integer)
    cog_id=db.Column(db.Integer, ForeignKey('cognitiontheorytitle.cog_id'))
    cog_rating=db.Column(db.Integer)
    studyduration=db.Column(db.Integer)
    studyduration_rating=db.Column(db.Integer)
    week_no=db.Column(db.Integer, nullable=False)
    comment=db.Column(db.String(500), nullable=False)

    def __init__(self, user_id, lt_id, lt_rating, cog_id, cog_rating, studyduration, studyduration_rating, week_no, comment):
        self.user_id=user_id
        self.lt_id=lt_id
        self.lt_rating=lt_rating
        self.cog_id=cog_id
        self.cog_rating=cog_rating
        self.studyduration=studyduration
        self.studyduration_rating=studyduration_rating
        self.week_no=week_no
        self.comment=comment

class class_cog(db.Model):
    __tablename__='classcognition'
    index=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, unique=False)
    classcog_id=db.Column(db.Integer, ForeignKey('cognitiontheorytitle.cog_id'))
    classcog_rating=db.Column(db.Integer)
    week_no=db.Column(db.Integer, nullable=False)
    worksheet_percentage=db.Column(db.Integer, nullable=False)
    class_comment=db.Column(db.String(1000), nullable=False)

    def __init__(self, user_id, classcog_id, classcog_rating, week_no, worksheet_percentage, class_comment):
        self.user_id=user_id
        self.classcog_id=classcog_id
        self.classcog_rating=classcog_rating
        self.week_no=week_no
        self.worksheet_percentage=worksheet_percentage
        self.class_comment=class_comment

class learningtheorytitle(db.Model):
    lt_id=db.Column(db.Integer, primary_key=True, nullable=False)
    learningtheorytitle=db.Column(db.String(100), nullable=False)
    
    def __init__(self, lt_id, learningtheorytitle):
        self.lt_id=lt_id
        self.learningtheorytitle=learningtheorytitle
        
class cognitiontheorytitle(db.Model):
    cog_id=db.Column(db.Integer, primary_key=True, nullable=False)
    cognitiontitle=db.Column(db.String(100), nullable=False)

    def __init__(self, cog_id, cognitiontitle):
        self.cog_id=cog_id
        self.cognitiontitle=cognitiontitle

@app.route('/templates/index.html', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/templates/lets get started.html')
def lgs():
    return render_template('lets get started.html')

@app.route('/templates/templates/lecture.html')
def lecture():
    return render_template('lecture.html')

@app.route('/templates/templates/self-study.html')
def self_study():
    return render_template('self-study.html')

@app.route('/templates/templates/lecture mo.html')
def lecture_mo():
    return render_template('lecture mo.html')

@app.route('/templates/templates/lecture stereochemistry.html')
def lecture_stereochemistry():
    return render_template('lecture stereochemistry.html')

@app.route('/templates/templates/lecture mechanisms.html')
def lecture_mechanisms():
    return render_template('lecture mechanisms.html')

@app.route('/templates/templates/lecture alkenes & alkynes.html')
def lecture_reactions():
    return render_template('lecture alkenes & alkynes.html')

@app.route('/templates/templates/self-mo.html')
def self_mo():
    return render_template('self-mo.html')

@app.route('/templates/templates/self-stereochemistry.html')
def self_stereochemistry():
    return render_template('self-stereochemistry.html')

@app.route('/templates/templates/self-mechanisms.html')
def self_mechanisms():
    return render_template('self-mechanisms.html')

@app.route('/templates/templates/self-alkenes & alkynes.html')
def self_reactions():
    return render_template('self-alkenes & alkynes.html')


@app.route('/templates/templates/lecture mo.html', methods=['GET', 'POST'])
def lecture1():
    if request.method == 'POST':
        user_id=request.form['user_id']
        classcog_id=request.form['classcog_id']
        classcog_rating=request.form['classcog_rating']
        week_no=request.form['classweek_no']
        worksheet_percentage=request.form['worksheet_percentage']
        class_comment=request.form['class_comment']

        classcognition=class_cog(user_id, classcog_id, classcog_rating, week_no, worksheet_percentage, class_comment)
        db.session.add(classcognition)
        db.session.commit() 

        return render_template('lecture mo.html')


@app.route('/templates/templates/lecture stereochemistry.html', methods=['GET', 'POST'])
def lecture2():
    if request.method == 'POST':
        user_id=request.form['user_id']
        classcog_id=request.form['classcog_id']
        classcog_rating=request.form['classcog_rating']
        week_no=request.form['classweek_no']
        worksheet_percentage=request.form['worksheet_percentage']
        class_comment=request.form['class_comment']

        classcognition=class_cog(user_id, classcog_id, classcog_rating, week_no, worksheet_percentage, class_comment)
        db.session.add(classcognition)
        db.session.commit() 

        return render_template('lecture stereochemistry.html')


@app.route('/templates/templates/lecture mechanisms.html', methods=['GET', 'POST'])
def lecture3():
    if request.method == 'POST':
        user_id=request.form['user_id']
        classcog_id=request.form['classcog_id']
        classcog_rating=request.form['classcog_rating']
        week_no=request.form['classweek_no']
        worksheet_percentage=request.form['worksheet_percentage']
        class_comment=request.form['class_comment']

        classcognition=class_cog(user_id, classcog_id, classcog_rating, week_no, worksheet_percentage, class_comment)
        db.session.add(classcognition)
        db.session.commit() 

        return render_template('lecture mechanisms.html')

@app.route('/templates/templates/lecture alkenes & alkynes.html', methods=['GET', 'POST'])
def lecture4():
    if request.method == 'POST':
        user_id=request.form['user_id']
        classcog_id=request.form['classcog_id']
        classcog_rating=request.form['classcog_rating']
        week_no=request.form['classweek_no']
        worksheet_percentage=request.form['worksheet_percentage']
        class_comment=request.form['class_comment']

        classcognition=class_cog(user_id, classcog_id, classcog_rating, week_no, worksheet_percentage, class_comment)
        db.session.add(classcognition)
        db.session.commit() 

        return render_template('lecture alkenes & alkynes.html')


@app.route('/templates/templates/self-mo.html', methods=['GET', 'POST'])
def selfstudy_mo(): #vary to change depending on html/react form submission buttons.
    if request.method == 'POST':
        user_id=request.form['user_id']
        lt_id = request.form['lt_id']
        lt_rating= request.form['lt_rating']
        cog_id= request.form['cog_id']
        cog_rating = request.form['cog_rating']
        studyduration=request.form['studytime']
        studyduration_rating=request.form['studytime_rating']
        week_no=request.form['week_no']
        comment=request.form['comment']

        selfStudy=selfstudy(user_id, lt_id, lt_rating, cog_id, cog_rating, studyduration, studyduration_rating, week_no, comment)
        db.session.add(selfStudy)
        db.session.commit()

        return render_template("self-mo.html")

@app.route('/templates/templates/self-stereochemistry.html', methods=['GET', 'POST'])
def selfstudy_stereochemistry(): #vary to change depending on html/react form submission buttons.
    if request.method == 'POST':
        user_id=request.form['user_id']
        lt_id = request.form['lt_id']
        lt_rating= request.form['lt_rating']
        cog_id= request.form['cog_id']
        cog_rating = request.form['cog_rating']
        studyduration=request.form['studytime']
        studyduration_rating=request.form['studytime_rating']
        week_no=request.form['week_no']
        comment=request.form['comment']

        selfStudy=selfstudy(user_id, lt_id, lt_rating, cog_id, cog_rating, studyduration, studyduration_rating, week_no, comment)
        db.session.add(selfStudy)
        db.session.commit()

        return render_template("self-stereochemistry.html")

@app.route('/templates/templates/self-mechanisms.html', methods=['GET', 'POST'])
def selfstudy_mechanisms(): #vary to change depending on html/react form submission buttons.
    if request.method == 'POST':
        user_id=request.form['user_id']
        lt_id = request.form['lt_id']
        lt_rating= request.form['lt_rating']
        cog_id= request.form['cog_id']
        cog_rating = request.form['cog_rating']
        studyduration=request.form['studytime']
        studyduration_rating=request.form['studytime_rating']
        week_no=request.form['week_no']
        comment=request.form['comment']

        selfStudy=selfstudy(user_id, lt_id, lt_rating, cog_id, cog_rating, studyduration, studyduration_rating, week_no, comment)
        db.session.add(selfStudy)
        db.session.commit()

        return render_template("self-mechanisms.html")

@app.route('/templates/templates/self-alkenes & alkynes.html', methods=['GET', 'POST'])
def selfstudy_alkenes_alkynes(): #vary to change depending on html/react form submission buttons.
    if request.method == 'POST':
        user_id=request.form['user_id']
        lt_id = request.form['lt_id']
        lt_rating= request.form['lt_rating']
        cog_id= request.form['cog_id']
        cog_rating = request.form['cog_rating']
        studyduration=request.form['studytime']
        studyduration_rating=request.form['studytime_rating']
        week_no=request.form['week_no']
        comment=request.form['comment']

        selfStudy=selfstudy(user_id, lt_id, lt_rating, cog_id, cog_rating, studyduration, studyduration_rating, week_no, comment)
        db.session.add(selfStudy)
        db.session.commit()

        return render_template("self-alkenes & alkynes.html")

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)
