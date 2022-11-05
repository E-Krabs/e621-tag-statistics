from flask import Flask, render_template
from app_init import *
app = Flask(__name__)


date_tag_frequency('monthly')
row_lst, tags = date_tag_count()


@app.route('/')
def home():
	return render_template('index.htm', tags=tags, rows=row_lst)
