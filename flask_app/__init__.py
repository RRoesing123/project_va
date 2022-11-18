from flask import Flask, render_template, request, redirect, session, flash
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'slkdfjsldkfjsldkfjlsdkfjlsdkfj'