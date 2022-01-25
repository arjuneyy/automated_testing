Feature: TS_000002 Dashboard Display with Regards to User Permission
    Currently, there are 2 user permissions:
    - Monitoring User with access level 2.
    - Warehousing user with access level 1.

 Background: Website url
  Given website url "http://127.0.0.1:8080"
   And access website

 @logout
 Scenario:[UP_S_000001] User with either of the specified access level should have no modules in his/her dashboard
  Given user credentials username "User" and password "User"
   And username input field id "username"
   And password input field id "password"
   And login button xpath "//*[@id='login-form']/button"
   And input user credentials
  When login button is clicked
  Then element with id "btn-logout" should be visible
   And element with id "sn-group" should be visible
   And should have "0" number of modules displayed in sidebar with id "sn-group"

 @logout
 Scenario:[UP_S_000002] Account type for user with access level 2 should have 'MONITORING' title in sidebar
  Given user credentials username "Kasper" and password "Cain"
   And username input field id "username"
   And password input field id "password"
   And login button xpath "//*[@id='login-form']/button"
   And input user credentials
  When login button is clicked
  Then element with id "sn-group" should be visible
   And account type should be "MONITORING" in element with id "/html/body/div[1]/div/div[2]/div[1]/div[1]/span"

 @logout
 Scenario Outline:[UP_S_000003 - UP_S-000006] Account type for user with access level 2 should have access to specific modules
  Given user credentials username "Kasper" and password "Cain"
   And username input field id "username"
   And password input field id "password"
   And login button xpath "//*[@id='login-form']/button"
   And input user credentials
  When login button is clicked
  Then element with id "sn-group" should be visible
   And get displayed modules displayed in element with id "sn-group"
   And "<module>" module should be displayed

  Examples:
   | module     |
   | Requesting |
   | Released   |
   | Reports    |
   | MIRR       |

 @logout
 Scenario:[UP_S_000007] Account type for user with access level 1 should have 'WAREHOUSING' title in sidebar
  Given user credentials username "Karl" and password "Dasma"
   And username input field id "username"
   And password input field id "password"
   And login button xpath "//*[@id='login-form']/button"
   And input user credentials
  When login button is clicked
  Then element with id "sn-group" should be visible
   And account type should be "WAREHOUSING" in element with id "/html/body/div[1]/div/div[2]/div[1]/div[1]/span"

 @logout
 Scenario Outline:[UP_S_000008 - UP_S_0000011] Account type for user with access level 1 should have access to specific modules
  Given user credentials username "Karl" and password "Dasma"
   And username input field id "username"
   And password input field id "password"
   And login button xpath "//*[@id='login-form']/button"
   And input user credentials
  When login button is clicked
  Then element with id "sn-group" should be visible
   And get displayed modules displayed in element with id "sn-group"
   And "<module>" module should be displayed

  Examples:
   | module    |
   | Warehouse |
   | Receiving |
   | Releasing |
   | Reports   |
