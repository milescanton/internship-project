Feature: Tests for Target site

  Scenario Outline: Search for a product
    Given Open Target main page
    When Search for <product>
    Then Search results for <product_results> are shown
    Examples:
    |product   |product_results  |
    |tea       |tea              |
    |mug       |mug              |
    |coffee    |coffee           |

  Scenario: Verify "Your cart is empty" message
    Given Open Target main page
    When Click on cart icon
    Then Empty Cart message is shown

  Scenario: Verify ability to open Sign In form
    Given Open Target main page
    When Click Account button
    Then Click Sign In button
    Then Verify Sign In page

    Scenario: Verify cart addition
      Given Open Target main page
      When Search for bread
      Then Click Add to Cart Button
      And Store product name
      And Click 2nd Add to Cart Button
      And Click View Cart Button
      Then Verify Cart

    Scenario: User can open and close Terms and Conditions from Sign In page
      Given Open Sign In page
      When Store original window
      And Click on Target Terms and Conditions link
      And Switch to new window
      Then Verify Terms and Conditions page is opened
      And Return to original window

#  Scenario: Verify benefit cells
#    Given Open Target main page
#    When Click Target Circle
#    Then Verify 5 benefit cells are shown
#
#  Scenario: Verify that user can see product names and images
#    Given Open Target main page
#    When Search for AirPods
#    Then Verify that every product has a name and an image
#
#  Scenario: User can search for a tea on Target
#    Given Open Target main page
#    When Search for tea
#    Then Search results for tea are shown