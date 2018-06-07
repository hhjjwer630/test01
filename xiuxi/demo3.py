import pytest
@pytest.mark.parametrize(('username','password'),[('zhangsan','2345'),('lisi','4567')])
def testLogin(username,password):
    print('用户名是', username)
    print('密码是', password)

