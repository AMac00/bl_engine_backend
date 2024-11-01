# Import main backend application
from bl_engine_main import app


# This file provides the WSGI fork.

if __name__ == "__main__":
    app.run()
