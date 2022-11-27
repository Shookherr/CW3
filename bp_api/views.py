from flask import Blueprint, jsonify
import logger
import utils

POSTS_JSON = 'data/posts.json'          # путь к файлу с постами

bp_api = Blueprint('bp_api', __name__)

log = logger.get_logger('main')


@bp_api.route("/api/posts")
def api_all_posts():
    posts = utils.load_all_posts(POSTS_JSON)
    log.info(f'api_all_posts - > {len(posts)}')
    return jsonify(posts)


@bp_api.route("/api/posts/<int:pk>")
def api_view_post(pk):
    post = utils.load_post(pk, POSTS_JSON)
    log.info(f'api_view_post - > {pk}')
    return jsonify(post)


# ашипке api
@bp_api.app_errorhandler(404)
def page_not_found(e):
    return 'Страница отсутствует'


@bp_api.app_errorhandler(500)
def server_error(e):
    return 'Ошибка со стороны сервера'
