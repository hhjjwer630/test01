import pytest
class Test01:
    def test_01(self):
        print('test001----------')

    @pytest.mark.run(order=1)
    def test_02(self):
        print('test002----------')
    @pytest.mark.skipif(reason='done')
    def test_03(self):
        print('test003----------')
        assert 0