from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import functions as f
import psycopg2
from sqlalchemy import create_engine
import pandas as pd 
import getpass
from pandas import DataFrame


