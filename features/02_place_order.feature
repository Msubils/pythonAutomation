Feature: place order

    As a common user
    I want to place an order
    In order to validate placing an order

    Scenario: Place an order successfuly
        Given the user has an item in the cart
        When the user places an order
        And fills the requested fields
        Then a message will be displayed confirming the purchase
