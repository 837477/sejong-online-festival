from datetime import datetime
from pymongo import IndexModel, DESCENDING, ASCENDING
from .base import Model


class User(Model):

    VERSION = 1

    @property
    def index(self) -> list:
        return []

    @property
    def schema(self) -> dict:
        return {
            'user_id': "", # 유저 아이디
            'password': "", # 유저 패스워드 해시
            'roles': [], # 계정 권한
            'name': "", # 사용자 이름
            'major': "", # 사용자 전공
            'created_at': datetime.now(),
            '__version__': self.VERSION
        }