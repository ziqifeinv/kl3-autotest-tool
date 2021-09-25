import os

list_dir = os.listdir("./history/")

print(list_dir)

str_test = "[start]"

if str_test.find("START") > 0:
    print("找到大写的start")
if str_test.find("start") > 0:
    print("找到小写的start")

str_test = "[RESULT] - UNIT_SMC : SUCCEED"
if str_test.find("fail") > 0 or str_test.find("FAIL") > 0:
    result = "FAILED"
else:
    result = "SUCCEED"
print(" 执行结果：", result)

dir_script = os.getcwd()
print("current dir:", dir_script)