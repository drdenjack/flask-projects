# from src.app import log
from flask import Flask, json, jsonify, request
from flask.views import MethodView
from src.app_log import log
from src.models.user import User
from src.app_log import log
from src.database import db
# from src.util import Utils


class UserAPI(MethodView):
    """Handle all multiple user requests
    """
    @staticmethod
    def make_response(value, code):
        return jsonify(value), code

    def get(self, user_id: int):
        log.debug(f"Making a GET call in {self.__class__.__name__}", user_id=user_id)
        if user_id is not None:
            user = User.query.filter_by(id=user_id).first()
            if user:
                return self.make_response(user.serialize, 200)
            else:
                return f"User with id={user_id} not found in database.", 404
        else:
            users = User.query.all()
            users = [u.serialize for u in users]
            print(f'Users: {users}')
            return self.make_response(users, 200)

    def post(self):
        log.info(f"Making a POST call in {self.__class__.__name__}")
        try:
            log.msg("adding some users")
            body = request.get_json()
            log.info("Request Body:", body=body)
            new_users = body['users']


            log.msg("number of users to add", n=len(new_users))

            users = User.add_users(new_users)
            result = {
                'users': list(users.values())
            }
            return self.make_response(result, 200)
        except:
            code = 400  # bad request
            code = 401  # unauthorized
            code = 403  # forbidden
            code = 404  # not found
            code = 406  # Not Acceptible
            return "unable to add users", 400
        
    def put(self, user_id: int):
        log.info(f"Making a PUT call in {self.__class__.__name__}")
        if user_id:
            pass
        else:
            pass

    def delete(self, user_id: int):
        log.info(f"Making a DELETE call in {self.__class__.__name__}")
        if user_id:
            pass
        else:
            pass

def add_users_routes(app):
    print('adding url rules')
    user_view = UserAPI.as_view('user_api')
    app.add_url_rule('/users/', defaults={'user_id': None}, view_func=user_view, methods=['GET', ])
    app.add_url_rule('/users/', view_func=user_view, methods=['POST', ])
    app.add_url_rule('/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])
    
    # See https://flask.palletsprojects.com/en/2.0.x/views/

    # # General case:
    # def register_api(view, endpoint, url, pk='id', pk_type='int'):
    #     view_func = view.as_view(endpoint)
    #     app.add_url_rule(url, defaults={pk: None},  view_func=view_func, methods=['GET',])
    #     app.add_url_rule(url, view_func=view_func, methods=['POST',])
    #     app.add_url_rule(f'{url}<{pk_type}:{pk}>', view_func=view_func, methods=['GET', 'PUT', 'DELETE'])

    # register_api(UserAPI, 'user_api', '/users/', pk='user_id')