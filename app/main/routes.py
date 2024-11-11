from app.main import bp
from flask import render_template, request, flash, redirect, url_for
from app.email import send_email
from app.forms import ContactForm


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
    form = ContactForm()

    if request.method == "POST":
        if form.validate_on_submit():
            name = request.form['name']
            email = request.form.get('email')
            message = request.form['message']
            recipients = ""
            html_body = f"<p>{message}</p>"
            print('\n<-----------------------', name, email, message, html_body)
            send_email(
                subject=name,
                sender=email,
                html_body=html_body,
                recipients=["di.ar.34@gmail.com"],
                text_body=message)

            flash('Thank you for submitting your message!')
            print(name, email, recipients, message, html_body)
            return redirect(url_for('main.contact'))
    return render_template('contact.html', title='Contact', form=form) or 404
