Feature: Cart
    Background: the shops sells MacBook

    Scenario: Add from home page to cart
        Given user is looking at the home page
        When user clicks on "Add to cart" button of MacBook
        Then MacBook is added to user's shopping cart

    Scenario: Add from product's page to cart
        Given user is looking at the product detail page
        When user clicks on "Add to cart" button
        Then MacBook is added to user's shopping cart

    Scenario: Add invalid number of products <-infinity, 0> to cart
        Given user is looking at the MacBook detail page
        And user types in quantity from range <-infinity, 0> 
        When And user clicks on "Add to cart"
        Then MacBook is not added to user's shopping cart

    Scenario: Add non integer number of products to cart
        Given user is looking at the MacBook detail page
        And user types in quantity that is non-integer number
        When And user clicks on "Add to cart"
        Then MacBook is not added to user's shopping cart

    Scenario: Add item from wish list to cart
        Given the user is logged in
        And user is looking at their wish list
        And wish list contains MacBook
        When user clicks on "Add to cart" button
        Then MacBook is added to user's shopping cart

    Scenario: Remove item from cart
        Given MacBook is in the cart
        And user clicks on "Cart" button
        When user clicks on "Remove" button
        Then MacBook is removed from the user's shopping cart

    Scenario: View item in cart
        Given MacBook is in the cart
        When user clicks on "Cart" button
        Then MacBook is displayed

    Scenario: Update quantity in cart
        Given MacBook is in the cart
        And user is looking at the shopping cart
        And user types in "4" in quantity
        When user clicks on "Update" button
        Then MacBook has quantity "4"


    