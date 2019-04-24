Feature: Checkout
    Background: 
        Given the shop sells MacBook
        And MacBook is in the cart
    
    @add_to_cart @clear_cart
    Scenario Outline: Not filling in required fields in Billing details as guest
        Given user is not logged in
        And user is looking at Step 2: Billing Details
        When user does not fill in compulsory field
        Then warning about missing <warning> is displayed

        Examples:
            | warning |
            | First Name |
            | Last Name |
            | E-mail |
            | Telephone |
