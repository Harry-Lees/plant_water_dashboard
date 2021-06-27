from app import create_app

__author__ = 'Harry Lees'
__credits__ = ['Harry Lees']

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')