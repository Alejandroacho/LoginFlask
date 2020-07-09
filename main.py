from flask import Flask

def webserver():
    app = Flask(__name__)

    @app.route('/')
    def index():
        message='Hola mundo'
        return message
    
    return app

if __name__=='__main__':
    app=webserver()
    app.run()