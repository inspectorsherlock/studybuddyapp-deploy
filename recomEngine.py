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
from sqlalchemy.pool import NullPool
from sqlalchemy import create_engine
import random
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfTransformer


'''def predict(df):
    ratings = spark.createDataFrame(df, ['user_id', 'lt_id', 'lt_rating'] )
    #wk1_df = pd.DataFrame(wk1_data, columns=['user_id', 'lt_id', 'lt_rating', 'cog_id', 'cog_rating', 'studyduration', 'studyduration_rating', 'week_no', 'comment', 'TIMESTAMP'])
    wk1_df = wk1_df[['user_id', 'lt_id', 'lt_rating']]
    train_data,test_data = wk1_df.randomSplit([0.7, 0.3])
    recommender = ALS(maxIter=5, regParam=0.01, userCol='user_id', itemCol='lt_id', ratingCol='lt_rating', coldStartStrategy="drop")
    model=recommender.fit(train_data)
    pred_data=model.transform(test_data)
    wk1_df_lt_title = db.session.execute('SELECT * FROM learningtheorytitle')
    wk1_df_lt_title = pd.DataFrame(wk1_df_lt_title)
    userRecs= model.recommendForAllUsers(10) #Generate top 10 learning theory recommendations for each user
    userRecsExplode= userRecs.select(userRecs.user_id,f.explode(userRecs.recommendations)).orderBy(userRecs.userId)
    ltheory_recs=model.recommendForAllItems(10) #Generate top 10 user recommendation for each learning theory
    ltheory_recs.join(wk1_df_lt_title, ltheory_recs.lt_id==wk1_df_lt_title.lt_id,"left").select([ltheory_recs.lt_id,wk1_df_lt_title.learningtheorytitle,ltheory_recs.recommendations])
    ltheory_recsExplode=ltheory_recs.select(ltheory_recs.lt_id,f.explode(ltheory_recs.recommendations)).orderBy(ltheory_recs.lt_id)
    ltheory_recsExplode.join(wk1_df_lt_title,ltheory_recsExplode.lt_id==wk1_df_lt_title.lt_id,"left").select([ltheory_recsExplode.lt_id, wk1_df_lt_title.learningtheorytitle, ltheory_recsExplode.col.alias('recommendation')]).show()
    return render_template('self mo.html', prediction=ltheory_recsExplode)'''