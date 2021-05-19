# kl3-autotest-tool  
## 概述
kl3dtest自动化测试工具（以下简称“软件”）的前身是为了测试kl3计量功能而设计的一个python脚本，后来为了方便对kl3的各个功能进行自动化测试，将该脚本拓展为python+qt的一个软件。  
该软件主要包含如下亮点：  
* xml文件的读取、解析、保存  
* 界面可勾选dtest和dtest对应的case  
* xmodem下载固件
* 串口数据显示，可对关键字进行统计和设置颜色
* 可拓展串口数据处理模块
* 调试日志、串口日志文件记录  

程序启动后的界面如下图所示  
![image](https://user-images.githubusercontent.com/36351182/118810121-1638be00-b8de-11eb-86c0-33db8a67a4a2.png)
## 程序逻辑
程序为交互式执行，因此当程序在初始化完成后，会一直等到交互动作产生特定信号，来触发指定的流程。其大体的程序框架如下图所示：  
![image](https://user-images.githubusercontent.com/36351182/118810661-b68ee280-b8de-11eb-9bea-ae309a148120.png)
### xml加载
存在一个默认的xml文件，其路径在与软件（或python脚本）同级目录下，名称固定为”dtest.xml”，件在启动后会尝试读取默认的xml文件，并将xml的内容显示到界面。xml内容和界面的对应关系如下：
#### 调试界面使能
在xml中对应<debug_interface>节点，包含“true”或者“false”文本节点，如下图所示：  
 ![image](https://user-images.githubusercontent.com/36351182/118810871-f1911600-b8de-11eb-86f9-600e01175d2e.png)  
在界面中对应调试日志区域，当文本节点为“false”时，隐藏调试日志区域，当文本节点为“true”时，显示调试区域。
当隐藏调试区域时，调试区域上方的界面自动填充，如下图所示：  
![image](https://user-images.githubusercontent.com/36351182/118810900-f81f8d80-b8de-11eb-88c0-1a0fba181961.png)  
__【注】：隐藏界面时，调试日志仍然记录在界面中。__
#### 串口配置
在xml中对应\<port id="x">节点，该节点包含id属性，用于标识是第几个串口（从0开始计数，最多定义4个串口）；该节点包含5个子节点，其解释如下：  
* \<com>子节点，用于标识PC上的串口对应的com号，使用一个文本子节点记录；  
* \<buad>子节点，用于标识串口对应的波特率，使用一个文本子节点记录；  
* \<data>子节点，用于标识串口对应的数据位，使用一个文本子节点记录；  
* \<parity>子节点，用于标识串口对应的校验位，使用一个文本子节点记录；  
* \<stop>子节点，用于标识串口对应的停止位，使用一个文本子节点记录；  

完整的节点定义如下图所示：  
![image](https://user-images.githubusercontent.com/36351182/118811055-2309e180-b8df-11eb-9ba9-d6594eaceba9.png)  
在界面中对应配置界面COM口区域，配置界面需要在主界面点击“配置”按钮打开，配置界面如下如所示：  
  ![image](https://user-images.githubusercontent.com/36351182/118811092-2d2be000-b8df-11eb-8b6c-7beb1ccf0597.png)
从上到下，com口编号为0~3，对应xml文件中的id0~id3，界面中的波特率等参数均来自xml文件中定义的参数值。  
#### 固件路径
在xml文件中对应\<dir>节点，该节点包含id属性，当id为0时表示是主模式固件路径，id为1时表示是从模式固件路径。固件路径的文本储存在该节点下的文本子节点中。  
  ![image](https://user-images.githubusercontent.com/36351182/118811533-b3e0bd00-b8df-11eb-8581-d7891a4af5d1.png)  
在界面中对应配置界面固件路径区域，“主固件路径1”对应id为0的文本节点，“从固件路径2”对应id为1的文本节点。如下图所示：  
![image](https://user-images.githubusercontent.com/36351182/118811573-bc38f800-b8df-11eb-8a7c-8ad92d56d7b9.png)  
#### dtest信息
在xml中表现为\<dtest>节点，该节点包含id属性，用于标识是第几个dtest。\<dtest>节点包含5个子节点，其解释如下：  
* \<name>子节点，用于标识dtest名称，使用文本子节点记录内容；  
* \<note>子节点，用于标识dtest说明信息，使用文本子节点记录内容；  
* \<enable>子节点，用于标识dtest是否使能，使用文本子节点记录内容（true或者false）；  
* \<slave_mode>子节点，用于标识dtest是否支持从模式，使用文本子节点记录内容；  
* \<case>子节点，用于标识dtest具有的case信息，包含id属性，用于标识当前case编号。\<case>子节点下存在3个子节点。  
  * \<name>子节点，用于标识case名称，使用文本子节点记录内容；  
  * \<note>子节点，用于标识case说明信息，使用文本子节点记录内容；  
  * \<enable>子节点，用于标识case是否使能，使用文本子节点记录内容；  

![image](https://user-images.githubusercontent.com/36351182/118812172-6ca6fc00-b8e0-11eb-86cd-078150ca3735.png)  
在界面中对应测试用例配置区域，该区域分为两部分，分别为dtest列表和case列表，以dtest id+dtest名称形成一行，分别加入2个列表中（但是选择动作不同步），case id+case名称形成一行，加入到case列表中当前case所属dtest下。如下图所示：  
![image](https://user-images.githubusercontent.com/36351182/118812233-7af51800-b8e0-11eb-8470-cf8327610fe4.png)  
#### 关键字规则
在xml中对应\<rule>节点，该节点包含id属性，用于标识当前规则的编号，\<rule>节点包含3个子节点，其解释如下：  
* \<keyword>子节点，用于标识关键字信息，使用文本子节点记录内容；
* \<color>子节点，用于标识关键字颜色，使用文本子节点记录内容，其格式为#RRGGBB
* \<enable>子节点，用于标识关键字是否使能，使用文本子节点记录内容  
![image](https://user-images.githubusercontent.com/36351182/118812411-a972f300-b8e0-11eb-9f56-98e66f72bf6c.png)  
在界面中对应关键字规则区域，\<enable>节点转换为复选框，节点内容为“true”时选中，为“false”时取消选中，\<color>节点转换为颜色框，\<keyword>节点内容显示到关键字列，从上到下，每一行分别对应\<rule>节点id0~idx（目前限定x最大为20）  
![image](https://user-images.githubusercontent.com/36351182/118812469-babbff80-b8e0-11eb-8ce8-dbfece92e329.png)  
## 状态机
在最初的设计中，dtest测试流程、串口数据的接收由子线程完成，并且在子线程中处理关键字以及将数据更新到界面，主线程负责界面的交互。然而在调试过程中发现以下几个问题：    
*	由于python的GIL限制，多线程无法做到真正的并行。  
*	负责更新界面的进程不能被阻塞，也不能休眠，否则会导致界面出现卡死的现象。  
*	pyqt使用的时候如果非界面线程直接访问控件元素会有问题  
因此，设计方案改为仅采用一个线程，配合定时器+状态机完成界面更新和dtest测试。  
dtest的测试可以简化为以下4个步骤：   
*	连接模块  
*	xmodem方式下载固件  
*	发送case组合  
*	接收串口数据，并等待dtest测试完毕（收到RESULT关键字）  
步骤相对简单，且几乎没有额外的分支，因此状态机的设计也相对简单，如下图所示  
![image](https://user-images.githubusercontent.com/36351182/118812732-fce54100-b8e0-11eb-9caa-d550f289aa77.png)  
## 交互动作
### xml导入、保存、另存  
xml文件的导入，保存和另存动作，触发方式为选中菜单栏中“文件”菜单下对应的动作选项，如下图所示：  
![image](https://user-images.githubusercontent.com/36351182/118812774-0cfd2080-b8e1-11eb-8e96-4d00cccb473d.png)  
导入和另存动作均会触发文件选择对话框，在弹出的选择框中，默认为当前软件（或python脚本）所在目录。  
![image](https://user-images.githubusercontent.com/36351182/118812795-16868880-b8e1-11eb-9b62-da4e23b34b9c.png)  
导入动作限定选择类型为xml文件，选中文件后会触发xml解析逻辑，更新界面。  
保存动作则将当前界面的配置按照xml规定的格式保存到当前打开的xml文件中。  
另存动作与保存类似，不过需要指定另存的文件名（或选择已存在的xml文件）。  
### 隐藏\显示调试界面
隐藏\显示调试界面动作有菜单栏中“界面”菜单中对应的动作选项触发，如下图所示：  
![image](https://user-images.githubusercontent.com/36351182/118812890-2ef6a300-b8e1-11eb-8329-f15832ab74d7.png)  
如字面意思所述，这两个动作表示隐藏或者显示软件调试日志显示区域。  
### 配置
配置动作由界面左上角的“配置”按钮触发，其功能为弹出配置界面。如下图所示：  
![image](https://user-images.githubusercontent.com/36351182/118812947-3f0e8280-b8e1-11eb-9335-39cdef373e96.png)  
在配置界面中，有多个下拉输入框，可配置串口的相关属性；2个文本输入框可配置主从固件所在路径。  
当点击“OK”按钮时，会判断用户配置是否有效，无效则弹出提示框，并将配置界面置于主界面上层，如果配置有效，或者点击“cancel”按钮和“x”退出按钮时，配置界面才能关闭。  
__【注】：配置有效是指未配置从模式时主模式2个串口均配置、COM号不冲突、路径有效。配置从模式时4个串口均配置、COM口不冲突，且2个路径均有效。*__ 
### dtest、case选择
dtest和case配置界面均存在复选框。当dtest界面中的复选框选中时，表示复选框对应的dtest需要参与测试。如果dtest对应的bin文件不存在，则在开始测试后会自动取消并标记为红色，并弹出警告框。  
![image](https://user-images.githubusercontent.com/36351182/118813051-564d7000-b8e1-11eb-8c1f-2383a5b05879.png)  
当case界面dtest名称（即一级目录）被选中时，则认为是改dtest所有case均需要测试，界面会自动勾选下属的所有case。当case名称（即二级目录）被选中时，表示当前case需要测试，在状态机执行到对应位置时，会将所有选中的case转换为%08X格式的数据发送到当前dtest中。  
如选中的case为case0和case1时发送的数据格式如下：  
**[CONFIG] - metering_test : 00000003'**
### 开始测试
如字面意思所述，单击“开始测试”按钮时，会初始化状态机，启动测试流程。  
### 循环次数
如字面意思所述，表示测试循环次数，默认为1，当该值设置为0或者负数时，表示无限循环。  
如当值设置为2是，表示将当前勾选且有效的所有dtest测试2次（reboot字段导致的dtest重启不计算在内）。  
### 关键字规则设置
关键字规则界面如下：  
![image](https://user-images.githubusercontent.com/36351182/118813182-78df8900-b8e1-11eb-9df3-d82598a9396c.png)  
使能列对应的复选框表示本行的关键字是否生效，如果生效，则当串口接收到包含关键字的数据时，将累计一次次数，并使用当前行设置的颜色标记显示在终端界面的本次数据。  
颜色列对应的颜色框可以单击，启动颜色选择框，选择自定义的颜色。  
关键字列对应的关键字可以随意更改。  












