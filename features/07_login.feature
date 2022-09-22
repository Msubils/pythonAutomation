Feature: user login

    As a common user
    I want to login in the website
    In order to have access to the application

    Scenario: Login in the website
        Given the user is on demoblaze.com
        When the user logs in
        Then the page displays the button log out
