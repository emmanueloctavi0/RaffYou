
# Django
from django.views import View
from django.contrib.auth. mixins import LoginRequiredMixin
from django.http import JsonResponse

# Models
from carts.models import PromotionalCode

# Utilities
import json
from carts.utils import check_code


class CheckCodeView(LoginRequiredMixin, View):

    def invalid_code_res(self):
        return JsonResponse({
            'status': 'invalid',
            'message': 'Código no valido',
        }, status=400)

    def post(self, request):
        try:
            body = json.loads(request.body)
            code = body['code']
            price = float(body['price'])
        except KeyError:
            return self.invalid_code_res()

        is_valid, new_price = check_code(code, price)
        if not is_valid:
            return self.invalid_code_res()

        return JsonResponse({
            'status': 'valid',
            'code': code,
            'price': new_price,
            'message': 'Código valido',
        })
