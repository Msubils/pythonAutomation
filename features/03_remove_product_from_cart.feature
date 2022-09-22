Feature: remove product from cart

    As a common user
    I want to remove a product from the cart
    In 

   // Scenario: Place an order successfuly
        Given the user has an item in the cart
        When the user places an order
        And fills the requested fields
        Then a message will be displayed confirming the purchase
