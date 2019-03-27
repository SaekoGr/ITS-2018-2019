Feature: Checkout
    Background:
        Given online shop is selling MacBook
        And user has MacBook in his cart
    
    Scenario Outline: Start checkout
        Given user is <status>
        When user clicks on "Checkout" button
        Then checkout starts at step <step>

        Examples:
            | status | step |
            | logged in | 2 |
            | not logged in | 1 |

    Scenario Outline: Checkout options when not logged in
        Given user is not logged in
        And user chooses their option: <option>
        When user clicks on "Continue" button
        Then checkout continues with <result>

        Examples:
            | option | result |
            | register account | registration and billing address |
            | guest account | billing address |

    Scenario: User logs in at checkout
        Given user has an account
        And user inputs their information
        When user clicks on "Login"
        Then checkout continues with user is logged in 

    Scenario Outline: Logged in user chooses billing address
        Given user is logged in
        And user is looking at the step 2 page
        When user wants to use <address_type>
        Then <address_result>

        Examples:
            | address_type | address_result |
            | existing address | existing address is used |
            | new address | user can type in new address |

    Scenario Outline: Logged in user chose new address
        Given user is logged in
        And user wants to use a new address
        When user does not fill in <warning>
        Then warning about missing <warning> is displayed

        Examples:
            | warning |
            | First Name |
            | Last Name |
            | Address 1 |
            | City |
            | Post Code |
            | Country |
            | Region / State |
        
    Scenario: Payment method
        Given user is looking at the step 3 page
        When user does not check the "Terms & Conditions" box
        Then warning is triggered 

    Scenario Outline: Not filling in required fields in Billing details as guest
        Given user chose guest checkout
        When user does not fill in <warning>
        Then warning about missing <warning> is displayed

        Examples:
            | warning |
            | First Name |
            | Last Name |
            | E-mail |
            | Telephone |
            | Address 1 |
            | City |
            | Post Code |
            | Country |
            | Region / State |

    Scenario Outline: Not filling in required fields in Account & Billing Details as newly registering user
        Given user chose register account
        When user does not fill in <warning>
        Then warning about missing <warning> is displayed 

        Examples:
            | warning |
            | First Name |
            | Last Name |
            | E-mail |
            | Telephone |
            | Password |
            | Password Confirm |
            | Address 1 |
            | City |
            | Post Code |
            | Country |
            | Region / State |

    Scenario: Confirming order
        Given user is looking at the step 4 page
        When user clicks on "Confirm Order" button
        Then order has been placed

