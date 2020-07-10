from flask import *
from flask_bootstrap import Bootstrap

def webserver():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['TEMPLATES_AUTO_RELOAD']=True
    bootstrap = Bootstrap(app)

    @app.route('/')
    def index():
        context={
            'user_ip':request.remote_addr
        }

        return render_template('index.html', **context)
    
    return app

if __name__=='__main__':
    app=webserver()
    app.run()