Feature: TS_00001 Login Page
 Scenario: Title should be properly set
  Given website url "http://127.0.0.1:8080"
  When accessing the website
  Then title should be "Mamsar Inventory & Monitoring System"

 Scenario: Login should fail providing empty credentials
  Given unregistered user credentials username "None" and password "None"
   And username input field id "username"
   And password input field id "password"
   And login button xpath "//*[@id='login-form']/button"
   And input user credentials
  When login button is clicked
  Then console log should not be empty
   And "Empty fields!" should be thrown in console log

 Scenario: Login should fail for unregistered users
  Given unregistered user credentials username "user1" and password "password"
   And username input field id "username"
   And password input field id "password"
   And login button xpath "//*[@id='login-form']/button"
   And input user credentials
  When login button is clicked
  Then console log should not be empty
   And "login error!" should be thrown in console log

 Scenario: Login should fail for correct username but wrong password
  Given unregistered user credentials username "Kasper" and password "wrong_password"
   And username input field id "username"
   And password input field id "password"
   And login button xpath "//*[@id='login-form']/button"
   And input user credentials
  When login button is clicked
  Then console log should not be empty
   And "login error!" should be thrown in console log

 Scenario: Login should fail for wrong username but correct password
  Given unregistered user credentials username "Kasper" and password "wrong_password"
   And username input field id "username"
   And password input field id "password"
   And login button xpath "//*[@id='login-form']/button"
   And input user credentials
  When login button is clicked
  Then console log should not be empty
   And "login error!" should be thrown in console log

 Scenario: Successful login for users with correct credentials
  Given unregistered user credentials username "Kasper" and password "Cain"
   And username input field id "username"
   And password input field id "password"
   And login button xpath "//*[@id='login-form']/button"
   And input user credentials
  When login button is clicked
  Then element with id "btn-logout" should be visible
   And element with id "sn-group" should be visible
