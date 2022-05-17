import json
import flask_app
import unittest
from mock import patch

app = flask_app.app.load()


class ApiTests(unittest.TestCase):
    def test_api_health_check(self):
        with app.test_client() as c:
            rv = c.get(path="/api/healthz")
            value = json.loads(rv.data)
            assert {"pass": True} == value and rv.status_code == 200

    @patch("flask_app.api.views.wish_list", [])
    def test_api_wish_list_get_empty(self):
        with app.test_client() as c:
            rv = c.get(path="/api/user/1/wishlist")
            value = json.loads(rv.data)
            assert rv.status_code == 200
            assert isinstance(value, list)
            assert len(value) == 0

    @patch("flask_app.api.views.wish_list", [{"user_id": 1, "book_id": 1}, {"user_id": 2, "book_id": 2}])
    def test_api_wish_list_get_value(self):
        with app.test_client() as c:
            rv = c.get(path="/api/user/1/wishlist")
            value = json.loads(rv.data)
            assert rv.status_code == 200
            assert isinstance(value, list)
            assert len(value) == 1
            assert value[0]["book_id"] == 1

    @patch("flask_app.api.views.users", [])
    @patch("flask_app.api.views.books", [{"id": 1}, {"id": 2}])
    def test_api_add_book_wishlist_no_user(self):
        with app.test_client() as c:
            rv = c.post(path="/api/user/1/wishlist/1")
            assert rv.status_code == 404

    @patch("flask_app.api.views.users", [{"id": 1}, {"id": 2}])
    @patch("flask_app.api.views.books", [])
    def test_api_add_book_wishlist_no_book(self):
        with app.test_client() as c:
            rv = c.post(path="/api/user/1/wishlist/1")
            assert rv.status_code == 404

    @patch("flask_app.api.views.wish_list", [])
    @patch("flask_app.api.views.users", [{"id": 1}, {"id": 2}])
    @patch("flask_app.api.views.books", [{"id": 1}, {"id": 2}])
    def test_api_add_book_wishlist_success(self):
        assert len(flask_app.api.views.wish_list) == 0
        with app.test_client() as c:
            rv = c.post(path="/api/user/1/wishlist/1")
            assert rv.status_code == 201
            assert len(flask_app.api.views.wish_list) == 1

    @patch("flask_app.api.views.wish_list", [])
    @patch("flask_app.api.views.users", [{"id": 1}, {"id": 2}])
    @patch("flask_app.api.views.books", [{"id": 1}, {"id": 2}])
    def test_api_remove_book_wishlist_empty(self):
        assert len(flask_app.api.views.wish_list) == 0
        with app.test_client() as c:
            rv = c.delete(path="/api/user/1/wishlist/1")
            assert rv.status_code == 200
            assert len(flask_app.api.views.wish_list) == 0

    @patch("flask_app.api.views.wish_list", [{"user_id": 1, "book_id": 1}])
    @patch("flask_app.api.views.users", [{"id": 1}, {"id": 2}])
    @patch("flask_app.api.views.books", [{"id": 1}, {"id": 2}])
    def test_api_remove_book_wishlist_sucess(self):
        assert len(flask_app.api.views.wish_list) == 1
        with app.test_client() as c:
            rv = c.delete(path="/api/user/1/wishlist/1")
            assert rv.status_code == 200
            assert len(flask_app.api.views.wish_list) == 0

    @patch("flask_app.api.views.wish_list", [{"user_id": 1, "book_id": 2}])
    @patch("flask_app.api.views.users", [{"id": 1}, {"id": 2}])
    @patch("flask_app.api.views.books", [{"id": 1}, {"id": 2}])
    def test_api_remove_book_wishlist_not_there(self):
        assert len(flask_app.api.views.wish_list) == 1
        with app.test_client() as c:
            rv = c.delete(path="/api/user/1/wishlist/1")
            assert rv.status_code == 200
            assert len(flask_app.api.views.wish_list) == 1

    @patch("flask_app.api.views.wish_list", [])
    def test_api_get_all_users_with_wishlist_empty(self):
        with app.test_client() as c:
            rv = c.get(path="/api/wishlist/users")
            value = json.loads(rv.data)
            assert rv.status_code == 200
            assert isinstance(value, list)
            assert len(value) == 0

    @patch("flask_app.api.views.wish_list", [{"user_id": 1, "book_id": 1}, {"user_id": 2, "book_id": 2}])
    def test_api_get_all_users_with_wishlist(self):
        with app.test_client() as c:
            rv = c.get(path="/api/wishlist/users")
            value = json.loads(rv.data)
            assert rv.status_code == 200
            assert isinstance(value, list)
            assert len(value) == 2

    @patch("flask_app.api.views.wish_list", [{"user_id": 1, "book_id": 1}, {"user_id": 2, "book_id": 2}])
    def test_api_get_all_wishlists(self):
        with app.test_client() as c:
            rv = c.get(path="/api/wishlist")
            value = json.loads(rv.data)
            assert rv.status_code == 200
            assert isinstance(value, list)
            assert len(value) == 2

    @patch("flask_app.api.views.wish_list", [])
    def test_api_get_all_wishlists_empty(self):
        with app.test_client() as c:
            rv = c.get(path="/api/wishlist")
            value = json.loads(rv.data)
            assert rv.status_code == 200
            assert isinstance(value, list)
            assert len(value) == 0
