from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS

from movie_base.schema import schema
from movie_base.config import config


app = Flask(__name__)
app.debug = True

cors = CORS(app, resources={'/graphql': {'origins': '*'}})


# def index(path=None):
#     return render_template('index.html', js_location=config['js_location'])


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
    )
)

# app.add_url_rule(
#     '/',
#     view_func=index
# )
# app.add_url_rule(
#     '/<path:path>',
#     view_func=index
# )
