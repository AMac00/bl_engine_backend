from flask_restplus import Api, fields

# Import your API Views
from .bp_system import api as bp_system


api = Api(
    title='TTEC Business Logic Engine',
    version='1.0',
    description='A place to build TTEC Business Logic for use with Automation.',

)

# Application User API
bp_bl_param = api.model("Logging",
                                 {
                                     "offset_time": fields.String(description="Time of Logs to pull", required=True),
                                     "instant": fields.String(description="Pull files instantly", required=True),
                                     'applications': fields.String(description="['cucm','cvp','cvp-vxml']")})



# Add imports to API context
api.add_namespace(bp_system)