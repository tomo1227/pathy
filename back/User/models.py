from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone

# cliでユーザー作成するときのclass
class MyUserManager(BaseUserManager):
    # 一般ユーザーの作成
    #def create_user(self, email, username, password=None):
    def create_user(self, request_data, *args, **kwargs):
        now = timezone.now()
        if not request_data['email']:
            raise ValueError('メールアドレスは必須です。')

        user = self.model(
            username=request_data['username'],
            email=self.normalize_email(request_data['email']),
            is_active=True,
            is_admin=False,
        )

        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user

    # 管理ユーザーの作成
    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='メールアドレス',max_length=255,unique=True)
    username = models.CharField(verbose_name='ユーザー名',max_length=50,unique=True,blank=True) # 空文字を許容
    password = models.CharField(max_length=128, verbose_name='パスワード')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    # 認証に使用するfield
    USERNAME_FIELD = 'email'

    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin