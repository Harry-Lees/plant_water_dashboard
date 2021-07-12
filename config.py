from os import getenv

class Config:
    # Debug mode
    DEBUG: bool = False

    # Database setup
    SQLALCHEMY_DATABASE_URI: str = getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # User Config
    GRAPH_LENGTH: int = 30
    DRYNESS_THRESHOLD: float = 2.0

    SECRET_KEY: str = getenv('SECRET_KEY') or '12345'