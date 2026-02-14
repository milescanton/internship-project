Feature: Internship Tasks

  Scenario: Add a project through the settings
    Given Open Reelly sign-in page
    When Login to page using cantonmiles@gmail.com and testpassword1
    And Click on Settings
    And Click on Add a Project
    Then Add and verify test information
    And Verify Send an Application button is active