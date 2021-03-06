from flask import Blueprint, render_template, current_app
from flask_api.decorators import set_renderers
from flask_api.renderers import HTMLRenderer


blueprint = Blueprint('magic-page', __name__)


@blueprint.route("/magic")
@set_renderers(HTMLRenderer)
def get():
    return render_template(
        'magic.html',
        config=current_app.config
    )
