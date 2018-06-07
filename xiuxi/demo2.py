import  pytest
@pytest.mark.parametrize(('username','password'),[('张三','2345'),('李四','3456')])
def test01(username,password):
    print('用户名为：%s' %username)
    print('密码为：%s' %password)