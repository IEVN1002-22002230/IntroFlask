from flask_mysqldb import MySQL  

mysql = MySQL()

def registrar_blueprints(app):
    from blueprints.alumnos.routes import alumnos_bp
    from blueprints.maestros.routes import maestros_bp
    
    app.register_blueprint(alumnos_bp)
    app.register_blueprint(maestros_bp)