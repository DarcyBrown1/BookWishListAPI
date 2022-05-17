from .app import load

my_app = load()


if __name__ == "__main__":
    my_app.run(debug=True)
