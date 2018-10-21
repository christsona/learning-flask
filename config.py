from peewee import *

my_sql = MySQLDatabase("christsona", host="71.31.30.32", port=5000, user="christsona", password="XiAxhk6pbzB5zSL8")
# my_sql = MySQLDatabase("christsona", host="localhost", user="christsona", passwd="XiAxhk6pbzB5zSL8")
class DynamicModel(Model):
    class Meta:
        database = my_sql
