
from flask_sqlalchemy import create_engine


DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(root,lennon,localhost,3306,lennon)
engine = create_engine(DB_URI)