Feature: post text and image
  Scenario: login
    Given in twitter login page
    When enter valid username and password
    And click login button
    Then success login
  Scenario: post text and image
    Given in twitter home page
    When enter text and upload image
    And click button tweet
    Then success post text and image
