from django.db import models

# Create your models here.
class LoginUser(models.Model):

    user_id = models.CharField(max_length=20, unique=True, null=False, default=False)
    user_pw = models.CharField(max_length=256, null=False, default=False)

    class Meta:
        # 테이블명은 내부 Metaclass에 db_table로 만든다.
        db_table = 'login_user'
        verbose_name = '로그인 테스트 테이블'