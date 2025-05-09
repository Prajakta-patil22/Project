Feature: Verify user sign-in functionality

  Scenario: Verify log in functionality
    When User visits the test environment
    When User clicks on the sign-in url
    When User clicks on the sign-in link
    Then User enters "user1" email
    Then User enters "pwd" password
    Then User clicks on the sign-in button
    Then User asserts user profile
