Feature: Online Shopping

  Scenario: Purchase an Iphone
    Given I launch chrome browser
    When I open ProtoCommerce home Page
    When click on shop button
    When Select a product and add to cart
    When click Check out on shopping page
    When click check out on checkout page
    When Enter country name
    When click on country name
    When Enable Check box
    When Click on Purchase button
    Then Verify the succes message
