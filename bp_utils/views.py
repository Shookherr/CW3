from flask import Blueprint, render_template, request
import utils

POSTS_JSON = 'data/posts.json'          # путь к файлу с постами
COMMENTS_JSON = 'data/comments.json'    # путь к файлу с постами
LIM = 50                                # ограничение отображения укороченного поста в символах

bp_utils = Blueprint('bp_utils', __name__)


@bp_utils.route("/")
def view_all_posts():
    posts = utils.load_all_posts(POSTS_JSON, LIM)  # с ограничением, несколько корявенько, но через шаблон и css не смог
    return render_template('index.html', posts=posts)


@bp_utils.route("/<int:pk>")
def view_post(pk):
    post = utils.load_post(pk, POSTS_JSON)
    comments = utils.load_comments_pk(pk, COMMENTS_JSON)
    return render_template('post.html', post=post, comments=comments, numb_comm=len(comments))


@bp_utils.route("/search")
def search_post():
    str_search = request.args.get('s', '')
    post = utils.filter_str_posts(utils.load_all_posts(POSTS_JSON), 'content', str_search)
    return render_template('index.html', posts=post)


@bp_utils.route("/user/<user_name>")
def search_user_post(user_name):
    post = utils.filter_str_posts(utils.load_all_posts(POSTS_JSON, LIM), 'poster_name', user_name)
    return render_template('index.html', posts=post)
