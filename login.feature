Feature: Verify user sign-in functionality

  Scenario: Verify log in functionality
    When User visits the test environment
    And User clicks on the sign-in url
    And User clicks on the sign-in link
    Then User enters email ID
    And User enters password
    When User clicks on the sign-in button
