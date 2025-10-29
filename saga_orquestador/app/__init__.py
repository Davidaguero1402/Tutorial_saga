# saga_orquestador/app/__init__.py
from flask import Flask, jsonify
import os
from app.config import config

def create_app():
    app_context = os.getenv('FLASK_CONTEXT')
    app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development')
    app.config.from_object(f)
    
    from app.resource.saga_router import saga_bp

    app.register_blueprint(saga_bp, url_prefix='/saga')
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    @app.errorhandler(429)
    def too_many_request(error):
        return jsonify({'msg':'Too many requests'}), 429

    return app