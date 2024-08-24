import json

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ApiBackEnd.utils import Envelope


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):

    @staticmethod
    def get(request):
        return Envelope(200, None, None).to_res()

    @staticmethod
    def post(request):
        return Envelope(200, None, None).to_res()

    @staticmethod
    def put(request):
        return Envelope(200, None, None).to_res()

    @staticmethod
    def delete(request):
        return Envelope(200, None, None).to_res()
