from flask import Blueprint

app_code_clone = Blueprint(
'app_code_clone',
__name__,
template_folder='templates',
static_folder='static',
static_url_path='/app_code_clone/static'
)

from app_code_clone import views
