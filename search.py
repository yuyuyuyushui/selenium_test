from base import BasePage
from base import InvalidPageException
from product import ProductPage
class SearchRegion(BasePage):
    _search_box_locator = 'q'
    def __init__(self,driver):
        super(SearchRegion, self).__init__(driver)
    def searchFor(self, term):#返回SearchResult类对应的搜索结果页面
        self.search_field = self.driver.find_element_by_name(self._search_box_locator)
        self.search_field.clear()
        self.search_field.send_keys(term)
        self.search_field.submit()
        return SearchRegion(self.driver)

class SearchResults(BasePage):
    _product_list_locator = 'ul.products-grid > li'
    _product_name_locator ='h2.product-name a'
    _product_image_link = 'a.product-image'
    _product_title_locator = 'div.page-title'
    _product_count = 0
    _products ={}
    def __init__(self, driver):
        super(SearchResults, self).__init__(driver)
        results = self.driver.find_elements_by_css_selector(self._product_list_locator)
        for product in results:
            name = product.find_element_by_css_selector(self._product_name_locator).text
            self._products[name]=product.find_element_by_css_selector(self._product_image_link)
    def _validate_page(self, driver):
        if 'Search results for' not in driver.title:
            raise InvalidPageException('Search results not loaded')
    @property
    def product_count(self):
        return len(self._products)
    def get_products(self):
        return self._products
    def open_product_page(self, product_name):
        self._products[product_name].click()
        return ProductPage(self.driver)