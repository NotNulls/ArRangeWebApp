from app.main import bp
from flask import render_template, request
from app.email import send_email
from app.forms import ContactForm
from flask import flash

images = {
    'bg': 'static/img/bg.jpg',
    'project_1': 'static/img/projects/1.jpg',
    'project_2': 'img/projects/2.jpg',
    'project_1': 'img/projects/3.jpg',
    'project_2': 'img/projects/4.jpg',
}


@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home', images=images) or 404


@bp.route('/about', methods=['GET', 'POST'])
def about_us():
    return render_template('about.html', title='About us') or 404


@bp.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    return render_template('portfolio.html', title='Portfolio') or 404


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm

    if request.method == "POST":
        if form.validate_on_submit():
            data = request.form
            print(data)
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
            send_email(data["name"], data["email"], data["subject"], data["message"])
            flash('Thank you for submitting your message!')
    return render_template('contact.html', title='Contact', form=form) or 404

