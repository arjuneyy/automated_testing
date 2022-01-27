Feature: TS_000001 Login Page

  Background: Website url
    Given website url from environment file
      And access the website

  Scenario: Title should be properly set
    Then title should be "4K: Materials Request & Warehouse Inventory Monitoring System"

  Scenario: Login should fail providing empty credentials
    Given user credentials username "None" and password "None"
      And input user credentials
    When login button is clicked
    Then console log should not be empty
      And "Empty fields!" should be thrown in console log

  Scenario: Login should fail for unregistered users
    Given user credentials username "user1" and password "password"
      And input user credentials
    When login button is clicked
    Then console log should not be empty
      And "login error!" should be thrown in console log

  Scenario: Login should fail for correct username but wrong password
    Given user credentials username "Kasper" and password "wrong_password"
      And input user credentials
    When login button is clicked
    Then console log should not be empty
      And "login error!" should be thrown in console log

  Scenario: Login should fail for wrong username but correct password
    Given user credentials username "Kasper" and password "wrong_password"
      And input user credentials
    When login button is clicked
    Then console log should not be empty
      And "login error!" should be thrown in console log

  Scenario: Successful login for users with correct credentials
    Given user credentials username "Kasper" and password "Cain"
      And input user credentials
    When login button is clicked
    Then logout button should be visible
      And sidebar should be visible
