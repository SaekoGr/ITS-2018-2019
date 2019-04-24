#!/usr/binenv python3

### BROWSE TESTS ###

# Background check
@given("the shop sells MacBook")
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
    text = context.browser.find_element_by_xpath("//div[@id='content']/p").text
    assert(text == u"Your shopping cart is empty!")

# Add non integer number of products to cart
@given("user types in quantity that is non-integer number")
def step_impl(context):
    context.browser.find_element_by_id("input-quantity").send_keys("1.5")

# Add item from wish list to cart
@given("wish list contains MacBook")
def step_impl(context):
    context.browser.get(context.base_url)
    context.browser.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[3]/button[2]/i").click()
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=account/wishlist")
    context.browser.find_element_by_xpath("//a[contains(text(),'MacBook')]")

@given("user is looking at their wish list")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=account/wishlist")

@when("user clicks on \"Add to cart\" button from wish list")
def step_impl(context):
    context.browser.find_element_by_xpath("//div[@id='content']/div/table/tbody/tr/td[6]/button/i").click()

# Remove item from cart
@given("MacBook is in the cart")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=checkout/cart")
    context.browser.find_element_by_xpath("(//a[contains(text(),'MacBook')])[2]")

@given("user clicks on \"Cart\" button")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/")
    context.browser.find_element_by_id("cart-total").click()
    context.browser.find_element_by_css_selector("a:nth-child(1) > strong").click()

@when("user clicks on \"Remove\" button")
def step_impl(context):
    context.browser.find_element_by_xpath("//div[@id='content']/form/div/table/tbody/tr/td[4]/div/span/button[2]/i").click()

@then("MacBook is removed from the user\'s shopping cart")
def step_impl(context):
    text = context.browser.find_element_by_xpath("//div[@id='content']/p").text
    assert(text == u"Your shopping cart is empty!")


# View item in cart
@when("user clicks on \"Cart\" button")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/")
    context.browser.find_element_by_id("cart-total").click()
    context.browser.find_element_by_css_selector("a:nth-child(1) > strong").click()

@then("MacBook is displayed")
def step_impl(context):
    text = context.browser.find_element_by_xpath("(//a[contains(text(),'MacBook')])[2]").text
    assert(text == u"MacBook")

# Update quantity in cart
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

### CHECKOUT ###
# Start checkout as logged user
@when("user clicks on \"Checkout\" button")
def step_impl(context):
    context.browser.get(context.base_url)
    context.browser.find_element_by_xpath("//div[@id='top-links']/ul/li[5]/a/i").click()

@then("checkout starts at step 2")
def step_impl(context):
    text = context.browser.find_element_by_xpath("//a[contains(text(),'Step 2: Billing Details')]").text
    assert(text == u"Step 2: Billing Details")

# Start checkout as guest user
@given("user is not logged in")
def step_impl(context):
    context.browser.get(context.base_url)
    context.browser.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/a/i")
    context.browser.find_element_by_xpath("//a[contains(text(),'Login')]")

@then("checkout starts at step 1")
def step_impl(context):
    text = context.browser.find_element_by_xpath("//a[contains(text(),'Step 1: Checkout Options')]").text
    assert(text == u"Step 1: Checkout Options")

# Checkout options when not logged in -- @1.1
@given("user is looking at the step 1 page")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=checkout/checkout")

@given("user chooses their option: register account")
def step_impl(context):
    context.browser.find_element_by_xpath("//label[contains(.,'Register Account')]").click()

@given("user chooses their option: guest account")
def step_impl(context):
    context.browser.find_element_by_xpath("//label[contains(.,'Guest Checkout')]").click()
    
@when("user clicks on \"Continue\" button")
def step_impl(context):
    context.browser.find_element_by_id("button-account").click()

# User logs in at checkout
@given("user inputs their information")
def step_impl(context):
    context.browser.find_element_by_xpath("//input[@id='input-email']").send_keys("miami@florida.gmail.com")
    context.browser.find_element_by_xpath("//input[@id='input-password']").send_keys("wtfwtfwtfwtf")

@when("user clicks on \"Login\"")
def step_impl(context):
    context.browser.find_element_by_id("button-login").click()

