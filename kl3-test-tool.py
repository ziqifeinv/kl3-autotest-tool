#通用库
import os
import sys
import codecs
import numpy
import serial
import time
import datetime
from serial.serialutil import Timeout
import serial.tools.list_ports
from logging import exception, warning
from xml.dom import minidom
import xmodem
from multiprocessing import Process, Queue, freeze_support

#QT库
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QCursor, QColor
from PyQt5.QtWidgets import QApplication, QMenu, QMessageBox, QFileDialog, QColorDialog
from PyQt5.QtWidgets import QTableWidgetItem, QTreeWidgetItem, QHeaderView
from PyQt5.QtCore import QTimer
from xmb import Ui_MainWindow
from config import Ui_config

#全局变量，这里当做宏定义使用
g_file_name_dtest_xml = "dtest.xml"
g_module_connect_key = b"WQKL"
g_module_connected_key = b"C"
# g_module_connected_key = b"Recieving RAM-IMAGE in xmodem : C"
g_module_relay_on_key = bytes.fromhex('FF0F0000000801FF301D')
g_module_relay_off_key = bytes.fromhex('FF0F000000080100705D')
g_module_log_key_reboot = "[REBOOT]"
g_module_log_key_info = "[INFO]"
g_module_log_key_start = "[START]"
g_module_log_key_result = "[RESULT]"
g_module_log_key_data = "[DATA]"
g_rule_number = 20

#考虑到涉及xml配置信息时都需要读取minidom和treewidget，采用变量保存信息能提高效率
#python可以使用numpy定义结构体，相当与字典，但是没有append方法，所以采用列表，下标固定
g_idx_name = 0      #dtest节点name下标
g_idx_note = 1      #dtest节点note下标
g_idx_eb = 2        #dtest节点enable下标
g_idx_slave = 3     #dtest节点slave_mode下标
g_idx_name_c = 0    #case节点name下标
g_idx_note_c = 1    #case节点note下标
g_idx_eb_c = 2      #case节点enable下标
#关键字规则采用list保存，为了方便后续拓展，下标使用固定数值
g_idx_rule_key = 0
g_idx_rule_color = 1
g_idx_rule_eb = 2

#状态机对应的状态
g_fsm_free = 0
g_fsm_connect = 1
g_fsm_download = 2
g_fsm_running = 3

# 消息弹窗对应的消息类型
g_msg_about = 0
g_msg_crirical = 1
g_msg_info = 2
g_msg_question = 3
g_msg_warning = 4

#这里的全局变量用于xmodem操作，保存2个下载串口的句柄
g_port_xmodex = []

#这是是用于给子进程抛消息的队列
g_list_queue = []

#这里的全局函数也是为了给xmodem使用
def xmodem_transf_0_getc(size, timeout = 1):
    return g_port_xmodex[0].read(size) or None
def xmodem_transf_0_putc(data, timeout = 1):
    return g_port_xmodex[0].write(data)
def xmodem_transf_0_callback(total, succeed, failed):
    if total % 10 == 0:
        print(".", end='')

def xmodem_transf_1_getc(size, timeout = 1):
    return g_port_xmodex[1].read(size) or None
def xmodem_transf_1_putc(data, timeout = 1):
    return g_port_xmodex[1].write(data)
def xmodem_transf_1_callback(total, succeed, failed):
    if total % 10 == 0:
        print(".", end='')

def process_log_file_write(g_list_queue):
    msg_process = ""    # python子进程不能使用print(stdout)，所以打印到文件
    dir_script = os.getcwd()    # 当前脚本所在目录
    # 创建debug日志文件和终端日志文件，路径固定为软件所在目录下的log文件夹
    dir_log = os.path.join(dir_script, "log")
    path_debug = dir_log +  "\\debug " + \
        datetime.datetime.now().strftime('%Y-%m-%d %H%M%S') + ".log"
    path_terminal = dir_log +  "\\terminal " + \
        datetime.datetime.now().strftime('%Y-%m-%d %H%M%S') + ".log"

    # 每个dtest打印单独存为一个log文件，位于history目录下时间戳最新的子目录下
    # os.listdir是名称从小到大返回列表
    dir_dtest_history = os.path.join(dir_script, "history")
    dir_dtest_list = os.listdir(dir_dtest_history)
    dir_dtest = dir_dtest_list[len(dir_dtest_list) - 1]

    if not os.access(dir_log, os.F_OK):
        msg_process = "创建log目录: " + dir_log + "\r\n"
        os.mkdir(dir_log)
    fd_debug = codecs.open(path_debug, 'w', 'utf-8')
    fd_terminal = codecs.open(path_terminal, 'w', 'utf-8')
    fd_dtest = None

    while True:
        if g_list_queue[0].full():
            msg_process += "调试log队列已满！！！\r\n"

        if not g_list_queue[1].empty():
            if g_list_queue[1].full():
                msg_process += "终端队列已满！！！\r\n"
            msg = g_list_queue[1].get()
            msg = str(msg).replace("\r\n", "")
            # 写入单独的log文件
            if not g_list_queue[2].empty():
                if fd_dtest:
                    fd_dtest.close()
                name_dtest = g_list_queue[2].get()
                name_dtest = str(name_dtest).replace(".bin", "")
                path_dtest_log = os.path.join(dir_dtest_history, dir_dtest,
                    name_dtest, name_dtest + ".log")
                fd_dtest = codecs.open(path_dtest_log, 'w', 'utf-8')
                msg_process += "创建" + name_dtest + "对应的log文件，路径:" + \
                    path_dtest_log + "\r\n"
            if fd_dtest:
                # msg_process += "写入单独的log文件:" + msg + "\r\n"
                fd_dtest.write(msg)
                fd_dtest.flush()
            # 写入总的log文件
            fd_terminal.write(msg)
            fd_terminal.flush()
        # 写入调试日志
        if not g_list_queue[0].empty():
            msg = g_list_queue[0].get()
            fd_debug.write(msg + "\r\n")
            fd_debug.flush()
        if len(msg_process):
            fd_debug.write(msg_process + "\r\n")
            fd_debug.flush()
            msg_process = ""

