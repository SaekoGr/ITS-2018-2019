Feature: Checkout
    Background:
        Given online shop is selling MacBook
        And user has MacBook in his cart
    
    Scenario: Start checkout
        Given user is "<status>"
        When user clicks on "Checkout" button
        Then checkout starts at step "<step>"

        Example:
            | status | step |
            | logged in | 2 |
            | not logged in | 1 |

    Scenario: Checkout options when not logged in
        Given user is not logged in
        And user chooses their option: "<option>"
        When user clicks on "Continue" button
        Then checkout continues with "<result>"

        Example:
            | option | result |
            | register account | registration and billing address |
            | guest account | billing address |

    Scenario: User logs in at checkout
        Given user has an account
        And user inputs their information
        When user clicks on "Login"
        Then checkout continues with user is logged in 

    Scenario: Logged in user chooses billing address
        Given user is logged in
        And user is looking at the step 2 page
        When user wants to use "<address_type>"
        Then "<address_result>"

        Example:
            | address_type | address_result |
            | existing address | existing address is used |
            | new address | user types in new address |

    Scenario: Payment method
        Given user is looking at the step 3 page
        When user does not check the "Terms & Conditions" box
        Then warning is triggered 
