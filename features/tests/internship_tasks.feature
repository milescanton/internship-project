Feature: Internship Tasks

  Scenario: Add a project through the settings
    Given Open Reelly sign-in page
    When Login to page
    And Click on Settings
    And Click on Add a Project
    Then Add test information
    And Verify test information
    And Verify Send an Application button is available