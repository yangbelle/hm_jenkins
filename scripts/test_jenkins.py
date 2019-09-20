import allure


class TestJenkins:
    """测试jenkins工作原理"""

    @allure.step('操作jenkins')
    def test_001(self):
        allure.attach("附件名称","附件内容")
        assert True