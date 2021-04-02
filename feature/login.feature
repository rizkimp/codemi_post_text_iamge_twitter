Feature: login
  Scenario: login
    Given in twitter login page
    When enter valid username and password
    And click login button
    Then success login
