#!/usr/binenv python3

### BROWSE TESTS ###

# Background check
@given("the shops sells MacBook")
def step_impl(context):
    context.browser.get(context.base_url)
    context.browser.find_element_by_xpath("//a[contains(text(),'MacBook')]")

# Add item to Wish List -- @1.1
@given("user is looking at the online shop page")
def step_impl(context):
    context.browser.get(context.base_url)

@given("user is logged in")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=account/login")
    context.browser.find_element_by_id("input-email").send_keys("miami@florida.gmail.com")
    context.browser.find_element_by_id("input-password").send_keys("wtfwtfwtfwtf")
    context.browser.find_element_by_xpath("//div[@id='content']/div/div[2]/div/form/input").click()

@when("user clicks on \"Add to Wish List\" button next to MacBook")
def step_impl(context):
    context.browser.get(context.base_url)
    context.browser.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[3]/button[2]/i").click()

@then("MacBook is added to the Wish list")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=account/wishlist")
    context.browser.find_element_by_xpath("//a[contains(text(),'MacBook')]")


# Add item to Wish List -- @1.2
@given("user is looking at MacBook product page")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=product/product&product_id=43")

@when("user clicks on \"Add to Wish List\" button ")
def step_impl(context):
    context.browser.get(context.base_url)
    context.browser.find_element_by_xpath("//button[2]").click()

# Show subcategories list
@when("user clicks on \"Components\" button")
def step_impl(context):
    context.browser.find_element_by_xpath("//nav[@id='menu']/div[2]/ul/li[3]/a").click()

@then("list of products is shown")
def step_impl(context):
    for row in context.table:
        assert(row["category"] == context.browser.find_element_by_xpath("//a[contains(text(),'"+row["category"]+"')]").text)

# Show products list
@when("user clicks on \"Phones & PDAs\"")
def step_impl(context):
    context.browser.find_element_by_xpath("//a[contains(text(),'Phones & PDAs')]").click()

@then("products are displayed")
def step_impl(context):
    for row in context.table:
        assert(row["product"] == context.browser.find_element_by_xpath("//a[contains(text(),'"+row["product"]+"')]").text)

# Show empty category
@when("user clicks on \"Software\" button")
def step_impl(context):
    context.browser.find_element_by_xpath("//nav[@id='menu']/div[2]/ul/li[5]/a").click()

@then("\"There are no products to list in this category\" is displayed")
def step_impl(context):
    context.browser.find_element_by_xpath("//p[contains(.,'There are no products to list in this category.')]")

### CART TESTS ###

# Add from home page to cart
@when("user clicks on \"Add to cart\" button next to the MacBook")
def step_impl(context):
    context.browser.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[3]/button/i").click()

@then("MacBook is added to user's shopping cart")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=checkout/cart")
    context.browser.find_element_by_xpath("(//a[contains(text(),'MacBook')])[2]")
    # cleanup
    #context.browser.find_element_by_xpath("//div[@id='content']/form/div/table/tbody/tr/td[4]/div/span/button[2]/i").click()

# Add from product's page to cart
@when("user clicks on \"Add to cart\" button")
def step_impl(context):
    context.browser.find_element_by_id("button-cart").click()


# Add invalid number of products <-infinity, 0> to cart
@given("user types in quantity from range <-infinity, 0>")
def step_impl(context):
    context.browser.find_element_by_id("input-quantity").send_keys("-2")

@then("MacBook is not added to user's shopping cart")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=checkout/cart")
    found = context.browser.find_element_by_xpath("(//a[contains(text(),'MacBook')])[2]").text
    if(found == u"MacBook"):
        context.browser.find_element_by_xpath("//div[@id='content']/form/div/table/tbody/tr/td[4]/div/span/button[2]/i").click()
        raise Exception()
    else:
        pass

# Add non integer number of products to cart
@given("user types in quantity that is non-integer number")
def step_impl(context):
    context.browser.find_element_by_id("input-quantity").send_keys("1.5")

# Add item from wish list to cart
@given("wish list contains MacBook")
def step_impl(context):
    try:
        context.browser.get("http://mys01.fit.vutbr.cz:8012/")
        context.browser.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[3]/button[2]/i").click()
    except:
        pass
    context.browser.find_element_by_xpath("//a[contains(text(),'MacBook')]")

@given("user is looking at their wish list")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=account/wishlist")

@when("user clicks on \"Add to cart\" button from wish list")
def step_impl(context):
    context.browser.find_element_by_xpath("//div[@id='content']/div/table/tbody/tr/td[6]/button/i").click()
    # cleanup
    context.browser.find_element_by_xpath("//div[@id='content']/div/table/tbody/tr/td[6]/a/i").click()

# 




















@given("MacBook is in the cart")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=product/product&product_id=43")
    context.browser.find_element_by_id("button-cart").click()





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

@given("user types in \"4\" in quantity")
def step_impl(context):
    context.browser.find_element_by_xpath("//input[starts-with(@name, 'quantity')]").clear()
    context.browser.find_element_by_xpath("//input[starts-with(@name, 'quantity')]").send_keys("4")

@when("user clicks on \"Update\" button")
def step_impl(context):
    context.browser.find_element_by_css_selector("button.btn.btn-primary").click()

@then("MacBook has quantity \"4\"")
def step_impl(context):
    amount = context.browser.find_element_by_xpath("//input[starts-with(@name, 'quantity')]").get_attribute("value")
    assert(amount == u"4")