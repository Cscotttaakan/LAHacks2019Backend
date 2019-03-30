import config
import mlapp
from flask import Flask

app = mlapp.create_app(config)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
