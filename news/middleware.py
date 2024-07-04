from news.models import News


class RouteVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("before getting response in Middleware calling")
        response = self.get_response(request)
        print("after getting response in Middleware calling")
        return response
