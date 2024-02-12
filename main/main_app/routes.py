from flask import Blueprint, render_template, request
from main.models import Post

main_app = Blueprint('main', __name__)

@main_app.route("/")
@main_app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_published.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main_app.route("/about")
def about():
    return render_template('about.html', title='About')