@then("checkout continues with user is logged in")
def step_impl(context):
    context.browser.find_element_by_xpath("//label[contains(.,'I want to use an existing address')]")
    context.browser.get(context.base_url)

#Payment method
@given("user is looking at the step 3 page")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=checkout/checkout")
    try:
        context.browser.find_element_by_xpath("//div[@id='collapse-payment-address']/div/form/div/label").click()
    except:
        context.browser.find_element_by_xpath("//a[contains(text(),'Step 2: Billing Details')]").click()
        context.browser.find_element_by_xpath("//div[@id='collapse-payment-address']/div/form/div/label").click()

    context.browser.find_element_by_id("button-payment-address").click()

@when("user does not check the \"Terms & Conditions\" box")
def step_impl(context):
    try:
        context.browser.find_element_by_id("button-payment-method").click()
    except:
        context.browser.find_element_by_xpath("//a[contains(text(),'Step 3: Payment Method')]").click()
        context.browser.find_element_by_id("button-payment-method").click()

@then("warning is triggered")
def step_impl(context):
    text = context.browser.find_element_by_css_selector(".alert").text
    assert(text == u"Warning: You must agree to the Terms & Conditions!\n×")

# Confirming order
@given("user is looking at the step 4 page")
def step_impl(context):
    # preparing all the stuff
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=checkout/checkout")
    try:
        context.browser.find_element_by_xpath("//div[@id='collapse-payment-address']/div/form/div/label").click()
    except:
        context.browser.find_element_by_xpath("//a[contains(text(),'Step 2: Billing Details')]").click()
        context.browser.find_element_by_xpath("//div[@id='collapse-payment-address']/div/form/div/label").click()

    
    context.browser.find_element_by_id("button-payment-address").click()

    try:
        context.browser.find_element_by_xpath("//input[@name='agree']").click()
    except:
        context.browser.find_element_by_xpath("//a[contains(text(),'Step 3: Payment Method')]").click()
        context.browser.find_element_by_xpath("//input[@name='agree']").click()

    context.browser.find_element_by_id("button-payment-method").click()

@when("user clicks on \"Confirm Order\" button")
def step_impl(context):
    try:
        context.browser.find_element_by_id("button-confirm").click()
    except:
        context.browser.find_element_by_xpath("//a[contains(text(),'Step 4: Confirm Order')]").click()
        context.browser.find_element_by_id("button-confirm").click()

@then("order has been placed")
def step_impl(context):
    text = context.browser.find_element_by_xpath("//p[contains(.,'Your order has been successfully processed!')]").text
    assert(text == u"Your order has been successfully processed!")

@given("user is looking at Step 2: Billing Details")
def step_impl(context):
    context.browser.get("http://mys01.fit.vutbr.cz:8012/index.php?route=checkout/checkout")
    try:
        context.browser.find_element_by_xpath("//label[contains(.,'Guest Checkout')]").click()
    except:
        context.browser.find_element_by_xpath("//a[contains(.,'Step 1: Checkout Options')]").click()
        context.browser.find_element_by_xpath("//label[contains(.,'Guest Checkout')]").click()

    context.browser.find_element_by_id("button-account").click()

@when("user does not fill in compulsory field")
def step_impl(context):
    try:
        context.browser.find_element_by_id("button-guest").click()
    except:
        context.browser.find_element_by_xpath("//a[contains(.,'Step 2: Billing Details')]").click()
        context.browser.find_element_by_id("button-guest").click()

@then("warning about missing First Name is displayed")
def step_impl(context):
    text = context.browser.find_element_by_css_selector("#account > .form-group:nth-child(3) > .text-danger").text
    assert(text == u"First Name must be between 1 and 32 characters!")

@then("warning about missing Last Name is displayed")
def step_impl(context):
    text = context.browser.find_element_by_css_selector(".form-group:nth-child(4) > .text-danger").text
    assert(text == u"Last Name must be between 1 and 32 characters!")

@then("warning about missing E-mail is displayed")
def step_impl(context):
    text = context.browser.find_element_by_css_selector(".form-group:nth-child(6) > .text-danger")
    assert(text == u"E-Mail address does not appear to be valid!")