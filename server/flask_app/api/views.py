from . import api, wish_list, users, books
from flask import jsonify


@api.route("/healthz")
def healthz():
    """
    Return the result of a full self diagnostic check.
    """
    return jsonify({"pass": True})


@api.route("/user/<int:user_id>/wishlist", methods=["GET"])
def user_list_get(user_id):
    """
    Returns a list of all books on a user's wishlist
    """
    users_wish_list = [book for book in wish_list if book["user_id"] == user_id]
    return jsonify(users_wish_list)


@api.route("/user/<int:user_id>/wishlist/<int:book_id>", methods=["POST"])
def user_book_add(user_id, book_id):
    """
    Add a book to a user's wish list.
    """
    user = [user for user in users if user["id"] == user_id]
    book = [book for book in books if book["id"] == book_id]
    if not (user and book):
        return "", 404

    book_in_list = [book for book in wish_list if book["book_id"] == book_id and book["user_id"] == user_id]
    if not book_in_list:
        wish_list.append({"user_id": user_id, "book_id": book_id})
    return "", 201


@api.route("/user/<int:user_id>/wishlist/<int:book_id>", methods=["DELETE"])
def user_book_remove(user_id, book_id):
    """
    Remove a book from a user's wish list
    """
    book_in_list = [book for book in wish_list if book["book_id"] == book_id and book["user_id"] == user_id]
    if book_in_list:
        for book in book_in_list:
            wish_list.remove(book)
    return ""


@api.route("/wishlist/users", methods=["get"])
def wishlist_users_get():
    """
    get all user id's that have a wishlist
    """
    users = [book["user_id"] for book in wish_list]
    return jsonify(users)


@api.route("/wishlist", methods=["get"])
def wishlist_get():
    """
    get all wishlist's
    personally I think this is an insane idea, but the directions read:
    We also want an API for getting all wishlists
    I would actually use the two api's above, together with get list for a user
    to get this data.
    """
    return jsonify(wish_list)