class kl3_test_app(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, argv):
        self.auto_test_mode = 0
        if len(argv) > 1:
            if argv[1] == "auto":
                self.auto_test_mode = 1
        print("init argv:", argv, ", auto test mode:", self.auto_test_mode)
        super(kl3_test_app, self).__init__()  #super调用父类的构造函数
        self.setupUi(self)
        #配置主界面标题栏
        self.setWindowTitle("kl3 dtest测试工具 V1.0")
        #使能debug、终端文本框只读属性
        self.edit_debug.setReadOnly(True)
        self.edit_terminal.setReadOnly(True)
        #dtest\case\rule设置表头宽度自适应，不能手动更改（表头由设计工具直接产生）
        self.widget_dtest.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.widget_case.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.widget_rule.horizontalHeader().setSectionResizeMode(\
            0, QHeaderView.ResizeToContents)
        self.widget_rule.horizontalHeader().setSectionResizeMode(\
            1, QHeaderView.ResizeToContents)
        self.widget_rule.horizontalHeader().setSectionResizeMode(\
            2, QHeaderView.ResizeToContents)
        self.widget_rule.horizontalHeader().setSectionResizeMode(\
            3, QHeaderView.Stretch)
        self.widget_rule.setRowCount(g_rule_number)    #需要先设置行数，默认0行不显示
        #使能dtest和case界面右键菜单
        self.widget_dtest.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.widget_case.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #连接按键信号与槽函数
        self.pbt_cfg.clicked.connect(self.pbt_handle_cfg)
        self.pbt_start_test.clicked.connect(self.pbt_handle_test_act)
        self.widget_dtest.customContextMenuRequested.connect(
            lambda: self.mouse_handle_widget_right_clicked(QCursor.pos(), 0))
        self.widget_case.customContextMenuRequested.connect(
            lambda: self.mouse_handle_widget_right_clicked(QCursor.pos(), 1))
        #dtest、case、rule界面在初始化时会触发itemchanged信号，
        # 因此itemchanged信号会在xml_file_load函数中解绑并重新绑定
        self.widget_dtest.itemChanged.connect(self.tree_widget_item_changed_handle)
        self.widget_case.itemChanged.connect(self.tree_widget_item_changed_handle)
        self.widget_rule.cellChanged.connect(self.table_widget_cell_changed)
        self.widget_rule.cellClicked.connect(self.table_widget_cell_clicked)
        #连接动作信号与槽函数
        self.act_debug_visible.triggered.connect(
            lambda: self.act_handle_debug_interface_config(0))
        self.act_debug_invisible.triggered.connect(
            lambda: self.act_handle_debug_interface_config(1))
        self.act_sel_all.triggered.connect(
            lambda: self.act_handle_option_select(QApplication.focusWidget(), 2))
        self.act_sel_none.triggered.connect(
            lambda: self.act_handle_option_select(QApplication.focusWidget(), 0))
        self.act_load.triggered.connect(lambda: self.act_handle_xml_file_open_save(0))
        self.act_save.triggered.connect(lambda: self.act_handle_xml_file_open_save(1))
        self.act_save_as.triggered.connect(lambda: self.act_handle_xml_file_open_save(2))
        #配置界面实例化，连接信号与槽
        self.cfg = Ui_config()
        self.ui_cfg = QtWidgets.QDialog(self)
        self.cfg.setupUi(self.ui_cfg)
        self.ui_cfg.setWindowTitle("配置")
        self.cfg.pbt_box_cfg.accepted.connect(self.pbt_handle_cfg_accept)
        self.cfg.pbt_box_cfg.rejected.connect(self.pbt_handle_cfg_reject)
        self.cfg.pbt_sel_file_0.clicked.connect(
            lambda: self.pbt_handle_cfg_file_select(0))
        self.cfg.pbt_sel_file_1.clicked.connect(
            lambda: self.pbt_handle_cfg_file_select(1))
        #IO操作比较费时，会导致界面刷新缓慢，改为使用队列+子进程方式实现写文件
        g_list_queue.append(Queue(300)) # 软件调试打印队列
        g_list_queue.append(Queue(300)) # dtest日志打印队列
        g_list_queue.append(Queue(5))   # 当前dtest名称队列
        thread_log = Process(target=process_log_file_write, args=(g_list_queue,))
        thread_log.daemon = True
        thread_log.start()
        #手动模式时标准输出重定向到界面，自动测试模式时输出到标准输出（jenkins）
        if self.auto_test_mode:
            #自动测试模式时隐藏调试窗口
            self.widget_debug.setVisible(False)
        else:
            self.stdout_old = sys.stdout
            sys.stdout = self
        #调用初始化函数
        self.init()

    def init(self):
        #结构体定义
        cfg_type = numpy.dtype({
            'names':['fd', 'com', 'baud', 'data', 'parity', 'stop'],
            'formats':['O', 'U32', 'i', 'i', 'U32', 'f']
        })
        #串口列表初始化
        self.init_com_port()
        #4个串口对应的数组，参数初始化为115200，8N1
        self.np_port_info = numpy.array([(0, "", 115200, 8, 0, 0), (0, "", 115200, 8, 0, 0),
            (0, "", 115200, 8, 0, 0), (0, "", 115200, 8, 0, 0)], dtype=cfg_type)
        #固件路径初始化
        self.list_path = ['', '']
        #初始化一个保存xml配置信息的列表
        #格式为[[[dtest1 info1, dtest1 info2], [case info1], [case info2]], [dtest2]]
        self.list_dtest_info = []
        #初始化关键字规则信息，格式为[[keyword1, color1, enable1], [keyword2...]]
        self.list_rule_info = []
        #dtest固件配置xml读取
        self.xml_file_load('')
        #初始化状态机（字典）
        self.fsm = {'dtest':0, 'reboot':0, 'state':0, 'cycle':0}
        #dtest测试采用timer+状态机的方式（进程while1和sleep会导致界面卡死）
        self.timer = QTimer()
        self.timer.timeout.connect(self.test_fsm_handle)
        if self.auto_test_mode:
            # 模拟触发开始测试按钮
            print("开始自动测试")
            self.pbt_handle_test_act()

    def init_com_port(self):
        #当前串口列表初始化，使用列表获取，没有则退出程序，有则私有字典保存com口字符串
        self.dict_com = {}
        list_com_temp = list(serial.tools.list_ports.comports())
        if len(list_com_temp) <= 0:
            print("未发现串口，程序退出")
            self.msg_box_show(g_msg_warning, "未发现串口")
            exit(1)
        self.cfg.combo_com_0.addItem('')
        self.cfg.combo_com_1.addItem('')
        self.cfg.combo_com_2.addItem('')
        self.cfg.combo_com_3.addItem('')
        for port in list_com_temp:
            self.dict_com["%s" % port[0]] = "%s" % port[1]
            self.cfg.combo_com_0.addItem(port[0])
            self.cfg.combo_com_1.addItem(port[0])
            self.cfg.combo_com_2.addItem(port[0])
            self.cfg.combo_com_3.addItem(port[0])
        print("串口列表: %s" % self.dict_com)

    def xml_file_load(self, path_file):
        if (len(path_file) == 0):   #传参为空，则使用默认文件
            print("使用默认文件(%s)" % g_file_name_dtest_xml)
            path_file = os.getcwd() + "\\" + g_file_name_dtest_xml
        if not os.access(path_file, os.F_OK | os.R_OK):
            msg = "文件不存在或不可读：\n" + path_file
            print(msg)
            self.msg_box_show(g_msg_warning, msg)
            return
        else:
            #清空界面和相关列表
            print("清空dtest、case和rule配置界面，清空列表内容")
            # self.widget_case.setHeaderHidden(True)
            self.widget_dtest.clear()
            self.widget_case.clear()
            self.widget_rule.clearContents()
            # self.list_dtest_info.clear()
            self.list_dtest_info = []
            self.list_rule_info = []
            self.path_xml_file = path_file
        #解绑信号，防止在加载xml过程中更新界面触发信号
        self.widget_dtest.itemChanged.disconnect(self.tree_widget_item_changed_handle)
        self.widget_case.itemChanged.disconnect(self.tree_widget_item_changed_handle)
        self.widget_rule.cellChanged.disconnect(self.table_widget_cell_changed)
        #读取xml文件
        cnt_dtest = 0
        cnt_case = 0
        self.xml_tree = minidom.parse(path_file)
        root = self.xml_tree.documentElement
        #读取debug界面使能信息
        debug_interface_eb = root.getElementsByTagName("debug_interface")[0].firstChild.data
        print("从xml文件中读取到的调试界面使能信息：%s" % debug_interface_eb)
        if debug_interface_eb == "false":   #默认是打开的
            self.act_handle_debug_interface_config(0)
        #读取关键字规则信息并显示
        rules = root.getElementsByTagName("rule")
        for i in range(0, g_rule_number):
            # id_rule = int(rule.getAttribute("id"))
            id_rule = i
            item_rule = QTableWidgetItem("", 0)
            item_rule.setCheckState(QtCore.Qt.Unchecked)
            keyword = ""
            color_str = "#000000"
            eb = "false"
            if i < len(rules):
                if rules[i].getElementsByTagName("keyword")[0].hasChildNodes():
                    keyword = rules[i].getElementsByTagName("keyword")[0].childNodes[0].data
                color_str = rules[i].getElementsByTagName("color")[0].childNodes[0].data
                eb = rules[i].getElementsByTagName("enable")[0].childNodes[0].data
                if eb == "true":
                    item_rule.setCheckState(QtCore.Qt.Checked)
            self.list_rule_info.append([keyword, color_str, eb])
            self.widget_rule.setItem(id_rule, 0, item_rule)
            item_rule = QTableWidgetItem("0", 1)
            item_rule.setFlags(item_rule.flags() & (~QtCore.Qt.ItemIsEditable))
            self.widget_rule.setItem(id_rule, 1, item_rule)
            color = QColor(color_str)
            item_rule = QTableWidgetItem("", 0)
            item_rule.setBackground(color)
            self.widget_rule.setItem(id_rule, 2, item_rule)
            self.widget_rule.setItem(id_rule, 3, QTableWidgetItem(keyword, 3))
        print("从xml文件中读取的关键字规则信息：", self.list_rule_info)
        #读取串口信息
        ports = root.getElementsByTagName("port")
        for port in ports:
            # if port.hasChildNodes():
            id_port = int(port.getAttribute("id"))
            if port.getElementsByTagName("com")[0].hasChildNodes():
                self.np_port_info[id_port]['com'] = \
                    port.getElementsByTagName("com")[0].childNodes[0].data
            self.np_port_info[id_port]['baud'] = \
                port.getElementsByTagName("baud")[0].childNodes[0].data
            self.np_port_info[id_port]['data'] = \
                port.getElementsByTagName("data")[0].childNodes[0].data
            self.np_port_info[id_port]['parity'] = \
                port.getElementsByTagName("parity")[0].childNodes[0].data
            self.np_port_info[id_port]['stop'] = \
                port.getElementsByTagName("stop")[0].childNodes[0].data
        print("从xml文件中读取的串口信息：", self.np_port_info)
        #获取路径信息
        self.list_path[0] = root.getElementsByTagName("dir")[0].firstChild.data
        if root.getElementsByTagName("dir")[1].hasChildNodes():
            self.list_path[1] = root.getElementsByTagName("dir")[1].firstChild.data
        print("从xml文件中读取的文件夹地址:", self.list_path)
        #读取dtest信息
        dtests = root.getElementsByTagName("dtest")
        for dtest in dtests:
            cnt_dtest += 1
            id_dtest = int(dtest.getAttribute("id"))
            name = dtest.getElementsByTagName("name")[0].childNodes[0].data
            note = dtest.getElementsByTagName("note")[0].childNodes[0].data
            eb = dtest.getElementsByTagName("enable")[0].childNodes[0].data
            slave = dtest.getElementsByTagName("slave_mode")[0].childNodes[0].data
            print("找到第%d个dtest\n\tname:%s\n\tnote:%s\n\tenable:%s\n"
                "\tslave:%s" % (id_dtest, name, note, eb, slave))
            self.list_dtest_info.append([])
            self.list_dtest_info[id_dtest].append([name, note, eb, slave])
            #添加dtest和case界面，还有一种方法是添加一个check box，选中时可以触发信号
            item_dtest = QTreeWidgetItem(self.widget_dtest)
            item_dtest.setText(0, str(id_dtest))
            item_dtest.setText(1, name)
            item_case_1 = QTreeWidgetItem(self.widget_case)
            item_case_1.setText(0, str(id_dtest))
            item_case_1.setText(1, name)
            if (eb == "true"):
                item_dtest.setCheckState(0, QtCore.Qt.Checked)
            else:
                item_dtest.setCheckState(0, QtCore.Qt.Unchecked)
            item_case_1.setCheckState(0, QtCore.Qt.Unchecked)
            item_case_1.setExpanded(True)   #默认展开
            #case界面填充
            for node in dtest.getElementsByTagName("case"):
                if node.hasChildNodes():
                    cnt_case += 1
                    id_case = int(node.getAttribute("id"))
                    name_case = node.getElementsByTagName("name")[0].childNodes[0].data
                    note_case = node.getElementsByTagName("note")[0].childNodes[0].data
                    eb_case = node.getElementsByTagName("enable")[0].childNodes[0].data
                    print("第%d个case，enable:%s, name:%s, note:%s" %
                        (id_case, eb_case, name_case, note_case))
                    self.list_dtest_info[id_dtest].append([name_case, note_case, eb_case])
                    item_case_2 = QTreeWidgetItem(item_case_1)
                    item_case_2.setText(0, str(id_case))
                    item_case_2.setText(1, name_case)
                    if eb_case == "true":
                        item_case_2.setCheckState(0, QtCore.Qt.Checked)
                    else:
                        item_case_2.setCheckState(0, QtCore.Qt.Unchecked)
        print("dtest信息：", self.list_dtest_info)
        #连接界面信号与槽
        self.widget_dtest.itemChanged.connect(self.tree_widget_item_changed_handle)
        self.widget_case.itemChanged.connect(self.tree_widget_item_changed_handle)
        self.widget_rule.cellChanged.connect(self.table_widget_cell_changed)

    def xml_file_save(self, path):
        #更新dom tree中dir、dtest、port、rule部分
        root = self.xml_tree.documentElement
        #由于存在较多空行，会导致生成的xml文件有较多空行，这里选择删除
        nodes = root.childNodes
        i = 0
        while(i < nodes.length):
            if nodes[i].nodeType == minidom.Node.TEXT_NODE \
                and str(nodes[i].data).find("\n") >= 0:
                root.removeChild(nodes[i])
            else:
                nodes_son = nodes[i].childNodes
                j = 0
                while j < nodes_son.length:
                    if nodes_son[j].nodeType == minidom.Node.TEXT_NODE \
                        and str(nodes_son[j].data).find("\n") >= 0:
                        nodes[i].removeChild(nodes_son[j])
                    else:
                        nodes_grandson = nodes_son[j].childNodes
                        m = 0
                        while m < nodes_grandson.length:
                            if nodes_grandson[m].nodeType == minidom.Node.TEXT_NODE \
                                and str(nodes_grandson[m].data).find("\n") >= 0:
                                nodes_son[j].removeChild(nodes_grandson[m])
                            else:
                                m += 1
                        j += 1
                i += 1
        #调试界面使能flag不采用变量保存，而是直接读取界面状态
        debug_interface = root.getElementsByTagName("debug_interface")
        eb = "true" if self.widget_debug.isVisible() else "false"
        debug_interface[0].firstChild.data = eb

        dirs = root.getElementsByTagName("dir")
        for i in range(len(self.list_path)):
            if dirs[i].hasChildNodes():
                dirs[i].firstChild.data = self.list_path[i]
            else:
                if len(self.list_path[i]):
                   dir_text =  self.xml_tree.createTextNode(self.list_path[i])
                   dirs[i].appendChild(dir_text)

        dtests = root.getElementsByTagName("dtest")
        for i in range(0, len(self.list_dtest_info)):
            dtests[i].getElementsByTagName("enable")[0].firstChild.data = \
                self.list_dtest_info[i][0][g_idx_eb]
            for j in range(1, len(self.list_dtest_info[i])):
                dtests[i].getElementsByTagName("case")[j -1]\
                    .getElementsByTagName("enable")[0].firstChild.data = \
                    self.list_dtest_info[i][j][g_idx_eb_c]

        ports = root.getElementsByTagName("port")
        for i in range(0, len(self.np_port_info)):
            if ports[i].getElementsByTagName("com")[0].hasChildNodes():
                ports[i].getElementsByTagName("com")[0].firstChild.data = \
                    self.np_port_info[i]['com']
            else:
                com_text = self.xml_tree.createTextNode(self.np_port_info[i]['com'])
                ports[i].getElementsByTagName("com")[0].appendChild(com_text)
            ports[i].getElementsByTagName("baud")[0].firstChild.data = \
                self.np_port_info[i]['baud']
            ports[i].getElementsByTagName("data")[0].firstChild.data = \
                self.np_port_info[i]['data']
            ports[i].getElementsByTagName("parity")[0].firstChild.data = \
                self.np_port_info[i]['parity']
            ports[i].getElementsByTagName("stop")[0].firstChild.data = \
                self.np_port_info[i]['stop']

        rules = root.getElementsByTagName("rule")
        for i in range(0, len(self.list_rule_info)):
            rule_num_xml = len(rules)
            if i < rule_num_xml:
                if rules[i].getElementsByTagName("keyword")[0].hasChildNodes():
                    rules[i].getElementsByTagName("keyword")[0].firstChild.data = \
                        self.list_rule_info[i][g_idx_rule_key]
                else:
                    keyword_text = self.xml_tree.createTextNode(\
                        self.list_rule_info[i][g_idx_rule_key])
                    rules[i].getElementsByTagName("keyword")[0].appendChild(keyword_text)
                rules[i].getElementsByTagName("color")[0].firstChild.data = \
                    self.list_rule_info[i][1]
                rules[i].getElementsByTagName("enable")[0].firstChild.data = \
                    self.list_rule_info[i][2]
            else:
                # if self.list_rule_info[i][g_idx_rule_eb] == "false":
                #     continue
                rule_new = self.xml_tree.createElement("rule")
                rule_new.setAttribute("id", str(i))
                keyword = self.xml_tree.createElement("keyword")
                keyword_text = self.xml_tree.createTextNode(\
                    self.list_rule_info[i][g_idx_rule_key])
                keyword.appendChild(keyword_text)
                color = self.xml_tree.createElement("color")
                color_text = self.xml_tree.createTextNode(\
                    self.list_rule_info[i][g_idx_rule_color])
                color.appendChild(color_text)
                eb = self.xml_tree.createElement("enable")
                eb_text = self.xml_tree.createTextNode(\
                    self.list_rule_info[i][g_idx_rule_eb])
                eb.appendChild(eb_text)
                rule_new.appendChild(keyword)
                rule_new.appendChild(color)
                rule_new.appendChild(eb)
                root.appendChild(rule_new)
        #保存xml文件，使用w模式打开，如文件存在则新建文件
        # fd_xml = open(path, 'w')
        fd_xml = codecs.open(path, 'wb', 'utf-8')   #这里必须用codecs.open指定编码
        if fd_xml == None:
            msg = path + " 文件打开失败"
            print(msg)
            self.msg_box_show(g_msg_warning, msg)
            return
        self.xml_tree.writexml(fd_xml, indent='',
            addindent='    ', newl='\n', encoding='UTF-8')
        # self.xml_tree.writexml(fd_xml, encoding='utf-8')
        fd_xml.close()
        return

    def pbt_handle_cfg(self):
        print("配置按钮被按下")
        print("默认窗口配置：", self.np_port_info)
        #某些配置选项置为默认值
        self.cfg.combo_com_0.setCurrentText(self.np_port_info[0]['com'])
        self.cfg.combo_com_1.setCurrentText(self.np_port_info[1]['com'])
        self.cfg.combo_com_2.setCurrentText(self.np_port_info[2]['com'])
        self.cfg.combo_com_3.setCurrentText(self.np_port_info[3]['com'])
        self.cfg.combo_baud_0.setCurrentText(str(self.np_port_info[0]['baud']))
        self.cfg.combo_baud_1.setCurrentText(str(self.np_port_info[1]['baud']))
        self.cfg.combo_baud_2.setCurrentText(str(self.np_port_info[2]['baud']))
        self.cfg.combo_baud_3.setCurrentText(str(self.np_port_info[3]['baud']))
        self.cfg.combo_data_0.setCurrentText(str(self.np_port_info[0]['data']))
        self.cfg.combo_data_1.setCurrentText(str(self.np_port_info[1]['data']))
        self.cfg.combo_data_2.setCurrentText(str(self.np_port_info[2]['data']))
        self.cfg.combo_data_3.setCurrentText(str(self.np_port_info[3]['data']))
        self.cfg.edit_fw_path_0.setText(str(self.list_path[0]))
        self.cfg.edit_fw_path_1.setText(str(self.list_path[1]))
        self.ui_cfg.show()

    def pbt_handle_cfg_accept(self):
        slave_take_effect = 0
        list_cfg_valid = [0, 0]
        print("配置界面 确定 按钮被按下，获取配置参数")
        #串口0
        self.np_port_info[0]['com'] = self.cfg.combo_com_0.currentText()
        self.np_port_info[0]['baud'] = int(self.cfg.combo_baud_0.currentText())
        self.np_port_info[0]['data'] = int(self.cfg.combo_data_0.currentText())
        self.np_port_info[0]['parity'] = self.cfg.combo_parity_0.currentText()
        self.np_port_info[0]['stop'] = float(self.cfg.combo_stop_0.currentText())
        #串口1
        self.np_port_info[1]['com'] = self.cfg.combo_com_1.currentText()
        self.np_port_info[1]['baud'] = int(self.cfg.combo_baud_1.currentText())
        self.np_port_info[1]['data'] = int(self.cfg.combo_data_1.currentText())
        self.np_port_info[1]['parity'] = self.cfg.combo_parity_1.currentText()
        self.np_port_info[1]['stop'] = float(self.cfg.combo_stop_1.currentText())
        #串口2
        self.np_port_info[2]['com'] = self.cfg.combo_com_2.currentText()
        self.np_port_info[2]['baud'] = int(self.cfg.combo_baud_2.currentText())
        self.np_port_info[2]['data'] = int(self.cfg.combo_data_2.currentText())
        self.np_port_info[2]['parity'] = self.cfg.combo_parity_2.currentText()
        self.np_port_info[2]['stop'] = float(self.cfg.combo_stop_2.currentText())
        #串口3
        self.np_port_info[3]['com'] = self.cfg.combo_com_3.currentText()
        self.np_port_info[3]['baud'] = int(self.cfg.combo_baud_3.currentText())
        self.np_port_info[3]['data'] = int(self.cfg.combo_data_3.currentText())
        self.np_port_info[3]['parity'] = self.cfg.combo_parity_3.currentText()
        self.np_port_info[3]['stop'] = float(self.cfg.combo_stop_3.currentText())
        print("配置的串口参数：", self.np_port_info)
        #文件路径
        self.list_path[0] = self.cfg.edit_fw_path_0.text();
        self.list_path[1] = self.cfg.edit_fw_path_1.text();
        print("配置的固件路径参数：", self.list_path)
        #判断配置是否合理，要求至少配主模式2个串口和一个文件路径
        if (len(self.np_port_info[0]['com']) == 0
            or len(self.np_port_info[1]['com']) == 0
            or len(self.list_path[0]) == 0):
            print("配置无效，至少需要2个串口和一个路径")
            self.msg_box_show(g_msg_warning, '至少需要配置主模式的\n'
                '2个串口和固件路径')
            list_cfg_valid[0] = 0
        else:
            list_cfg_valid[0] = 1
        #如果配置了从模式，同样需要检查参数是否有效
        if (len(self.np_port_info[2]['com']) > 0
            or len(self.np_port_info[3]['com']) > 0
            or len(self.list_path[1]) > 0):
            slave_take_effect = 1
            if (len(self.np_port_info[2]['com']) == 0
                or len(self.np_port_info[3]['com']) == 0
                or len(self.list_path[1]) == 0):
                print("从模式配置无效，需要配置从模式2个串口和一个路径")
                self.msg_box_show(g_msg_warning, '需要配置从模式的\n'
                    '2个串口和固件路径')
                list_cfg_valid[1] = 0
            else:
                list_cfg_valid[1] = 1
        else:
            list_cfg_valid[1] = 0
        #如果配置无效，则保持配置界面处于最上层
        if (list_cfg_valid[0] == 1
            and list_cfg_valid[1] == slave_take_effect):
            #检查串口是否冲突
            cycle_index = 4 if list_cfg_valid[1] == 1 else 2
            for i in range(0, int(cycle_index / 2)):
                for j in range(0, cycle_index):
                    if self.np_port_info[i]['com'] == self.np_port_info[j]['com']\
                        and i != j:
                        print("串口冲突")
                        self.msg_box_show(g_msg_warning, "串口冲突")
                        return
            #检查路径是否存在，防止手动输入错误路径
            if (os.path.exists(self.list_path[0]) == False
                or os.path.exists(self.list_path[1]) != slave_take_effect):
                print("文件夹路径不存在")
                self.msg_box_show(g_msg_warning, "文件夹不存在")
                return
            self.ui_cfg.close()

    def pbt_handle_cfg_reject(self):
        print("配置界面 取消 按钮被按下")
        self.ui_cfg.close()

    def pbt_handle_cfg_file_select(self, pbt_num):
        print("配置界面 路径选择按钮%d 被按下" % pbt_num)
        path_temp = str(QFileDialog.getExistingDirectory(self,
            '请选择固件所在目录', './', QFileDialog.ShowDirsOnly))
        print("获取到文件夹路径：", path_temp)
        if (os.path.exists(path_temp) == False):
            print("文件夹路径不存在")
            path_temp = ''
        if (len(path_temp) > 0):
            self.list_path[pbt_num] = path_temp
            if (pbt_num == 0):
                self.cfg.edit_fw_path_0.setText(path_temp)
            else:
                self.cfg.edit_fw_path_1.setText(path_temp)

    def pbt_handle_test_act(self):
        list_failed_dtest = []
        list_succeed_dtest = []
        pbt_text = self.pbt_start_test.text()
        print("%s 按钮被按下" % pbt_text)
        if pbt_text == "开始测试":
            if (self.test_start_file_check() < 0) or (self.test_start_port_check() < 0):
                if self.auto_test_mode:
                    exit(1)
                return
            #由于工期紧张，从模块的连接和下载由多线程同时工作更改为顺序执行，下述循环：
            #从模式连接->从模式下载->主模式连接->主模式下载->发送case组合->打印串口
            #【注意】：该流程及后续的流程中存在较多常量下标，以后拓展时需要注意
            #【注意】：由于现有流程在单线程执行且部分流程为死循环，这会导致界面卡住
            self.fsm['state'] = g_fsm_free
            self.fsm['dtest'] = -1
            self.fsm['cycle'] = 0
            self.fsm['reboot'] = 0
            #使用timer+状态机的方式
            self.timer.start(1000)
            self.pbt_start_test.setText("停止测试")
            self.pbt_cfg.setEnabled(False)
            self.edit_cycle_index.setReadOnly(True)
        else:
            self.test_stop_handle()

    def test_fsm_handle(self):
        # print("定时器超时信号触发")
        if self.fsm['state'] == g_fsm_free:
            #获取下一个将要执行的dtest
            overflow = 0
            dtest_n = self.fsm['dtest']
            if not self.fsm['reboot']:
                if self.fsm['dtest'] + 1 >= len(self.list_dtest_info):#一轮执行完毕
                    overflow = 1
                for i in range(dtest_n + 1, len(self.list_dtest_info)):
                    if self.list_dtest_info[i][0][g_idx_eb] == "true":
                        dtest_n = i
                        break
                    if i == len(self.list_dtest_info) - 1:
                        overflow = 1
            if overflow:
                self.fsm['cycle'] += 1
                cycle_curr = self.fsm['cycle']
                cycle_total = int(self.edit_cycle_index.text())
                print("当前循环次数：%d，总循环次数：%d" % (cycle_curr, cycle_total))
                if (cycle_total <= 0) or (cycle_curr < cycle_total):    #下一轮
                    self.fsm['dtest'] = -1
                    self.fsm['state'] = g_fsm_free
                    return
                else:   #所有测试结束
                    print("所有测试执行完毕")
                    self.test_stop_handle()
                    if self.auto_test_mode:
                        exit(0)
                    return
            else:
                self.fsm['state'] = g_fsm_download
                self.fsm['dtest'] = dtest_n
                print("下一个将要执行的dtest编号：%d" % dtest_n)
        elif self.fsm['state'] == g_fsm_download:
            failed_flag = 0
            failed_str = ["从模块连接", "从模块下载", "主模块连接", "主模块下载"]
            #这里部分操作为阻塞模式，因此要先关掉timer
            self.timer.stop()
            dtest_index = self.fsm['dtest']
            name_file = self.list_dtest_info[dtest_index][0][g_idx_name]
            if name_file.rfind(".bin") < 0:
                name_file += ".bin"
            path = self.list_path[0] + "\\" + name_file
            print("开始测试第%d个dtest(%s)，路径：%s" % (dtest_index, name_file, path))
            if self.auto_test_mode:
                g_list_queue[2].put_nowait(name_file)
            if self.list_dtest_info[dtest_index][0][g_idx_slave] == "true":
                name_file_slave = name_file.replace('.', '_slave.')
                path_slave = self.list_path[1] + '\\' + name_file_slave
                print("从模式使能，bin文件：", path_slave)
                if self.test_start_connect_module(self.np_port_info[2]['fd'], \
                    self.np_port_info[3]['fd']):
                    failed_flag = 1
                if failed_flag == 0 and \
                    self.test_start_xmodem_transf_1(self.np_port_info[2]['fd'], \
                    path_slave) < 0:
                    failed_flag = 2
            if failed_flag == 0 and \
                self.test_start_connect_module(self.np_port_info[0]['fd'], \
                self.np_port_info[1]['fd']):
                failed_flag = 3
            if failed_flag == 0 and \
                self.test_start_xmodem_transf_0(self.np_port_info[0]['fd'], path) < 0:
                failed_flag = 4
            if failed_flag:
                print("%s执行失败，原因：%s 失败" % (name_file, failed_str[failed_flag - 1]))
                self.fsm['state'] = g_fsm_free
                self.test_save_dtest_result(name_file.replace(".bin", ""), "FAILED")
                self.timer.start(100)  # start next test
            else:
                self.fsm['state'] = g_fsm_running
                self.fsm_timestamp_download_complete = datetime.datetime.now()
                self.fsm_dtest_running_flag = 0
                self.timer.start(200)
        elif self.fsm['state'] == g_fsm_running:
            complete_flag = 0
            #【TODO】：这里计划增加一个更改串口波特率的流程
            # 10s没有收到数据，则认为dtest执行失败了
            name_dtest = self.list_dtest_info[self.fsm['dtest']][0][g_idx_name]
            if not self.fsm_dtest_running_flag:
                if ((datetime.datetime.now() - self.fsm_timestamp_download_complete).seconds > 10):
                    print("未收到dtest发送的START字段，也许dtest执行失败了")
                    self.test_save_dtest_result(name_dtest, "FAILED")
                    self.fsm['state'] = g_fsm_free
                    self.timer.start(1000)
            #串口接收并打印
            # read_bytes = b"this is test"
            # read_bytes = self.np_port_info[0]['fd'].readall()
            ready_num = self.np_port_info[0]['fd'].inWaiting()
            if ready_num == 0:
                self.timer.start(100)
                return
            if not self.fsm_dtest_running_flag:
                if ready_num < len(g_module_log_key_start):
                    print("串口数据长度不够，收到的数据长度:", ready_num)
                    self.timer.start(100)
                    return
            read_bytes = self.np_port_info[0]['fd'].read(ready_num)
            string = read_bytes.decode('utf-8')    #这里已知串口数据均为字符

            #字符串规则匹配，如需处理原始串口数据，则额外提供函数(放到规则匹配后面)
            #串口收到的字符串可能发送粘连，因此以换行符为间隔进行匹配
            list_str = string.splitlines()
            for i in range(0, len(list_str)):
                if len(list_str[i]) == 0:
                    continue
                string_temp = str(list_str[i])
                color = QColor("#000000")   #黑色
                for i in range(0, len(self.list_rule_info)):
                    if self.list_rule_info[i][g_idx_rule_eb] == "false":
                        continue
                    if string_temp.find(self.list_rule_info[i][g_idx_rule_key]) >= 0:
                        item_cnt = self.widget_rule.item(i, 1)
                        keyword_cnt = int(item_cnt.text()) + 1
                        item_cnt.setText(str(keyword_cnt))
                        color = QColor(self.list_rule_info[i][g_idx_rule_color])
                #[TODO]:颜色更改显示字符串
                self.edit_terminal.setTextColor(color)
                self.edit_terminal.append(string_temp)
                # self.edit_terminal.moveCursor(QTextCursor.End)
                # print("当前字符串颜色：%s，内容：%s" % (color.name(), string_temp))
            #发送消息到写文件的进程
            g_list_queue[1].put_nowait(string)

            #预定义的关键字处理
            if string.find(g_module_log_key_result) >= 0:
                if string.find("fail") > 0 or string.find("FAIL") > 0:
                    result = "FAILED"
                else:
                    result = "SUCCEED"
                print(name_dtest, " 执行完成，结果：", result)
                self.test_save_dtest_result(name_dtest, result)
                complete_flag = 1
            elif string.find(g_module_log_key_reboot) >= 0:
                print("dtest需要重启")
                self.fsm['reboot'] = 1
                complete_flag = 1
            elif string.find(g_module_log_key_start) >= 0 and \
                not self.fsm_dtest_running_flag:
                print("received start keyword, send dtest case group")
                self.fsm_dtest_running_flag = 1
                #发送case组合
                time.sleep(0.3)
                self.test_start_send_case_group(self.fsm['dtest'], self.np_port_info[0]['fd'])
            if complete_flag:
                self.timer.start(1000)
                self.fsm['state'] = g_fsm_free
            self.timer.start(100)

    def test_start_send_case_group(self, dtest_index, port):
        group = 0
        for i in range(1, len(self.list_dtest_info[dtest_index])):
            if self.list_dtest_info[dtest_index][i][g_idx_eb_c] == "true":
                group |= (1 << (i - 1))
        cmd = ("[CONFIG] - 0x" + str("{:08X}".format(group))).encode(encoding='utf-8')
        print("%s case组合：%d，发送到dtest的指令：%s" % \
            (self.list_dtest_info[dtest_index][0][g_idx_name], group, cmd))
        port.write(cmd)
        return 0

    def test_start_xmodem_transf_0(self, port, path_bin):
        print("开始xmodem下载固件: ", path_bin)
        x_modem = xmodem.XMODEM(xmodem_transf_0_getc,
            xmodem_transf_0_putc, mode='xmodem1k')
        time_start = datetime.datetime.now()
        try:
            fd_bin = open(path_bin, 'rb')
        except exception as e:
            msg = "文件：" + path_bin + " 打开失败"
            print(msg)
            self.msg_box_show(g_msg_warning, msg)
            return -1
        send_flag = x_modem.send(fd_bin, callback=xmodem_transf_0_callback)
        time_end = datetime.datetime.now()
        time_delta = (time_end - time_start).seconds
        print("固件(%s)发送完成，用时：%ss" % (path_bin, time_delta))
        return 0

    def test_start_xmodem_transf_1(self, port, path_bin):
        self.fsm['state'] = g_fsm_download
        print("开始xmodem下载固件: ", path_bin)
        x_modem = xmodem.XMODEM(xmodem_transf_1_getc,
            xmodem_transf_1_putc, mode='xmodem1k')
        time_start = datetime.datetime.now()
        try:
            fd_bin = open(path_bin, 'rb')
        except exception as e:
            msg = "文件：" + path_bin + " 打开失败"
            print(msg)
            self.msg_box_show(g_msg_warning, msg)
            return -1
        send_flag = x_modem.send(fd_bin, callback=xmodem_transf_1_callback)
        time_end = datetime.datetime.now()
        time_delta = (time_end - time_start).seconds
        print("固件(%s)发送完成，用时：%ss" % (path_bin, time_delta))
        return 0

    def test_start_connect_module(self, port, port_relay):
        print("尝试连接模块")
        str_recv = b''
        time_start = datetime.datetime.now()
        self.fsm['state'] = g_fsm_connect
        while 1:
            #【注意】：这里并没有判断继电器的返回值
            port_relay.write(g_module_relay_off_key)
            time.sleep(0.5)
            port_relay.write(g_module_relay_on_key)
            time.sleep(0.2)
            for i in range(0, 5):
                port.write(g_module_connect_key)
                time.sleep(0.1)
                # temp = port.readall()
                ready_num = self.np_port_info[0]['fd'].inWaiting()
                if ready_num == 0:
                    continue
                temp = self.np_port_info[0]['fd'].read(ready_num)
                if len(temp):
                    print("port rec len: %d, data:%s" % (len(temp), temp))
                str_recv += temp
                if str_recv.find(g_module_connected_key) >= 0:
                    print("模块连接成功")
                    return 0
            time_now = datetime.datetime.now()
            time_delta = (time_now - time_start).seconds
            if (time_delta > 120):
                print("模块连接超时：%s -> %s" % (time_start, time_now))
                return -1

    def test_start_port_check(self):
        list_slave = []
        for i in range(0, len(self.list_dtest_info)):
            if self.list_dtest_info[i][0][g_idx_eb] == "true":
                list_slave.append(self.list_dtest_info[i][0][g_idx_slave])
        print("从模式使能情况：%s" % list_slave)
        for i in range(0, len(self.np_port_info)):
            if (i > 1):
                if list_slave.count("true") > 0:
                    if self.np_port_info[i]['com'] == '' \
                        or self.np_port_info[i + 1]['com'] == '':
                        msg = "使能了从模式，但是未配置从模式串口"
                        print(msg)
                        self.msg_box_show(g_msg_warning, msg)
                        return -1
                else:
                    continue
            port = self.np_port_info[i]['com']
            baud = self.np_port_info[i]['baud']
            data = self.np_port_info[i]['data']
            parity = self.np_port_info[i]['parity'][0]  #取第一个字符
            stop = self.np_port_info[i]['stop']
            print("尝试打开串口，com号(%s)，波特率(%d)，数据位(%d)，校验位(%s)，"
                "停止位(%f)" % (port, baud, data, parity, stop))
            try:
                self.np_port_info[i]['fd'] = serial.Serial(port = port,
                    baudrate = baud, bytesize = data, parity = parity,
                    stopbits = stop, timeout = 0.3)
                print("%s 串口打开成功" % port)
                g_port_xmodex.append(self.np_port_info[i]['fd'])
            except Exception as e:
                msg = port + "串口打开失败，原因：" + str(e)
                print(msg)
                self.msg_box_show(g_msg_warning, msg)
                return -1
        return 0

    def test_start_file_check(self):
        #判断dtest文件是否存在，不存在则enable标签置位false，且dtest界面标红
        file_lack = []
        for i in range(0, len(self.list_dtest_info)):
            if self.list_dtest_info[i][0][g_idx_eb] == "false":
                continue
            item = self.widget_dtest.topLevelItem(i)
            name_file = self.list_dtest_info[i][0][g_idx_name]
            if name_file.rfind('.bin') < 0:
                name_file += '.bin'
            # if str_file_name.find(name_file) < 0:
            path = self.list_path[0] + '\\' + name_file
            print("当前检查的文件名为:%s， 路径为：%s" % (name_file, path))
            if not os.access(path, os.F_OK | os.R_OK):
                self.list_dtest_info[i][0][g_idx_eb] = "false"
                item.setCheckState(0, 0)
                item.setForeground(0, QtCore.Qt.red)
                item.setForeground(1, QtCore.Qt.red)
                file_lack.append(name_file)
            else:
                if self.list_dtest_info[i][0][g_idx_slave] == "true" \
                    and self.list_dtest_info[i][0][g_idx_eb] == "true":
                    if len(self.list_path[1]) == 0:
                        msg = "使能了从模式，但是未配置从固件文件夹路径"
                        print(msg)
                        self.msg_box_show(g_msg_warning, msg)
                        return -1
                    name_file_slave = name_file.replace('.', '_slave.')
                    path_slave = self.list_path[1] + '\\' + name_file_slave
                    print("slave模式使能，slave文件名:%s， 路径：%s" %
                        (name_file_slave, path_slave))
                    # if str_file_name.find(name_file_slave) < 0:
                    if not os.access(path_slave, os.F_OK | os.R_OK):
                        self.list_dtest_info[i][0][g_idx_eb] = "false"
                        item.setCheckState(0, 0)
                        item.setForeground(0, QtCore.Qt.red)
                        item.setForeground(1, QtCore.Qt.red)
                        file_lack.append(name_file_slave)
                else:
                    item.setForeground(0, QtCore.Qt.black)
                    item.setForeground(1, QtCore.Qt.black)
        if len(file_lack) > 0:
            msg = "缺少以下固件：" + str(file_lack)
            print(msg)
            self.msg_box_show(g_msg_warning, msg)
            return -1
        return 0

    def test_stop_handle(self):
        print("停止测试，关闭串口和文件，释放变量")
        self.timer.stop()
        self.pbt_cfg.setEnabled(True)
        self.edit_cycle_index.setReadOnly(False)
        g_port_xmodex.clear()
        self.fsm['state'] = g_fsm_free
        self.fsm['dtest'] = -1
        self.fsm['cycle'] = 0
        self.fsm['reboot'] = 0
        for i in range(0, len(self.np_port_info)):
            if self.np_port_info[i]['fd']:
                self.np_port_info[i]['fd'].close()
        self.pbt_start_test.setText("开始测试")
        return

    def test_save_dtest_result(self, dtest, result):
        path_result_file = self.list_path[0] + "\\" + "result.log"
        try:
            fd_result = open(path_result_file, "a")
        except exception as e:
            print(path_result_file, "文件打开失败, 原因：", e)
        fd_result.write(dtest + " --> " + result + "\n")
        fd_result.close()

    def mouse_handle_widget_right_clicked(self, pos, src):
        print("%s右键单击被触发, 显示右键菜单" % ("dtest" if src == 0 else "case"))
        menu = QMenu(self.widget_dtest)
        menu.addAction(self.act_sel_all)
        menu.addAction(self.act_sel_none)
        menu.exec(pos)

    def tree_widget_item_changed_handle(self, item, column):
        check_state = 'true' if item.checkState(0) else 'false'
        print("复选框状态:%s" % check_state)
        #更新dtest_info列表enable选项
        if item.treeWidget() is self.widget_dtest:
            index = int(item.text(0))
            self.list_dtest_info[index][0][g_idx_eb] = check_state
        else:
            if str(item.parent()) != 'None':
                index = int(item.parent().text(0))
                index_case = int(item.text(0))
                self.list_dtest_info[index][index_case + 1][g_idx_eb_c] = check_state
            else:
                index = int(item.text(0))
                for i in range(1, len(self.list_dtest_info[index])):
                    self.list_dtest_info[index][i][g_idx_eb_c] = check_state
        #更新界面
        for i in range(0, item.childCount()):
            item_child = item.child(i)
            item_child.setCheckState(0, item.checkState(0))
        print("修改后的dtest list", self.list_dtest_info)

    def table_widget_cell_changed(self, row, column):
        item = self.widget_rule.item(row, column)
        if column == 1: #计数列的更改不处理
            return
        print("表格数据变化，坐标(%d, %d)" % (row, column))
        if column == 0:   #复选框
            check_state = 'true' if item.checkState() else 'false'
            print("复选框状态：", check_state)
            self.list_rule_info[row][g_idx_rule_eb] = check_state
        elif column == 2:   #颜色更改
            pass
        elif column == 3:   #关键字更改
            keyword = item.text()
            print("关键字更改为：", keyword)
            self.list_rule_info[row][g_idx_rule_key] = keyword
        print("修改之后的rule info:", self.list_rule_info)

    def table_widget_cell_clicked(self, row, column):
        if column != 2: #只响应颜色按钮
            return
        print("表格颜色列表被单击，坐标(%d, %d)" % (row, column))
        color = QColorDialog.getColor()
        if not color.isValid():
            return
        color_str = str(color.name())
        print("选中的颜色:%s" % color_str)
        self.list_rule_info[row][g_idx_rule_color] = color_str
        item = self.widget_rule.item(row, column)
        item.setBackground(color)

    def act_handle_debug_interface_config(self, act):
        print("显示0/关闭1调试窗口 动作(%d)被按下" % act)
        if act == 0:
            self.widget_debug.setVisible(False)
        else:
            self.widget_debug.setVisible(True)

    def act_handle_option_select(self, src, act):
        print("%s 右键菜单 %s 动作被触发" %
            ("dtest" if src is self.widget_dtest else "case",
            "全选" if act == 2 else "全取消"))
        #更新dtest_info列表enable选项
        str_eb = "true" if act == 2 else "false"
        if src is self.widget_dtest:
            widget_temp = self.widget_dtest
            for i in range(0, len(self.list_dtest_info)):
                self.list_dtest_info[i][0][g_idx_eb] = str_eb
        else:
            widget_temp = self.widget_case
            for i in range(0, len(self.list_dtest_info)):
                for j in range(1, len(self.list_dtest_info[i])):
                    self.list_dtest_info[i][j][g_idx_eb_c] = str_eb
        #更新界面
        for i in range(0, widget_temp.topLevelItemCount()):
            item = widget_temp.topLevelItem(i)
            item.setCheckState(0, act)
            for i in range(0, item.childCount()):
                item_child = item.child(i)
                item_child.setCheckState(0, item.checkState(0))
        print("修改后的dtest list", self.list_dtest_info)

    def act_handle_xml_file_open_save(self, act):
        print("%s 动作被触发" %
            ("导入" if act == 0 else ("保存" if act == 1 else "另存")))
        if act == 0:    #导入文件
            path_file, _ = QFileDialog.getOpenFileName(self,
                "选择要导入的xml文件", "./", 'xml文件 (*.xml)') #返回一个元组
            if len(path_file) == 0:
                print("选中的文件路径无效: ", path_file)
                return
            print("选中的文件： ", path_file)
            self.xml_file_load(path_file)
        elif act == 2:  #另存文件
            path_file, _ = QFileDialog.getSaveFileName(self,
                "另存为", "./", "xml文件 (*.xml)")
            if len(path_file) == 0:
                print("选中的文件路径无效: ", path_file)
                return
            self.xml_file_save(path_file)
        else:   #保存文件
            self.xml_file_save(self.path_xml_file)

    def write(self, str):
        if str == ' ' or str == '\n':
            return
        self.edit_debug.append(str)
        g_list_queue[0].put_nowait(str)

    def msg_box_show(self, type, msg):
        # 自动化测试时不弹窗
        if self.auto_test_mode:
            return
        if type == g_msg_warning:
            QMessageBox.warning(self, '警告', msg, QMessageBox.Yes)
        else:
            return

def main():
    app = QtWidgets.QApplication(sys.argv)
    my_app = kl3_test_app(argv=sys.argv)
    my_app.show()
    exit_flag = app.exec_()
    print(sys.argv[0], "exit flag: ", exit_flag)
    sys.exit(exit_flag)

if __name__ == '__main__':
    freeze_support()    #解决打包exe后出现的循环启动
    main()