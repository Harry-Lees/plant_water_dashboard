from flask_sqlalchemy import SQLAlchemy

engine = SQLAlchemy()
Session = SQLAlchemy.sessionmaker(bind=engine)
session = Session()