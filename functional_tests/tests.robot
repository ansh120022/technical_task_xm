*** Settings ***
Library    RequestsLibrary
Library    Collections


*** Variables ***
${api_url}=     http://0.0.0.0:80

*** Test Cases ***
positiveTest
    ${response} =  GET  ${api_url}/people/2/  expected_status=200
    Status Should Be        200
    Dictionary Should Contain Value     ${response.json()}     for any ID passed

negativeTest
    ${response} =  GET  ${api_url}/people/200/       expected_status=404
    Dictionary Should Contain Value     ${response.json()}     Record with ID 200 not found

cornerCase
    ${response} =  GET  ${api_url}/people/string/       expected_status=400
    Dictionary Should Contain Value     ${response.json()}     Incorrect element ID: string. The value should be integer

