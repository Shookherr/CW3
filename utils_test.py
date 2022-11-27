from pytest import fixture
from main import app
from utils import load_comments_pk


@fixture()
def posts_keys():
    return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_posts():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_post(posts_keys):
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) == posts_keys


def test_comments():
    data = load_comments_pk(3, 'data/comments.json')
    assert type(data) == list
