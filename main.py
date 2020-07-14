from flask import *
from flask_bootstrap import Bootstrap
from app import create_app

def webserver():
    app=create_app()

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__=='__main__':
    app=webserver()
    app.run()