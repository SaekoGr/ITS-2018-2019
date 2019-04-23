Feature: Cart
    Background: the shops sells MacBook

    @clear_cart
    Scenario: Add from home page to cart
        Given user is looking at the online shop page
        When user clicks on "Add to cart" button next to the MacBook
        Then MacBook is added to user's shopping cart

    @clear_cart
    Scenario: Add from product's page to cart
        Given user is looking at MacBook product page
        When user clicks on "Add to cart" button
        Then MacBook is added to user's shopping cart

    Scenario: Add invalid number of products <-infinity, 0> to cart
        Given user is looking at MacBook product page
        And user types in quantity from range <-infinity, 0> 
        When user clicks on "Add to cart" button
        Then MacBook is not added to user's shopping cart

    Scenario: Add non integer number of products to cart
        Given user is looking at MacBook product page
        And user types in quantity that is non-integer number
        When user clicks on "Add to cart" button
        Then MacBook is not added to user's shopping cart
    
    @clear_cart @clear_wish_list @log_out
    Scenario: Add item from wish list to cart
        Given user is logged in
        And wish list contains MacBook
        And user is looking at their wish list
        When user clicks on "Add to cart" button from wish list
        Then MacBook is added to user's shopping cart

    Scenario: Remove item from cart
        Given MacBook is in the cart
        And user clicks on "Cart" button
        When user clicks on "Remove" button
        Then MacBook is removed from the user's shopping cart

    @clear_cart
    Scenario: View item in cart
        Given MacBook is in the cart
        When user clicks on "Cart" button
        Then MacBook is displayed

    @clear_cart
    Scenario: Update quantity in cart
        Given MacBook is in the cart
        And user clicks on "Cart" button
        And user types in "4" in quantity
        When user clicks on "Update" button
        Then MacBook has quantity "4"