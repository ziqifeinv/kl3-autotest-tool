import os
import sys
import re
import datetime
import paramiko
import shutil
from paramiko import channel

host_ip = "10.0.1.111"
host_name = "daxiong"
host_passwd = "5555"
host_cmd = """
    export PATH=$PATH:/opt/riscv_env/bin/;
    cd share/kunlun-private/iotelic/kunlun/Mainline/build/;
    git checkout master_dtest;
    ./build_dtest_kl3.sh
"""
# 这里不适用“git rev-parse HEAD”，获取到的是本地合并之后的commit id，与库上的不符合，
# 需要抽取merge id，这里考虑是内部邮件，直接打印近两天的提交
host_cmd_commit_id = """
    cd share/kunlun-private/iotelic/kunlun/Mainline/build/;
    git log --since=2.days
"""
# 目前仅拷贝xxx.bin文件，
# 约定拷贝的文件存放于脚本所在目录下的dtest_file目录下，以单独的bin文件存在
path_dtest_kl3 = "/home/daxiong/share/kunlun-private/iotelic/kunlun/Mainline/dtest/dtest3/"
path_dtest_build = "/.output/lib/"
list_dtest_kl3 = [
    "unit_test_sfc",
    "unit_test_smc",
]

# -------------------------------建立ssh连接------------------------------------
print("开始ssh连接服务器")
# 建立一个sshclient对象
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
try:
    # 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 调用connect方法连接服务器
    ssh.connect(hostname=host_ip, port=22, username=host_name,
        password=host_passwd, timeout=5)
except paramiko.SSHException as e_ssh:
    print(e_ssh)
    print("%s@%s SSH连接失败" % (host_ip, host_name))
    sys.exit(1)
except Exception as e:
    print(e)
    print("%s@%s 连接失败" % (host_ip, host_name))
    sys.exit(2)
print("%s@%s 连接成功" % (host_ip, host_name))

# -------------------------------远程执行命令-----------------------------------
print("开始执行指令：", host_cmd)
try:
    build_fail = 0
    # 执行命令,结果放到stdout中，如果有错误将放到stderr中
    stdin, stdout, stderr = ssh.exec_command(host_cmd, get_pty=False)
    for line in iter(stdout.readline,""):
        if re.search("failed", line):
            build_fail = 1
        print(line, end="")
except paramiko.SSHException as e_ssh:
    print(e_ssh)
    print("命令[%s]执行失败" % (host_cmd))
    sys.exit(3)
except Exception as e:
    print(e)
    print("命令[%s]执行异常" % (host_cmd))
    sys.exit(4)
if build_fail:
    print("固件编译失败")
    sys.exit(5)
print("固件编译成功")

# -------------------------------拷贝编译文件-----------------------------------
print("开始拷贝文件")
port_trans = ssh.get_transport()
port_sftp = paramiko.SFTPClient.from_transport(port_trans)
# 目前仅拷贝xxx.bin文件
path_pwd = os.path.split(os.path.realpath(__file__))[0]
dir_dtest = os.path.join(path_pwd, "dtest_file")
if os.path.exists(dir_dtest):
    shutil.rmtree(dir_dtest)
os.makedirs(dir_dtest)
timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
for dtest in list_dtest_kl3:
    path_remote = path_dtest_kl3 + dtest + path_dtest_build + dtest + ".bin"
    dir_local = os.path.join(path_pwd, "history", timestamp, dtest)
    if not os.path.exists(dir_local):
        os.makedirs(dir_local)
    path_local = os.path.join(dir_local, dtest) + ".bin"
    print("remote path:", path_remote)
    print("local path:", path_local)
    try:
        port_sftp.get(path_remote, path_local)
    except Exception as e:
        print("文件拷贝失败", e)
        sys.exit(6)
    shutil.copy(path_local, dir_dtest)

# -------------------------------远程执行命令,获取commit id----------------------
print("开始执行指令：", host_cmd_commit_id)
info_commit = ""
try:
    build_fail = 0
    # 执行命令,结果放到stdout中，如果有错误将放到stderr中
    stdin, stdout, stderr = ssh.exec_command(host_cmd_commit_id, get_pty=False)
    for line in iter(stdout.readline,""):
        info_commit += line
    print("获取到commit id：", info_commit)
except paramiko.SSHException as e_ssh:
    print(e_ssh)
    print("命令[%s]执行失败" % (host_cmd_commit_id))
except Exception as e:
    print(e)
    print("命令[%s]执行异常" % (host_cmd_commit_id))
if build_fail:
    print("获取commit id失败")
print("获取commit id成功")
# 写入文件，用于附加到测试结果邮件中
path_commit_id = os.path.join(os.getcwd(), "dtest_file", "commit_info.log")
try:
    fd_commit = open(path_commit_id, "w")
except Exception as e:
    print("文件 %s 打开失败，原因：" % (path_commit_id), e)
fd_commit.write(info_commit)
fd_commit.close()

# -------------------------------关闭连接----------------------------------------
# 关闭连接
ssh.close()
print("脚本执行完成")
sys.exit(0)
