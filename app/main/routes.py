from app.main import bp
from flask import render_template

images = {
    'bg':'static/img/bg.jpg',
    'project_1': 'static/img/projects/1.jpg',
    'project_2': 'img/projects/2.jpg',
    'project_1': 'img/projects/3.jpg',
    'project_2': 'img/projects/4.jpg',
}

@bp.route('/index',methods=['GET','POST'])
@bp.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html', title='Home', images=images)