# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_config(object):
    def setupUi(self, config):
        config.setObjectName("config")
        config.resize(553, 260)
        self.gridLayout = QtWidgets.QGridLayout(config)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_com_0 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_com_0.sizePolicy().hasHeightForWidth())
        self.label_com_0.setSizePolicy(sizePolicy)
        self.label_com_0.setObjectName("label_com_0")
        self.horizontalLayout.addWidget(self.label_com_0)
        self.combo_com_0 = QtWidgets.QComboBox(config)
        self.combo_com_0.setObjectName("combo_com_0")
        self.horizontalLayout.addWidget(self.combo_com_0)
        self.label_baud_0 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_baud_0.sizePolicy().hasHeightForWidth())
        self.label_baud_0.setSizePolicy(sizePolicy)
        self.label_baud_0.setObjectName("label_baud_0")
        self.horizontalLayout.addWidget(self.label_baud_0)
        self.combo_baud_0 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_baud_0.sizePolicy().hasHeightForWidth())
        self.combo_baud_0.setSizePolicy(sizePolicy)
        self.combo_baud_0.setObjectName("combo_baud_0")
        self.combo_baud_0.addItem("")
        self.combo_baud_0.addItem("")
        self.combo_baud_0.addItem("")
        self.combo_baud_0.addItem("")
        self.combo_baud_0.addItem("")
        self.combo_baud_0.addItem("")
        self.combo_baud_0.addItem("")
        self.combo_baud_0.addItem("")
        self.combo_baud_0.addItem("")
        self.combo_baud_0.addItem("")
        self.combo_baud_0.addItem("")
        self.combo_baud_0.addItem("")
        self.combo_baud_0.addItem("")
        self.horizontalLayout.addWidget(self.combo_baud_0)
        self.label_data_0 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_data_0.sizePolicy().hasHeightForWidth())
        self.label_data_0.setSizePolicy(sizePolicy)
        self.label_data_0.setObjectName("label_data_0")
        self.horizontalLayout.addWidget(self.label_data_0)
        self.combo_data_0 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_data_0.sizePolicy().hasHeightForWidth())
        self.combo_data_0.setSizePolicy(sizePolicy)
        self.combo_data_0.setObjectName("combo_data_0")
        self.combo_data_0.addItem("")
        self.combo_data_0.addItem("")
        self.combo_data_0.addItem("")
        self.combo_data_0.addItem("")
        self.horizontalLayout.addWidget(self.combo_data_0)
        self.label_parity_0 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_parity_0.sizePolicy().hasHeightForWidth())
        self.label_parity_0.setSizePolicy(sizePolicy)
        self.label_parity_0.setObjectName("label_parity_0")
        self.horizontalLayout.addWidget(self.label_parity_0)
        self.combo_parity_0 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_parity_0.sizePolicy().hasHeightForWidth())
        self.combo_parity_0.setSizePolicy(sizePolicy)
        self.combo_parity_0.setObjectName("combo_parity_0")
        self.combo_parity_0.addItem("")
        self.combo_parity_0.addItem("")
        self.combo_parity_0.addItem("")
        self.combo_parity_0.addItem("")
        self.combo_parity_0.addItem("")
        self.horizontalLayout.addWidget(self.combo_parity_0)
        self.label_stop_0 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_stop_0.sizePolicy().hasHeightForWidth())
        self.label_stop_0.setSizePolicy(sizePolicy)
        self.label_stop_0.setObjectName("label_stop_0")
        self.horizontalLayout.addWidget(self.label_stop_0)
        self.combo_stop_0 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_stop_0.sizePolicy().hasHeightForWidth())
        self.combo_stop_0.setSizePolicy(sizePolicy)
        self.combo_stop_0.setObjectName("combo_stop_0")
        self.combo_stop_0.addItem("")
        self.combo_stop_0.addItem("")
        self.combo_stop_0.addItem("")
        self.horizontalLayout.addWidget(self.combo_stop_0)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_com_1 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_com_1.sizePolicy().hasHeightForWidth())
        self.label_com_1.setSizePolicy(sizePolicy)
        self.label_com_1.setObjectName("label_com_1")
        self.horizontalLayout_2.addWidget(self.label_com_1)
        self.combo_com_1 = QtWidgets.QComboBox(config)
        self.combo_com_1.setObjectName("combo_com_1")
        self.horizontalLayout_2.addWidget(self.combo_com_1)
        self.label_baud_1 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_baud_1.sizePolicy().hasHeightForWidth())
        self.label_baud_1.setSizePolicy(sizePolicy)
        self.label_baud_1.setObjectName("label_baud_1")
        self.horizontalLayout_2.addWidget(self.label_baud_1)
        self.combo_baud_1 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_baud_1.sizePolicy().hasHeightForWidth())
        self.combo_baud_1.setSizePolicy(sizePolicy)
        self.combo_baud_1.setObjectName("combo_baud_1")
        self.combo_baud_1.addItem("")
        self.combo_baud_1.addItem("")
        self.combo_baud_1.addItem("")
        self.combo_baud_1.addItem("")
        self.combo_baud_1.addItem("")
        self.combo_baud_1.addItem("")
        self.combo_baud_1.addItem("")
        self.combo_baud_1.addItem("")
        self.combo_baud_1.addItem("")
        self.combo_baud_1.addItem("")
        self.combo_baud_1.addItem("")
        self.combo_baud_1.addItem("")
        self.combo_baud_1.addItem("")
        self.horizontalLayout_2.addWidget(self.combo_baud_1)
        self.label_data_1 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_data_1.sizePolicy().hasHeightForWidth())
        self.label_data_1.setSizePolicy(sizePolicy)
        self.label_data_1.setObjectName("label_data_1")
        self.horizontalLayout_2.addWidget(self.label_data_1)
        self.combo_data_1 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_data_1.sizePolicy().hasHeightForWidth())
        self.combo_data_1.setSizePolicy(sizePolicy)
        self.combo_data_1.setObjectName("combo_data_1")
        self.combo_data_1.addItem("")
        self.combo_data_1.addItem("")
        self.combo_data_1.addItem("")
        self.combo_data_1.addItem("")
        self.horizontalLayout_2.addWidget(self.combo_data_1)
        self.label_parity_1 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_parity_1.sizePolicy().hasHeightForWidth())
        self.label_parity_1.setSizePolicy(sizePolicy)
        self.label_parity_1.setObjectName("label_parity_1")
        self.horizontalLayout_2.addWidget(self.label_parity_1)
        self.combo_parity_1 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_parity_1.sizePolicy().hasHeightForWidth())
        self.combo_parity_1.setSizePolicy(sizePolicy)
        self.combo_parity_1.setObjectName("combo_parity_1")
        self.combo_parity_1.addItem("")
        self.combo_parity_1.addItem("")
        self.combo_parity_1.addItem("")
        self.combo_parity_1.addItem("")
        self.combo_parity_1.addItem("")
        self.horizontalLayout_2.addWidget(self.combo_parity_1)
        self.label_stop_1 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_stop_1.sizePolicy().hasHeightForWidth())
        self.label_stop_1.setSizePolicy(sizePolicy)
        self.label_stop_1.setObjectName("label_stop_1")
        self.horizontalLayout_2.addWidget(self.label_stop_1)
        self.combo_stop_1 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_stop_1.sizePolicy().hasHeightForWidth())
        self.combo_stop_1.setSizePolicy(sizePolicy)
        self.combo_stop_1.setObjectName("combo_stop_1")
        self.combo_stop_1.addItem("")
        self.combo_stop_1.addItem("")
        self.combo_stop_1.addItem("")
        self.horizontalLayout_2.addWidget(self.combo_stop_1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_fw_path_0 = QtWidgets.QLabel(config)
        self.label_fw_path_0.setObjectName("label_fw_path_0")
        self.horizontalLayout_4.addWidget(self.label_fw_path_0)
        self.edit_fw_path_0 = QtWidgets.QLineEdit(config)
        self.edit_fw_path_0.setObjectName("edit_fw_path_0")
        self.horizontalLayout_4.addWidget(self.edit_fw_path_0)
        self.pbt_sel_file_0 = QtWidgets.QPushButton(config)
        self.pbt_sel_file_0.setObjectName("pbt_sel_file_0")
        self.horizontalLayout_4.addWidget(self.pbt_sel_file_0)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_com_2 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_com_2.sizePolicy().hasHeightForWidth())
        self.label_com_2.setSizePolicy(sizePolicy)
        self.label_com_2.setObjectName("label_com_2")
        self.horizontalLayout_3.addWidget(self.label_com_2)
        self.combo_com_2 = QtWidgets.QComboBox(config)
        self.combo_com_2.setObjectName("combo_com_2")
        self.horizontalLayout_3.addWidget(self.combo_com_2)
        self.label_baud_2 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_baud_2.sizePolicy().hasHeightForWidth())
        self.label_baud_2.setSizePolicy(sizePolicy)
        self.label_baud_2.setObjectName("label_baud_2")
        self.horizontalLayout_3.addWidget(self.label_baud_2)
        self.combo_baud_2 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_baud_2.sizePolicy().hasHeightForWidth())
        self.combo_baud_2.setSizePolicy(sizePolicy)
        self.combo_baud_2.setObjectName("combo_baud_2")
        self.combo_baud_2.addItem("")
        self.combo_baud_2.addItem("")
        self.combo_baud_2.addItem("")
        self.combo_baud_2.addItem("")
        self.combo_baud_2.addItem("")
        self.combo_baud_2.addItem("")
        self.combo_baud_2.addItem("")
        self.combo_baud_2.addItem("")
        self.combo_baud_2.addItem("")
        self.combo_baud_2.addItem("")
        self.combo_baud_2.addItem("")
        self.combo_baud_2.addItem("")
        self.combo_baud_2.addItem("")
        self.horizontalLayout_3.addWidget(self.combo_baud_2)
        self.label_data_2 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_data_2.sizePolicy().hasHeightForWidth())
        self.label_data_2.setSizePolicy(sizePolicy)
        self.label_data_2.setObjectName("label_data_2")
        self.horizontalLayout_3.addWidget(self.label_data_2)
        self.combo_data_2 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_data_2.sizePolicy().hasHeightForWidth())
        self.combo_data_2.setSizePolicy(sizePolicy)
        self.combo_data_2.setObjectName("combo_data_2")
        self.combo_data_2.addItem("")
        self.combo_data_2.addItem("")
        self.combo_data_2.addItem("")
        self.combo_data_2.addItem("")
        self.horizontalLayout_3.addWidget(self.combo_data_2)
        self.label_parity_2 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_parity_2.sizePolicy().hasHeightForWidth())
        self.label_parity_2.setSizePolicy(sizePolicy)
        self.label_parity_2.setObjectName("label_parity_2")
        self.horizontalLayout_3.addWidget(self.label_parity_2)
        self.combo_parity_2 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_parity_2.sizePolicy().hasHeightForWidth())
        self.combo_parity_2.setSizePolicy(sizePolicy)
        self.combo_parity_2.setObjectName("combo_parity_2")
        self.combo_parity_2.addItem("")
        self.combo_parity_2.addItem("")
        self.combo_parity_2.addItem("")
        self.combo_parity_2.addItem("")
        self.combo_parity_2.addItem("")
        self.horizontalLayout_3.addWidget(self.combo_parity_2)
        self.label_stop_2 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_stop_2.sizePolicy().hasHeightForWidth())
        self.label_stop_2.setSizePolicy(sizePolicy)
        self.label_stop_2.setObjectName("label_stop_2")
        self.horizontalLayout_3.addWidget(self.label_stop_2)
        self.combo_stop_2 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_stop_2.sizePolicy().hasHeightForWidth())
        self.combo_stop_2.setSizePolicy(sizePolicy)
        self.combo_stop_2.setObjectName("combo_stop_2")
        self.combo_stop_2.addItem("")
        self.combo_stop_2.addItem("")
        self.combo_stop_2.addItem("")
        self.horizontalLayout_3.addWidget(self.combo_stop_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_com_3 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_com_3.sizePolicy().hasHeightForWidth())
        self.label_com_3.setSizePolicy(sizePolicy)
        self.label_com_3.setObjectName("label_com_3")
        self.horizontalLayout_5.addWidget(self.label_com_3)
        self.combo_com_3 = QtWidgets.QComboBox(config)
        self.combo_com_3.setObjectName("combo_com_3")
        self.horizontalLayout_5.addWidget(self.combo_com_3)
        self.label_baud_3 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_baud_3.sizePolicy().hasHeightForWidth())
        self.label_baud_3.setSizePolicy(sizePolicy)
        self.label_baud_3.setObjectName("label_baud_3")
        self.horizontalLayout_5.addWidget(self.label_baud_3)
        self.combo_baud_3 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_baud_3.sizePolicy().hasHeightForWidth())
        self.combo_baud_3.setSizePolicy(sizePolicy)
        self.combo_baud_3.setObjectName("combo_baud_3")
        self.combo_baud_3.addItem("")
        self.combo_baud_3.addItem("")
        self.combo_baud_3.addItem("")
        self.combo_baud_3.addItem("")
        self.combo_baud_3.addItem("")
        self.combo_baud_3.addItem("")
        self.combo_baud_3.addItem("")
        self.combo_baud_3.addItem("")
        self.combo_baud_3.addItem("")
        self.combo_baud_3.addItem("")
        self.combo_baud_3.addItem("")
        self.combo_baud_3.addItem("")
        self.combo_baud_3.addItem("")
        self.horizontalLayout_5.addWidget(self.combo_baud_3)
        self.label_data_3 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_data_3.sizePolicy().hasHeightForWidth())
        self.label_data_3.setSizePolicy(sizePolicy)
        self.label_data_3.setObjectName("label_data_3")
        self.horizontalLayout_5.addWidget(self.label_data_3)
        self.combo_data_3 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_data_3.sizePolicy().hasHeightForWidth())
        self.combo_data_3.setSizePolicy(sizePolicy)
        self.combo_data_3.setObjectName("combo_data_3")
        self.combo_data_3.addItem("")
        self.combo_data_3.addItem("")
        self.combo_data_3.addItem("")
        self.combo_data_3.addItem("")
        self.horizontalLayout_5.addWidget(self.combo_data_3)
        self.label_parity_3 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_parity_3.sizePolicy().hasHeightForWidth())
        self.label_parity_3.setSizePolicy(sizePolicy)
        self.label_parity_3.setObjectName("label_parity_3")
        self.horizontalLayout_5.addWidget(self.label_parity_3)
        self.combo_parity_3 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_parity_3.sizePolicy().hasHeightForWidth())
        self.combo_parity_3.setSizePolicy(sizePolicy)
        self.combo_parity_3.setObjectName("combo_parity_3")
        self.combo_parity_3.addItem("")
        self.combo_parity_3.addItem("")
        self.combo_parity_3.addItem("")
        self.combo_parity_3.addItem("")
        self.combo_parity_3.addItem("")
        self.horizontalLayout_5.addWidget(self.combo_parity_3)
        self.label_stop_3 = QtWidgets.QLabel(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_stop_3.sizePolicy().hasHeightForWidth())
        self.label_stop_3.setSizePolicy(sizePolicy)
        self.label_stop_3.setObjectName("label_stop_3")
        self.horizontalLayout_5.addWidget(self.label_stop_3)
        self.combo_stop_3 = QtWidgets.QComboBox(config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_stop_3.sizePolicy().hasHeightForWidth())
        self.combo_stop_3.setSizePolicy(sizePolicy)
        self.combo_stop_3.setObjectName("combo_stop_3")
        self.combo_stop_3.addItem("")
        self.combo_stop_3.addItem("")
        self.combo_stop_3.addItem("")
        self.horizontalLayout_5.addWidget(self.combo_stop_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_fw_path_1 = QtWidgets.QLabel(config)
        self.label_fw_path_1.setObjectName("label_fw_path_1")
        self.horizontalLayout_6.addWidget(self.label_fw_path_1)
        self.edit_fw_path_1 = QtWidgets.QLineEdit(config)
        self.edit_fw_path_1.setObjectName("edit_fw_path_1")
        self.horizontalLayout_6.addWidget(self.edit_fw_path_1)
        self.pbt_sel_file_1 = QtWidgets.QPushButton(config)
        self.pbt_sel_file_1.setObjectName("pbt_sel_file_1")
        self.horizontalLayout_6.addWidget(self.pbt_sel_file_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.pbt_box_cfg = QtWidgets.QDialogButtonBox(config)
        self.pbt_box_cfg.setOrientation(QtCore.Qt.Horizontal)
        self.pbt_box_cfg.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.pbt_box_cfg.setObjectName("pbt_box_cfg")
        self.gridLayout.addWidget(self.pbt_box_cfg, 3, 0, 1, 1)

        self.retranslateUi(config)
        QtCore.QMetaObject.connectSlotsByName(config)

    def retranslateUi(self, config):
        _translate = QtCore.QCoreApplication.translate
        config.setWindowTitle(_translate("config", "Dialog"))
        self.label.setText(_translate("config", "?????????????????????????????????dtest????????????????????????2???????????????????????????"))
        self.label_com_0.setText(_translate("config", "?????????COM???"))
        self.label_baud_0.setText(_translate("config", "?????????"))
        self.combo_baud_0.setItemText(0, _translate("config", "1200"))
        self.combo_baud_0.setItemText(1, _translate("config", "2400"))
        self.combo_baud_0.setItemText(2, _translate("config", "4800"))
        self.combo_baud_0.setItemText(3, _translate("config", "9600"))
        self.combo_baud_0.setItemText(4, _translate("config", "14400"))
        self.combo_baud_0.setItemText(5, _translate("config", "19200"))
        self.combo_baud_0.setItemText(6, _translate("config", "38400"))
        self.combo_baud_0.setItemText(7, _translate("config", "57600"))
        self.combo_baud_0.setItemText(8, _translate("config", "115200"))
        self.combo_baud_0.setItemText(9, _translate("config", "230400"))
        self.combo_baud_0.setItemText(10, _translate("config", "460800"))
        self.combo_baud_0.setItemText(11, _translate("config", "921600"))
        self.combo_baud_0.setItemText(12, _translate("config", "3000000"))
        self.label_data_0.setText(_translate("config", "?????????"))
        self.combo_data_0.setItemText(0, _translate("config", "5"))
        self.combo_data_0.setItemText(1, _translate("config", "6"))
        self.combo_data_0.setItemText(2, _translate("config", "7"))
        self.combo_data_0.setItemText(3, _translate("config", "8"))
        self.label_parity_0.setText(_translate("config", "?????????"))
        self.combo_parity_0.setItemText(0, _translate("config", "NONE"))
        self.combo_parity_0.setItemText(1, _translate("config", "ODD"))
        self.combo_parity_0.setItemText(2, _translate("config", "EVEN"))
        self.combo_parity_0.setItemText(3, _translate("config", "MARK"))
        self.combo_parity_0.setItemText(4, _translate("config", "SPACE"))
        self.label_stop_0.setText(_translate("config", "?????????"))
        self.combo_stop_0.setItemText(0, _translate("config", "1"))
        self.combo_stop_0.setItemText(1, _translate("config", "1.5"))
        self.combo_stop_0.setItemText(2, _translate("config", "2"))
        self.label_com_1.setText(_translate("config", "?????????COM???"))
        self.label_baud_1.setText(_translate("config", "?????????"))
        self.combo_baud_1.setItemText(0, _translate("config", "1200"))
        self.combo_baud_1.setItemText(1, _translate("config", "2400"))
        self.combo_baud_1.setItemText(2, _translate("config", "4800"))
        self.combo_baud_1.setItemText(3, _translate("config", "9600"))
        self.combo_baud_1.setItemText(4, _translate("config", "14400"))
        self.combo_baud_1.setItemText(5, _translate("config", "19200"))
        self.combo_baud_1.setItemText(6, _translate("config", "38400"))
        self.combo_baud_1.setItemText(7, _translate("config", "57600"))
        self.combo_baud_1.setItemText(8, _translate("config", "115200"))
        self.combo_baud_1.setItemText(9, _translate("config", "230400"))
        self.combo_baud_1.setItemText(10, _translate("config", "460800"))
        self.combo_baud_1.setItemText(11, _translate("config", "921600"))
        self.combo_baud_1.setItemText(12, _translate("config", "3000000"))
        self.label_data_1.setText(_translate("config", "?????????"))
        self.combo_data_1.setItemText(0, _translate("config", "5"))
        self.combo_data_1.setItemText(1, _translate("config", "6"))
        self.combo_data_1.setItemText(2, _translate("config", "7"))
        self.combo_data_1.setItemText(3, _translate("config", "8"))
        self.label_parity_1.setText(_translate("config", "?????????"))
        self.combo_parity_1.setItemText(0, _translate("config", "NONE"))
        self.combo_parity_1.setItemText(1, _translate("config", "ODD"))
        self.combo_parity_1.setItemText(2, _translate("config", "EVEN"))
        self.combo_parity_1.setItemText(3, _translate("config", "MARK"))
        self.combo_parity_1.setItemText(4, _translate("config", "SPACE"))
        self.label_stop_1.setText(_translate("config", "?????????"))
        self.combo_stop_1.setItemText(0, _translate("config", "1"))
        self.combo_stop_1.setItemText(1, _translate("config", "1.5"))
        self.combo_stop_1.setItemText(2, _translate("config", "2"))
        self.label_fw_path_0.setText(_translate("config", "???????????????1"))
        self.pbt_sel_file_0.setText(_translate("config", "????????????"))
        self.label_com_2.setText(_translate("config", "?????????COM???"))
        self.label_baud_2.setText(_translate("config", "?????????"))
        self.combo_baud_2.setItemText(0, _translate("config", "1200"))
        self.combo_baud_2.setItemText(1, _translate("config", "2400"))
        self.combo_baud_2.setItemText(2, _translate("config", "4800"))
        self.combo_baud_2.setItemText(3, _translate("config", "9600"))
        self.combo_baud_2.setItemText(4, _translate("config", "14400"))
        self.combo_baud_2.setItemText(5, _translate("config", "19200"))
        self.combo_baud_2.setItemText(6, _translate("config", "38400"))
        self.combo_baud_2.setItemText(7, _translate("config", "57600"))
        self.combo_baud_2.setItemText(8, _translate("config", "115200"))
        self.combo_baud_2.setItemText(9, _translate("config", "230400"))
        self.combo_baud_2.setItemText(10, _translate("config", "460800"))
        self.combo_baud_2.setItemText(11, _translate("config", "921600"))
        self.combo_baud_2.setItemText(12, _translate("config", "3000000"))
        self.label_data_2.setText(_translate("config", "?????????"))
        self.combo_data_2.setItemText(0, _translate("config", "5"))
        self.combo_data_2.setItemText(1, _translate("config", "6"))
        self.combo_data_2.setItemText(2, _translate("config", "7"))
        self.combo_data_2.setItemText(3, _translate("config", "8"))
        self.label_parity_2.setText(_translate("config", "?????????"))
        self.combo_parity_2.setItemText(0, _translate("config", "NONE"))
        self.combo_parity_2.setItemText(1, _translate("config", "ODD"))
        self.combo_parity_2.setItemText(2, _translate("config", "EVEN"))
        self.combo_parity_2.setItemText(3, _translate("config", "MARK"))
        self.combo_parity_2.setItemText(4, _translate("config", "SPACE"))
        self.label_stop_2.setText(_translate("config", "?????????"))
        self.combo_stop_2.setItemText(0, _translate("config", "1"))
        self.combo_stop_2.setItemText(1, _translate("config", "1.5"))
        self.combo_stop_2.setItemText(2, _translate("config", "2"))
        self.label_com_3.setText(_translate("config", "?????????COM???"))
        self.label_baud_3.setText(_translate("config", "?????????"))
        self.combo_baud_3.setItemText(0, _translate("config", "1200"))
        self.combo_baud_3.setItemText(1, _translate("config", "2400"))
        self.combo_baud_3.setItemText(2, _translate("config", "4800"))
        self.combo_baud_3.setItemText(3, _translate("config", "9600"))
        self.combo_baud_3.setItemText(4, _translate("config", "14400"))
        self.combo_baud_3.setItemText(5, _translate("config", "19200"))
        self.combo_baud_3.setItemText(6, _translate("config", "38400"))
        self.combo_baud_3.setItemText(7, _translate("config", "57600"))
        self.combo_baud_3.setItemText(8, _translate("config", "115200"))
        self.combo_baud_3.setItemText(9, _translate("config", "230400"))
        self.combo_baud_3.setItemText(10, _translate("config", "460800"))
        self.combo_baud_3.setItemText(11, _translate("config", "921600"))
        self.combo_baud_3.setItemText(12, _translate("config", "3000000"))
        self.label_data_3.setText(_translate("config", "?????????"))
        self.combo_data_3.setItemText(0, _translate("config", "5"))
        self.combo_data_3.setItemText(1, _translate("config", "6"))
        self.combo_data_3.setItemText(2, _translate("config", "7"))
        self.combo_data_3.setItemText(3, _translate("config", "8"))
        self.label_parity_3.setText(_translate("config", "?????????"))
        self.combo_parity_3.setItemText(0, _translate("config", "NONE"))
        self.combo_parity_3.setItemText(1, _translate("config", "ODD"))
        self.combo_parity_3.setItemText(2, _translate("config", "EVEN"))
        self.combo_parity_3.setItemText(3, _translate("config", "MARK"))
        self.combo_parity_3.setItemText(4, _translate("config", "SPACE"))
        self.label_stop_3.setText(_translate("config", "?????????"))
        self.combo_stop_3.setItemText(0, _translate("config", "1"))
        self.combo_stop_3.setItemText(1, _translate("config", "1.5"))
        self.combo_stop_3.setItemText(2, _translate("config", "2"))
        self.label_fw_path_1.setText(_translate("config", "???????????????2"))
        self.pbt_sel_file_1.setText(_translate("config", "????????????"))
