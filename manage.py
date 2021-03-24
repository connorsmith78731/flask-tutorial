import os
import sys
from flask import Flask
from flaskr import create_app
if __name__ == "__main__":
    app = create_app()
    app.run()
