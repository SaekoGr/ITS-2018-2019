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
        When user types in quantity from range <-infinity, 0> 
        And user clicks on "Add to cart"
        Then MacBook is not added to user's shopping cart

    Scenario: Add non integer number of products to cart
        Given user is looking at the MacBook detail page
        When user types in quantity that is non-integer number
        And user clicks on "Add to cart"
        Then MacBook is not added to user's shopping cart

    Scenario: Add item from wish list to cart
        Given the user is logged in
        And user is looking at their wish list
        And wish list contains MacBook
        When user clicks on "Add to cart" button
        Then MacBook is added to user's shopping cart

    Scenario: Remove item from cart
        Given MacBook is in the cart
        When user clicks on "Cart" button
        And user clicks on "Remove" button
        Then MacBook is removed from the user's shopping cart

    Scenario: View item in cart
        Given MacBook is in the cart
        When user click on "Cart" button
        And user clicks on "View Cart" button
        Then MacBook is displayed

    Scenario: Update quantity in cart
        Given MacBook is in the cart
        And user is looking ath the shopping cart
        When user types in "2" in quantity
        And user clicks on "Update" button
        Then MacBook has quantity "2"

    