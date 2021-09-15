@echo off

echo "[BAT] 连接虚拟机，获取dtest固件"
python -u "d:\workspace\vsc\python\ssh\ssh_linux.py"
IF %ERRORLEVEL% NEQ 0 (
    echo "[BAT] dtest固件获取失败"
    EXIT /B 1
)

echo "[BAT] 执行测试程序"
pushd "D:\workspace\vsc\python\kl3-test-tool"
python -u "kl3-test-tool.py" "auto"
IF %ERRORLEVEL% NEQ 0 (
    echo "[BAT] 测试程序执行失败"
    EXIT /B 1)
popd

echo "[BAT] 判断测试结果"
pushd "D:\workspace\vsc\python\ssh\dtest_file"
copy /y "result.txt" "C:\Users\大雄\.jenkins\workspace\kunlun_test\result.txt"
findstr "FAILED" result.log
IF %ERRORLEVEL% NEQ 0 (
    echo "[BAT] 未找到 FAILED 字段，测试通过"
    EXIT /B 0
) ELSE (
    echo "[BAT] 找到 FAILED 字段，测试未通过"
    EXIT /B 1
)
popd