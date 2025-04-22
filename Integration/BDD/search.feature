Feature: I want to search for products
    Scenario: Search
        Given I am on home page
        When I search for 'smartphone'
        Then I should see a list of matching products in search result