Feature:Searching on the web store
  As a customer,
  I want to ssearch for a product on the home page
  So I can add the listed product into my cart

  Scenario: Searching as a guest
    Given The store home page is displayed
    When The user searches for "dress"
    Then At least one product is listed

