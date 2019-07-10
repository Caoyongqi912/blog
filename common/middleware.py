#
from django.http import HttpResponseBadRequest, HttpResponseNotFound

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class MyCustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass
    def process_response(self, request,response):
        return response


class BadUAMiddleware(MyCustomMiddleware):
    def process_request(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        if not user_agent:
            return HttpResponseBadRequest(content='r u spider?')
        if 'python' in user_agent or 'requests' in user_agent or 'scrapy' in user_agent:
            return HttpResponseBadRequest(content='r u spider?')
#
#
#
# #中间件验证cookies
# # class BadCookieMiddleware(MyCustomMiddleware):
# #     def process_request(self, request):
# #         cookies = request.COOKIES
# #         if 'my_name' not in cookies:
# #             return HttpResponseBadRequest(content='不是一个好cookies')
#
#
#
# #定制访问频率
#
# # VISIT_TOTAL_TIME = 60
# # VISIT_PER_SECOND = 10
# # AllOW = {}
#
#
# # class SlowSpeedMiddleware(MyCustomMiddleware):
# #     ip = '1.1.1.1'
# #
# #     def process_request(self, request):
# #         ctime = time.time()
# #         ip = self.ip
# #         if ip not in AllOW:
# #             AllOW[ip] = ip
# #
# #         else:
# #             time_list = AllOW[ip]
# #             while 1:
# #                 last_time = time_list[-1] if time_list else None
# #                 if not last_time:
# #                     break
# #                 if ctime - VISIT_TOTAL_TIME > last_time:
# #                     time_list.pop()
# #                 else:
# #                     break
# #
# #             if len(AllOW[ip]) > VISIT_PER_SECOND:
# #                 err_msg = {
# #                     'msg': '慢点，访问频率太快啦，限制你{}！{}秒后再试'.format(ip, self.wait())
# #
# #                 }
# #                 return HttpResponseNotFound(content=demjson.encode(err_msg), content_type='application/json')
# #
# #     def wait(self):
# #         ip = self.ip
# #         ctime = time.time()
# #         first_in_time = AllOW[ip][-1]
# #         wt = VISIT_TOTAL_TIME - (ctime - first_in_time)
# #         return int(wt)
