# точка входа
from blog.app import create_app
from flask import redirect

app = create_app()

@app.route("/")
def index():
    return redirect('/users/')

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        debug = True,
        port = 5000
    )