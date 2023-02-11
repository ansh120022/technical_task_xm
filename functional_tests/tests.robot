*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Test Cases ***
positiveTest
    ${response} =  GET  %{TEST_APP_URL}/people/20/  expected_status=200
    Status Should Be        200
    Dictionary Should Contain Value     ${response.json()}     for any ID passed

negativeTest
    ${response} =  GET  %{TEST_APP_URL}/people/200/       expected_status=404
    Dictionary Should Contain Value     ${response.json()}     Record with ID 200 not found

cornerCase
    ${response} =  GET  %{TEST_APP_URL}/people/string/       expected_status=400
    Dictionary Should Contain Value     ${response.json()}     Incorrect element ID: string. The value should be integer

