from flask import request, jsonify, Blueprint
from flask import current_app as app
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, jwt_required, get_current_user
# Import standard Config for Seeding
from env_config import ProductionConfig
# Import supporting models
from models.fun_db import fun_db
# Import RestPlus for API Documentation
from flask_restplus import fields, Resource, Namespace, Api
import logging


# User Namespace
api = Namespace('system', description='System related operations')



# Database and PWD
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

ns_system_db_param = api.model("Database",
                                 {
                                     "element": fields.String(description="Element Name ", required=True),
                                     "element_value": fields.String(description="Element Value ", required=True)})


@api.route('/db/<col_name>')
class system_db_name(Resource):
    @api.expect()
    @api.doc()
    def get(selfs,col_name):
        db = fun_db()
        __results__ = db.db_get_content(col_name)
        return jsonify(__results__)

    @api.expect(ns_system_db_param)
    @api.doc(ns_system_db_param)
    def post(self,col_name):
        db = fun_db()
        __info__ = request.get_json()
        __info__["col_name"] = col_name
        __results__ = db.db_update_content(__info__)
        return jsonify(__results__)

    @api.expect()
    @api.doc()
    def delete(self, col_name):
        db = fun_db()
        __seed__ = ProductionConfig
        __info__ = {'col_name': col_name }
        __results__ = db.db_collection_drop(__seed__,__info__)
        return jsonify(__results__)
