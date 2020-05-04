class BasePage():
    #konstruktor klasy, specjalna fukncja uruchamiana przy tworzeniu obiektu
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()
        self._show_page(driver)

    def _verify_page(self):
        return

    def _show_page(self, driver):
        current_url = driver.current_url
        print ( "URL : %s" % current_url)
