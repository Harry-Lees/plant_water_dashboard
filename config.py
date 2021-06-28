class Config:
    # Debug mode
    DEBUG: bool = False

    # Database setup
    SQLALCHEMY_DATABASE_URI: str = 'postgresql://postgres:password@localhost/postgres'
    SQLALCHEMY_ECHO: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # User Config
    GRAPH_LENGTH: int = 30
    DRYNESS_THRESHOLD: float = 2.0