Feature: Browse
    Background: the shops sells MacBook

    Scenario Outline: Add item to Wish List
        Given user is looking at <page>
        When user click on "Add to wish list" button
        Then MacBook is added to the wish list

        Examples:
            | page |
            | MacBook at home page |
            | at MacBook product page |

    Scenario: Show subcategories list
        Given user is looking at the online shop page
        When user clicks on "Components" button
        Then list of products is shown:
            | product |
            | Mice and Trackballs |
            | Monitors |
            | Printers |
            | Scanners |
            | Web Cameras |

    Scenario: Show products list
        Given user is looking at the online shop page
        When user clicks on "Phones & PDAs"
        Then products are displayed:
            | HTC Touch HD |
            | iPhone |
            | Palm Treo Pro |

    Scenario: Show empty category
        Given user is looking at the online shop page
        When user clicks on "Software" button
        Then "There are no products to list in this category" is displayed