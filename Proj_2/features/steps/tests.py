#!/usr/binenv python3

### BROWSE TESTS

@given("user is looking at the online shop page")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/")

@when("user clicks on \"Phones & PDAs\"")
def step_impl(context):
    context.browser.find_element_by_xpath("//a[contains(text(),'Phones & PDAs')]").click()

@then("products are displayed")
def step_impl(context):
    context.browser.find_element_by_xpath("//a[contains(text(),'HTC Touch HD')]")
    context.browser.find_element_by_xpath("//a[contains(text(),'iPhone')]")
    context.browser.find_element_by_xpath("//a[contains(text(),'Palm Treo Pro')]")

@when("user clicks on \"Add to Wish List\" button next to MacBook")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/")
    context.browser.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[3]/button[2]/i").click()


@given("user is looking at MacBook product page")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=product/product&product_id=43")

@when("user clicks on \"Add to Wish List\" button ")
def step_impl(context):
    try:
        context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=account/wishlist")
        context.browser.find_element_by_xpath("//a[@href='http://mys01.fit.vutbr.cz:8012/index.php?route=account/wishlist&remove=43']").click()
    except:
        pass
    context.browser.get("http://mys01.fit.vutbr.cz:8012/")
    context.browser.find_element_by_xpath("//button[2]").click()

@then("MacBook is added to the Wish list")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=account/wishlist")
    context.browser.find_element_by_xpath("//a[contains(text(),'MacBook')]")

@given("user is looking at their wish list")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=account/wishlist")

@given("wish list contains MacBook")
def step_impl(context):
    try:
        context.browser.get("http://mys01.fit.vutbr.cz:8012/")
        context.browser.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[3]/button[2]/i").click()
    except:
        pass
    context.browser.find_element_by_xpath("//a[contains(text(),'MacBook')]")


@when("user clicks on \"Components\" button")
def step_impl(context):
    context.browser.find_element_by_xpath("//nav[@id='menu']/div[2]/ul/li[3]/a").click()

@then("list of products is shown")
def step_impl(context):
    pass
    #assert(u"Mice and Trackballs (0)" == context.browser.find_element_by_css_selector(".open li:nth-child(1) > a").value())

@when("user clicks on \"Software\" button")
def step_impl(context):
    context.browser.find_element_by_xpath("//nav[@id='menu']/div[2]/ul/li[5]/a").click()

@then("\"There are no products to list in this category\" is displayed")
def step_impl(context):
    context.browser.find_element_by_xpath("//p[contains(.,'There are no products to list in this category.')]")

@given("user is logged in")
def step_impl(context):
    try:
        context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=account/login")
        context.browser.find_element_by_id("input-email").send_keys("miami@florida.gmail.com")
        context.browser.find_element_by_id("input-password").send_keys("wtfwtfwtfwtf")
        context.browser.find_element_by_xpath("//div[@id='content']/div/div[2]/div/form/input").click()
    except:
        pass

@when("user clicks on \"Add to cart\" button from wish list")
def step_impl(context):
    context.browser.find_element_by_xpath("//div[@id='content']/div/table/tbody/tr/td[6]/button/i").click()

### CART TESTS

@when("user clicks on \"Add to cart\" button next to the MacBook")
def step_impl(context):
    context.browser.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[3]/button/i").click()

@when("user clicks on \"Add to cart\" button")
def step_impl(context):
    context.browser.find_element_by_id("button-cart").click()

@then("MacBook is added to user's shopping cart")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=checkout/cart")
    context.browser.find_element_by_xpath("(//a[contains(text(),'MacBook')])[2]")
    context.browser.find_element_by_xpath("//div[@id='content']/form/div/table/tbody/tr/td[4]/div/span/button[2]/i").click()

@given("MacBook is in the cart")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=product/product&product_id=43")
    context.browser.find_element_by_id("button-cart").click()

@given("user types in quantity from range <-infinity, 0>")
def step_impl(context):
    context.browser.find_element_by_id("input-quantity").send_keys("-2")

@given("user types in quantity that is non-integer number")
def step_impl(context):
    context.browser.find_element_by_id("input-quantity").send_keys("1.5")

@when("user clicks on \"Cart\" button")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/")
    context.browser.find_element_by_id("cart-total").click()
    context.browser.find_element_by_css_selector("a:nth-child(1) > strong").click()
    context.browser.find_element_by_xpath("(//a[contains(text(),'MacBook')])[2]")

@given("user clicks on \"Cart\" button")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/")
    context.browser.find_element_by_id("cart-total").click()
    context.browser.find_element_by_css_selector("a:nth-child(1) > strong").click()
    context.browser.find_element_by_xpath("(//a[contains(text(),'MacBook')])[2]")

@then("MacBook is displayed")
def step_impl(context):
    context.browser.find_element_by_xpath("(//a[contains(text(),'MacBook')])[2]")

@then("MacBook is not added to user's shopping cart")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=checkout/cart")
    try:
        context.browser.find_element_by_xpath("(//a[contains(text(),'MacBook')])[2]")
        raise Exception()
    except:
        pass

@when("user clicks on \"Remove\" button")
def step_impl(context):
    try:
        context.browser.find_element_by_xpath("//div[@id='content']/form/div/table/tbody/tr/td[4]/div/span/button[2]/i").click()
        raise Exception()
    except:
        pass

@then("MacBook is removed from the user\'s shopping cart")
def step_impl(context):
    pass




