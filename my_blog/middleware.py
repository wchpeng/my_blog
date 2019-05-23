request_user = None


class GlobalRequestUserMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def process_request(self, request):
        global request_user
        request_user = request.user


def get_request_user_filter():
    if request_user is None:
        return None
    return {'creater_id': request_user.id}
