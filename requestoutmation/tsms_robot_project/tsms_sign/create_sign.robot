*** Settings ***
Documentation    Suite description
Library  robot_commons.tsms_base.Tsmstest
Library  robot_commons.tsms_base
Library  robot_commons.tsms_db.OperationDb
Library  robot_commons.tsms_db

*** Test Cases ***
test_01
    [Tags]  level1    #标记，定义用例级别，执行用例时可选定执行指定标记的用例；可定义多个标记
    ${signature}    gen ranstr    num_letters=${5}
    ${data}    create dictionary    signature=${signature}    source=shenzhen    pics=cc
    req post    sign  ${data}

test_02
    ${signature}    gen ranstr    num_letters=${5}
    ${data}    set variable  {"signature": "${signature}","source": "shenzhen","pics": ["cc"]}
    req post  sign    ${data}

test_03
    #发送信息成功
    [Tags]  level2


