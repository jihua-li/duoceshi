*** Settings ***
Documentation    Suite description
Library  robot_commons.tsms_base.Tsmstest
Library  robot_commons.tsms_base
Library  robot_commons.tsms_db.OperationDb
Library  robot_commons.tsms_db
Variables  ../config/tsms_base_config.py
Resource    ../config/tsms_base_conf_robot.robot
*** Variables ***


*** Test Cases ***
test_01
#    log    ${header url}
    log    ${name}
    关键字

test_02
    [Tags]  level1

    ${data}    set variable    {"sign_id": ${542}, "temp_id": ${56}, "mobiles": [16757836209]}
    req post  message    ${data}
#    ${uuid}    get tsms uuid    #获取uuid
    ${uuid}    get t id
    check status code    200
    check tsms uuid
    ${real_res}    tsms select    sms_send    mobile,status,consume    uuid=${uuid}
    check_res    mobile    16757836209
    check_res    status    sending
    check_res    consume    1




*** Keywords ***
关键字
    log    ${header url}

