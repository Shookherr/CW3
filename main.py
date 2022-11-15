# Курсовая работа #3. Шумихин Алексей. 15.11.2022
from flask import Flask, render_template, jsonify, request

import utils, logger

POSTS_JSON = 'data/posts.json'  # путь к файлу с постами
COMMENTS_JSON = 'data/comments.json'  # путь к файлу с постами

app = Flask(__name__)


@app.route("/")
def view_all_posts():
    posts = utils.load_all_posts(POSTS_JSON)
    return render_template('index.html', posts=posts)


@app.route("/<int:pk>")
def view_post(pk):
    post = utils.load_post(pk, POSTS_JSON)
    comments = utils.load_comments_pk(pk, COMMENTS_JSON)
    return render_template('post.html', post=post, comments=comments, numb_comm=len(comments))


@app.route("/search")
def search_post():
    str_search = request.args.get('s', '')
    post = utils.filter_str_posts(utils.load_all_posts(POSTS_JSON), 'content', str_search)
    return render_template('index.html', posts=post)


@app.route("/user/<user_name>")
def search_user_post(user_name):
    post = utils.filter_str_posts(utils.load_all_posts(POSTS_JSON), 'poster_name', user_name)
    return render_template('index.html', posts=post)


log = logger.get_logger('main')


@app.route("/api")
def api_all_posts():
    posts = utils.load_all_posts(POSTS_JSON)
    log.info(f'api_all_posts - > {len(posts)}')
    return jsonify(posts)


@app.route("/api/<int:pk>")
def api_view_post(pk):
    post = utils.load_post(pk, POSTS_JSON)
    log.info(f'api_view_post - > {pk}')
    return jsonify(post)


@app.errorhandler(404)
def page_not_found(e):
    return 'Страница отсутствует'


@app.errorhandler(500)
def server_error(e):
    return 'Ошибка со стороны сервера'


if __name__ == "__main__":
    app.run()