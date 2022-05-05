from flask import Blueprint, render_template

router = Blueprint('router', __name__)


@router.route('/')
def index():
    return render_template('pages/index.html')
