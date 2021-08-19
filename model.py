#from flask import Flask, jsonify, request
#from sqlalchemy import BigInteger, Column, JSON, Text, engine, Integer, String, Date
#from sqlalchemy.sql import base
#from sqlalchemy.sql.schema import MetaData
##from sqlalchemy.sql.sqltypes import TIMESTAMP
#from app import db
#from sqlalchemy.dialects.postgresql import JSON
#import psycopg2
#from datetime import datetime
#from sqlalchemy import create_engine, Column, Integer, String, Date, MetaData
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import create_engine
        
"""    if request.method == 'POST':
        lt_rating = request.form['lt_rating']

        learningtheory = LearningTheory(lt_id, lt_rating)
        Base.session.add(LearningTheory)
        Base.session.commit()


class Cognitive(Base):
    __tablename__='cognition'
    user_id=Base.Column(Base.Integer, primary_key=True)
    cog_id=Base.Column(Base.Integer)
    cog_rating=Base.Column(Base.Integer)
    TIMESTAMP=Base.Column(Date)

def __init__(self, cog_id, cog_rating):
    self.cog_rating=cog_rating

    if request.method == 'POST':
        cog_rating = request.form['cog_rating']

        cognition = Cognitive(cog_id, cog_rating)
        Base.session.add(Cognitive)
        Base.session.commit()


class studyTime(Base):
    __tablename__='studytime'
    user_id=Base.Column(Base.Integer, primary_key=True)
    studytime=Base.Column(Base.Integer)
    studytime_rating=Base.Column(Base.Integer)
    TIMESTAMP=Base.Column(datetime)

    def __init__(self, studytime, studytime_rating):
        self.studytime=studytime
        self.studytime_rating=studytime_rating

        if request.method == 'POST':
            studytime = request.form['studytime']
            studytime_rating= request.form['studytimerating']

            studytime = studyTime(studytime, studytime_rating)
            Base.session.add(studyTime)
            Base.session.commit() """
