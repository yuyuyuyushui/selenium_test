from abc import abstractclassmethod
from search import SearchRegion
class BasePage(object):
    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver

    @abstractclassmethod #接口方法，只能用于继承
    def _validate_page(self, driver):# 使用属性和操作之前，验证页面是否已经加载到浏览器。
        return """Regions define functionality available through all page objects"""
    @property #将属性变成方法
    def search(self): # search属性用于返回SearchRegion对象
        return SearchRegion(self.driver)
class InvalidPageException(Exception):
    """ Throw this exception when you don't find the correct page """
    pass
