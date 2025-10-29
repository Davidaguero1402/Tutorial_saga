import os
from flask import Flask
from app.config import config



def create_app() -> None:
    config_name = os.getenv('FLASK_ENV')
    app = Flask(__name__)
    f = config.factory(config_name if config_name else 'development')
    app.config.from_object(f)
    f.init_app(app)

    
    from app.resource.router_action import accion_bp
    app.register_blueprint(accion_bp, url_prefix='/ms_uno')
   
    @app.shell_context_processor    
    def ctx():
        return {
            "app": app
            }
    
    return app