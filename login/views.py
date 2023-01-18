from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser

class Applogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')

        user = LoginUser.objects.filter(user_id=user_id).first()

        if not user:
            return Response(dict(msg='해당 사용자가 없습니다.'))

        # (사용자가 있으면 password체크)
        if check_password(user_pw, user.user_pw):
            return Response(dict(msg='로그인 성공'))
        else:
            return Response(dict(msg='로그인 실패, 비밀번호 틀림'))

# Create your views here.

class RegistUser(APIView):
    # APIView를 상속한 view클래스는 def post, def get으로 분리해서 받을 수 있다
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')
        # 암호화한 것으로 저장
        user_pw_encrypted = make_password(user_pw)

        # 중복 조회
        user = LoginUser.objects.filter(user_id=user_id).first()
        if user:
            return Response(dict(msg='동일한 아이디가 있습니다.'))
        # 생성
        # LoginUser.objects.create(user_id=user_id, user_pw=user_pw)
        LoginUser.objects.create(user_id=user_id, user_pw=user_pw_encrypted)

        # 그대로 내려보낼 건데, 일단 dict()화 시킨 뒤, Response클래스 dict를 넣어준다.
        data = dict(
            user_id=user_id,
            # user_pw=user_pw,
            user_pw=user_pw_encrypted,
        )

        return Response(data)
