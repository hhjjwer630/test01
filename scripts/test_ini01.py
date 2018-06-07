class TestABC:
			def setup_class(self):
				print("------->setup_class")
			def teardown_class(self):
				print("------->teardown_class")
			def test_a(self):
				print("------->test_a")
				assert 1
			def test_b(self):
				print("------->test_b")
				assert 0 # 断言失败