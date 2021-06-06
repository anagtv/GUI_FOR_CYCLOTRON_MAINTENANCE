#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license

# Title: PyQt5 lesson 14              Version: 1.0
# Date: 09-01-17                      Language: python3
# Description: pyqt5 gui and opening files
# pythonprogramming.net from PyQt4 to PyQt5
###############################################################
# do something


import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtGui import QIcon, QColor,QStandardItemModel,QMouseEvent
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox,QTableWidget,QTableWidgetItem,QTabWidget
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog,QScrollArea,QFrame
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtCore, QtWidgets
from numpy import arange, sin, pi
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
sys.path.append("/Users/anagtv/Desktop/Cyclotron_python/")
sys.path.append("/Users/anagtv/GUI_CYCLOTRON_BOTH_TARGETS")
import saving_files_summary_list_20200420
import getting_subsystems
import managing_files
import saving_trends
import columns_names
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
import matplotlib.patches as mpatch
import numpy as np
import os
import tfs
from matplotlib.widgets import CheckButtons
#import datetime
from datetime import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import source_studies_no_foil
from datetime import datetime
import os, sys
import matplotlib
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge, Rectangle
import target_information_class
import plotting_summary_files_one_target_1_4
import time
from datetime import datetime, timedelta
COLORS = ['#1E90FF','#FF4500','#32CD32',"#6A5ACD","#20B2AA","#00008B","#A52A2A","#228B22","#FF3300","#3366FF","#FF9933"]
COLUMNS_SOURCE = ["FILE","DATE","TARGET","FOIL","CURRENT_MAX", "CURRENT_MIN","CURRENT_AVE","CURRENT_STD","VOLTAGE_MAX","VOLTAGE_MIN","VOLTAGE_AVE","VOLTAGE_STD","HFLOW",
    "RATIO_MAX", "RATIO_MIN","RATIO_AVE","RATIO_STD"] 
COLUMNS_VACUUM = ["FILE","DATE","TARGET","FOIL","PRESSURE_MAX","PRESSURE_MIN","PRESSURE_AVE","PRESSURE_STD"]
COLUMNS_MAGNET = ["FILE","DATE","TARGET","FOIL","CURRENT_MAX","CURRENT_MIN","CURRENT_AVE","CURRENT_STD"]
COLUMNS_RF =  ["FILE","DATE","TARGET","FOIL","DEE1_VOLTAGE_MAX","DEE1_VOLTAGE_MIN","DEE1_VOLTAGE_AVE","DEE1_VOLTAGE_STD","DEE2_VOLTAGE_MAX","DEE2_VOLTAGE_MIN","DEE2_VOLTAGE_AVE","DEE2_VOLTAGE_STD",
    "FORWARD_POWER_MAX","FORWARD_POWER_MIN","FORWARD_POWER_AVE","FORWARD_POWER_STD","REFLECTED_POWER_MAX","REFLECTED_POWER_MIN","REFLECTED_POWER_AVE","REFLECTED_POWER_STD",
    "PHASE_LOAD_MAX","PHASE_LOAD_MIN","PHASE_LOAD_AVE","PHASE_LOAD_STD"]
COLUMNS_BEAM = ["FILE","DATE","TARGET","FOIL","COLL_CURRENT_L_MAX","COLL_CURRENT_L_MIN","COLL_CURRENT_L_AVE","COLL_CURRENT_L_STD","COLL_CURRENT_R_MAX","COLL_CURRENT_R_MIN","COLL_CURRENT_R_AVE","COLL_CURRENT_R_STD"
    ,"RELATIVE_COLL_CURRENT_L_MAX","RELATIVE_COLL_CURRENT_L_MIN","RELATIVE_COLL_CURRENT_L_AVE","RELATIVE_COLL_CURRENT_L_STD",
    "RELATIVE_COLL_CURRENT_R_MAX","RELATIVE_COLL_CURRENT_R_MIN","RELATIVE_COLL_CURRENT_R_AVE","RELATIVE_COLL_CURRENT_R_STD",
    "TARGET_CURRENT_MAX","TARGET_CURRENT_MIN","TARGET_CURRENT_AVE","TARGET_CURRENT_STD","FOIL_CURRENT_MAX","FOIL_CURRENT_MIN","FOIL_CURRENT_AVE","FOIL_CURRENT_STD",
    "EXTRACTION_LOSSES_MAX","EXTRACTION_LOSSES_MIN","EXTRACTION_LOSSES_AVE","EXTRACTION_LOSSES_STD"]
COLUMNS_EXTRACTION = ["FILE","DATE","TARGET","FOIL","CAROUSEL_POSITION_MAX","CAROUSEL_POSITION_MIN","CAROUSEL_POSITION_AVE","CAROUSEL_POSITION_STD"
    ,"BALANCE_POSITION_MAX","BALANCE_POSITION_MIN","BALANCE_POSITION_AVE","BALANCE_POSITION_STD"]

measurements_maintenance_central_region = ["CYCLOTRON","DATE","CENTRAL_REGION_(A)_BEFORE","CENTRAL_REGION_(B)_BEFORE", "CENTRAL_REGION_(C)_BEFORE","CENTRAL_REGION_(D)_BEFORE","CENTRAL_REGION_(A)_AFTER","CENTRAL_REGION_(B)_AFTER", "CENTRAL_REGION_(C)_AFTER","CENTRAL_REGION_(D)_AFTER"]#,"DEE 1 (A)","DEE 1 (B)", "DEE 1 (C)","DEE 1 (D)","DEE 2 (E)", "DEE 2 (F)","DEE 2 (G)", "DEE 2 (H)","DEE 1 (A)","DEE 1 (B) W", "DEE 1 (C) W","DEE 1 (D) W","DEE 2 (E) W", "DEE 2 (F) W","DEE 2 (G) W", "DEE 2 (H) W"]
measurements_maintenance_rf_1 = ["CYCLOTRON","DATE","RF_1_HEIGHT_A_BEFORE","RF_1_HEIGHT_B_BEFORE", "RF_1_HEIGHT_C_BEFORE","RF_1_HEIGHT_D_BEFORE","RF_1_HEIGHT_A_AFTER","RF_1_HEIGHT_B_AFTER", "RF_1_HEIGHT_C_AFTER","RF_1_HEIGHT_D_AFTER",
        "RF_1_THICKNESS_A_BEFORE","RF_1_THICKNESS_B_BEFORE", "RF_1_THICKNESS_C_BEFORE","RF_1_THICKNESS_D_BEFORE","RF_1_THICKNESS_A_AFTER","RF_1_THICKNESS_B_AFTER", "RF_1_THICKNESS_C_AFTER","RF_1_THICKNESS_D_AFTER"]#,"DEE 1 (A)","DEE 1 (B)", "DEE 1 (C)","DEE 1 (D)","DEE 2 (E)", "DEE 2 (F)","DEE 2 (G)", "DEE 2 (H)","DEE 1 (A)","DEE 1 (B) W", "DEE 1 (C) W","DEE 1 (D) W","DEE 2 (E) W", "DEE 2 (F) W","DEE 2 (G) W", "DEE 2 (H) W"]
measurements_maintenance_rf_2 = ["CYCLOTRON","DATE","RF_2_HEIGHT_E_BEFORE","RF_2_HEIGHT_F_BEFORE", "RF_2_HEIGHT_G_BEFORE","RF_2_HEIGHT_H_BEFORE","RF_2_HEIGHT_E_AFTER","RF_2_HEIGHT_F_AFTER", "RF_2_HEIGHT_G_AFTER","RF_2_HEIGHT_H_AFTER",
        "RF_2_THICKNESS_E_BEFORE","RF_2_THICKNESS_F_BEFORE", "RF_2_THICKNESS_G_BEFORE","RF_2_THICKNESS_H_BEFORE","RF_2_THICKNESS_E_AFTER","RF_2_THICKNESS_F_AFTER", "RF_2_THICKNESS_G_AFTER","RF_2_THICKNESS_H_AFTER"]#,"DEE 1 (A)","DEE 1 (B)", "DEE 1 (C)","DEE 1 (D)","DEE 2 (E)", "DEE 2 (F)","DEE 2 (G)", "DEE 2 (H)","DEE 1 (A)","DEE 1 (B) W", "DEE 1 (C) W","DEE 1 (D) W","DEE 2 (E) W", "DEE 2 (F) W","DEE 2 (G) W", "DEE 2 (H) W"]
measurements_maintenance_col = ["CYCLOTRON","DATE","SEPARATION_COL_1_BEFORE","APERTURE_COL_1_BEFORE","SEPARATION_COL_2_BEFORE","APERTURE_COL_2_BEFORE","SEPARATION_COL_1_AFTER","APERTURE_COL_1_AFTER","SEPARATION_COL_2_AFTER","APERTURE_COL_2_AFTER"]
measurements_maintenance_midplane = ["CYCLOTRON","DATE","ACTUAL_A","ACTUAL_B","ACTUAL_C","ACTUAL_D","ACTUAL_E","ACTUAL_F","ACTUAL_G","ACTUAL_H","VARIANCE_A","VARIANCE_B","VARIANCE_C","VARIANCE_D","VARIANCE_E","VARIANCE_F","VARIANCE_G","VARIANCE_H"] 
measurements_maintenance_midplane_dee1 = ["ACTUAL_A","ACTUAL_B","ACTUAL_C","ACTUAL_D"] 
measurements_maintenance_midplane_dee2 = ["ACTUAL_E","ACTUAL_F","ACTUAL_G","ACTUAL_H"] 
measurements_maintenance_midplane_dee1_ref = ["REF_A","REF_B","REF_C","REF_D"] 
measurements_maintenance_midplane_dee2_ref = ["REF_E","REF_F","REF_G","REF_H"] 
measurements_source_performance = ["CYCLOTRON","DATE","CURRENT_0","CURRENT_50","CURRENT_100","CURRENT_150","CURRENT_200","CURRENT_250","CURRENT_300","CURRENT_350","CURRENT_400","CURRENT_450","CURRENT_500","CURRENT_550","CURRENT_600"]
measurements_beam_performance = ["CYCLOTRON","DATE","DEE_VOLTAGE","MAGNET_I","GAS_FLOW","VACUUM","I_ION_SOURCE","I_PROBE","I_FOIL","I_TARGET","I_COLL_LOW","I_COLL_UP"]
measurements_collimators_values = ["CYCLOTRON","DATE","COLL_1_APERTURE_BEFORE","COLL_2_APERTURE_BEFORE","COLL_1_SEPARATION_BEFORE","COLL_2_SEPARATION_BEFORE","COLL_1_L_IMPEDANCE_BEFORE","COLL_1_U_IMPEDANCE_BEFORE","COLL_2_L_IMPEDANCE_BEFORE","COLL_2_U_IMPEDANCE_BEFORE",
"COLL_1_APERTURE_AFTER","COLL_2_APERTURE_AFTER","COLL_1_SEPARATION_AFTER","COLL_2_SEPARATION_AFTER","COLL_1_L_IMPEDANCE_AFTER","COLL_1_U_IMPEDANCE_AFTER","COLL_2_L_IMPEDANCE_AFTER","COLL_2_U_IMPEDANCE_AFTER"]
measurements_motor_values = ["CYCLOTRON","DATE","FLAP_1_BEFORE","FLAP_2_BEFORE","CARROUSSEL_1_BEFORE","CARROUSSEL_2_BEFORE","BALANCE_BEFORE","FLAP_1_AFTER","FLAP_2_AFTER","CARROUSSEL_1_AFTER","CARROUSSEL_2_AFTER","BALANCE_AFTER"]
measurements_impedance_values = ["CYCLOTRON","DATE","PROBE_BEFORE","TARGET_1_BEFORE","TARGET_4_BEFORE","CARROUSSEL_1_BEFORE","CARROUSSEL_2_BEFORE","BALANCE_BEFORE","PROBE_AFTER","TARGET_1_AFTER","TARGET_4_AFTER","CARROUSSEL_1_AFTER","CARROUSSEL_2_AFTER","BALANCE_AFTER"]
measurements_rf_flaps = ["CYCLOTRON","DATE","FLAP1_0","FLAP1_50","FLAP1_100","FLAP2_0","FLAP2_50","FLAP_2_100"]

#matplotlib.use('Qt5Agg')

class UpdateFrame(QFrame):
    def __init__(self, parent=None):
        super(UpdateFrame, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        for i in range(25):
            listFrame = QFrame()
            listFrame.setStyleSheet('background-color: white;'
                                    'border: 1px solid #4f4f51;'
                                    'border-radius: 0px;'
                                    'margin: 2px;'
                                    'padding: 2px')
            listFrame.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            listFrame.setGeometry(50, 50, 1500, 1000)
            
            self.layout.addWidget(listFrame)

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.frameWidget = UpdateFrame(self)

        # Set the frame widget to be part of the scroll area
        
        self.setGeometry(50, 50, 1500, 1000)
        self.setStyleSheet("background-color: #fdfdfe;")
        self.setWindowTitle('pyqt5 Tut')
        self.setWindowIcon(QIcon('pic.png'))
        self.current_row = 0
        self.current_row_folder = 0
        self.current_row_statistics = 0
        self.current_row_analysis = 0 
        self.row_to_plot = 0
        self.current_row_observables = 0
        self.current_row_observables_tab3 = 0

        self.target_1_value = 0
        self.target_4_value = 0
        self.max_min_value = 0        
        self.week_value = 0
        self.day_value = 1
        self.flag_no_gap = 1
        #
        self.df_central_region = pd.DataFrame(columns=measurements_maintenance_central_region)
        self.df_source_performance = pd.DataFrame(columns=measurements_source_performance)
        self.df_beam_performance = pd.DataFrame(columns=measurements_beam_performance)
        self.df_rf_1 = pd.DataFrame(columns=measurements_maintenance_rf_1)
        #self.df_rf_dee1_old = pd.DataFrame(columns=measurements_maintenance_rf_1)
        self.df_rf_2 = pd.DataFrame(columns=measurements_maintenance_rf_2)
        self.df_col = pd.DataFrame(columns=measurements_maintenance_col)
        self.df_mid_plane = pd.DataFrame(columns=measurements_maintenance_midplane)
        self.df_mid_plane_dee1 = pd.DataFrame(columns=measurements_maintenance_midplane_dee1)
        self.df_mid_plane_dee2 = pd.DataFrame(columns=measurements_maintenance_midplane_dee2)
        self.df_mid_plane_dee1_ref = pd.DataFrame(columns=measurements_maintenance_midplane_dee1_ref)
        self.df_mid_plane_dee2_ref = pd.DataFrame(columns=measurements_maintenance_midplane_dee2_ref)
        self.df_source = pd.DataFrame(columns=COLUMNS_SOURCE)
        self.df_vacuum = pd.DataFrame(columns=COLUMNS_VACUUM)
        self.df_magnet = pd.DataFrame(columns=COLUMNS_MAGNET)
        self.df_beam = pd.DataFrame(columns=COLUMNS_BEAM )
        self.df_rf = pd.DataFrame(columns=COLUMNS_RF)
        self.df_extraction = pd.DataFrame(columns=COLUMNS_EXTRACTION)

        mainMenu = self.menuBar()

        editorOpen = mainMenu.addMenu('&Open')
        self.openFolder = QAction('Open Folder', self)
        self.openFolder.triggered.connect(self.file_folder)   
        editorOpen.addAction(self.openFolder)


        openPlotSource = QAction('Plot Source', self)
        openPlotSource.triggered.connect(self.plot_source)  
        openPlotTarget1 = QAction('Plot Target 1', self)
        openPlotTarget1.triggered.connect(self.plot_target_1) 
        openPlotTarget4 = QAction('Plot Target 4', self)
        openPlotTarget4.triggered.connect(self.plot_target_4)       
        editorMenuPlot = mainMenu.addMenu('&Plot')
        editorMenuPlot.addAction(openPlotSource)
        editorMenuPlot.addAction(openPlotTarget1)
        editorMenuPlot.addAction(openPlotTarget4)
        self.setWindowTitle("Cyclotron Analysis")

        #self.main_widget = QtWidgets.QWidget(self)
       

        self.main_widget = QtWidgets.QWidget()
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidget(self.main_widget)
        self.scrollArea.setWidgetResizable(True)

        #self.scrollArea.setObjectName("scrollArea")
        #self.scrollArea.setEnabled(True)
        #self.horizontalLayout.addWidget(self.main_widget)

        lay = QtWidgets.QVBoxLayout(self.main_widget)
        #layout = QtWidgets.QVBoxLayout(self)
        #layout.addWidget(self.scrollArea)
        
        #centralWidget.setObjectName("centralWidget")
        #self.main_widget.setLayout(self.horizontalLayout)
        
        self.df_subsystem_source_all = []
        self.df_subsystem_vacuum_all = []
        self.df_subsystem_magnet_all = []
        self.df_subsystem_rf_all = []
        self.df_subsystem_extraction_all = []
        self.df_subsystem_beam_all = []
        self.df_subsystem_pressure_all = []

        #l = QtWidgets.QVBoxLayout(self.main_widget)
        #m = QtWidgets.QVBoxLayout(self.plot_widget)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.home(lay)
        self.setMinimumSize(1400, 700)
        #self.resize(450, 100)

    def home(self, main_layout):

        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        #self.tabs.resize(300,200)

        # Add tabs
        #self.tabs.addTab(self.tab1,"Individual Files")
        #self.tabs.addTab(self.tab3,"Individual Files (source)")
        #self.tabs.addTab(self.tab2,"Trends")
        self.tabs.addTab(self.tab1,"Cyclotron ")
        self.tabs.addTab(self.tab2,"Time Analysis")
        self.tabs.addTab(self.tab3,"Charge Analysis")
        
        # Create first tab

        widget = QtWidgets.QWidget(self.tab1)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.show()
        main_layout.addWidget(self.tabs)

        # TAB 4 (CENTRAL REGION)

        self.widget_tab1 = QtWidgets.QWidget(self.tab1)
        #self.widget_tab1.setLayout(main_layout)
        self.widget_tab1.setObjectName("widget")

        #         
        self.plot_evolution_source = Canvas("SOURCE",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_source.setGeometry(QtCore.QRect(520,225, 220, 220))

        self.plot_evolution_collimator_1 = Canvas("COLLIMATOR 1",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_collimator_1.setGeometry(QtCore.QRect(520, 10, 220, 220))

        self.plot_evolution_collimator_2 = Canvas("COLLIMATOR 2",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_collimator_2.setGeometry(QtCore.QRect(520,440, 220, 220))

        self.plot_evolution_target_1 = Canvas("TARGET 1",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_target_1.setGeometry(QtCore.QRect(100, 165, 350, 350))

        self.plot_evolution_target_4 = Canvas("TARGET 4",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_target_4.setGeometry(QtCore.QRect(800, 165, 350, 350))

        self.plot_evolution_foil_1 = Canvas("FOIL 1",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_foil_1.setGeometry(QtCore.QRect(40, 40, 150, 150))
        self.plot_evolution_foil_2 = Canvas("FOIL 2",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_foil_2.setGeometry(QtCore.QRect(200, 5, 150, 150))
        self.plot_evolution_foil_3 = Canvas("FOIL 3",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_foil_3.setGeometry(QtCore.QRect(370, 40, 150, 150))
        self.plot_evolution_foil_6 = Canvas("FOIL 6",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_foil_6.setGeometry(QtCore.QRect(40, 450, 150, 150))
        self.plot_evolution_foil_5 = Canvas("FOIL 5",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_foil_5.setGeometry(QtCore.QRect(200, 500, 150, 150))
        self.plot_evolution_foil_4 = Canvas("FOIL 4",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_foil_4.setGeometry(QtCore.QRect(370, 450, 150, 150))
        #
        self.plot_evolution_foil_1_2 = Canvas("FOIL 1",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_foil_1_2.setGeometry(QtCore.QRect(740, 40, 150, 150))
        self.plot_evolution_foil_2_2 = Canvas("FOIL 2",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_foil_2_2.setGeometry(QtCore.QRect(900, 5, 150, 150))
        self.plot_evolution_foil_3_2 = Canvas("FOIL 3",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_foil_3_2.setGeometry(QtCore.QRect(1070, 40, 150, 150))
        self.plot_evolution_foil_6_2 = Canvas("FOIL 6",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_foil_6_2.setGeometry(QtCore.QRect(740, 450, 150, 150))
        self.plot_evolution_foil_5_2 = Canvas("FOIL 5",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_foil_5_2.setGeometry(QtCore.QRect(900, 500, 150, 150))
        self.plot_evolution_foil_4_2 = Canvas("FOIL 4",width=7, height=50, dpi=200, parent=self.tab1) 
        self.plot_evolution_foil_4_2.setGeometry(QtCore.QRect(1070, 450, 150, 150))
        # TAB 2
        self.label_centralregion = QLabel("Input parameters:",self.tab2)
        self.label_centralregion.setGeometry(QtCore.QRect(630, 15, 150, 30))
        #
        self.label_cycltron = QLabel("Cyclotron",self.tab2)
        self.label_cycltron.setGeometry(QtCore.QRect(430, 40, 150, 30))
        #
        self.label_parameter = QLabel("Parameter",self.tab2)
        self.label_parameter.setGeometry(QtCore.QRect(630, 40, 150, 30))
        #
        self.label_weeks = QLabel("Number of weeks",self.tab2)
        self.label_weeks.setGeometry(QtCore.QRect(830, 40, 150, 30))
        #
        self.last_maintenance_input = QLabel("Last Maintenance (Input)",self.tab2)
        self.last_maintenance_input.setGeometry(QtCore.QRect(1030, 40, 150, 30))
        #
        self.cyclotron_information = QtWidgets.QLineEdit(self.tab2)
        self.cyclotron_information.setGeometry(QtCore.QRect(430, 70, 100, 30))
        #
        self.parameters_information = QtWidgets.QLineEdit(self.tab2)
        self.parameters_information.setGeometry(QtCore.QRect(630, 70, 100, 30))
        #
        self.weeks_number = QtWidgets.QLineEdit(self.tab2)
        self.weeks_number.setGeometry(QtCore.QRect(830, 70, 100, 30))
        #
        self.maintenance_input = QtWidgets.QTextEdit(self.tab2)
        self.maintenance_input.setGeometry(QtCore.QRect(1030, 70, 100, 30))
        #
        #
        self.btn = QPushButton('Apply', self.tab2)
        self.btn.setGeometry(QtCore.QRect(600, 105, 450, 25))
        self.btn.clicked.connect(self.folder_analyze)
        #
        self.plot_time_evolution = Canvas_half(labels=['HIGH','MEDIUM','LOW'],width=100, height=100, dpi=200, parent=self.tab2) 
        self.plot_time_evolution.setGeometry(QtCore.QRect(50, 100, 300, 300))
        #
        self.explanation = QLabel("This software allows to analyze the temporal evolution of:",self.tab2)
        self.explanation.setGeometry(QtCore.QRect(30, 15, 400, 30))
        self.ion_source = QLabel("Ion Source",self.tab2)
        self.ion_source.setGeometry(QtCore.QRect(30, 40, 400, 30))
        self.vacuum = QLabel("Vacuum",self.tab2)
        self.vacuum.setGeometry(QtCore.QRect(30, 65, 400, 30))
        self.beam_size = QLabel("Beam Size and loses ",self.tab2)
        self.beam_size.setGeometry(QtCore.QRect(30, 90, 400, 30))
        self.target_volume = QLabel("Target volume ",self.tab2)
        self.target_volume.setGeometry(QtCore.QRect(30, 115, 400, 30))
        # 
        self.average_value = QLabel("Average",self.tab2)
        self.average_value.setGeometry(QtCore.QRect(170, 135, 150, 30))
        self.average_value.setFont(QFont("Arial", 18,QFont.Bold))
        self.plot_average_value = Canvas_tab2(10,width=6, height=40, dpi=200,parent=self.tab2) 
        self.plot_average_value.setGeometry(QtCore.QRect(20, 315, 460, 365))
        #
        #TABLEEEE
        self.tablestatistic_tab2 = QtWidgets.QTableWidget(self.tab2) 
        self.tablestatistic_tab2.setGeometry(QtCore.QRect(600, 560, 420, 100))
        self.tablestatistic_tab2.setRowCount(2)
        self.tablestatistic_tab2.setColumnCount(4)
        #self.tablestatistic_tab2.setColumnWidth(150,150)
        self.tablestatistic_tab2.setHorizontalHeaderLabels(["Date","File","Foil","Value"])
        #
        #PLOT TEMPORAL EVOLUTION
        self.plot_evolution_temporal = Canvas_tab2(12,width=7, height=50, dpi=200, parent=self.tab2) 
        self.plot_evolution_temporal.setGeometry(QtCore.QRect(430, 160, 750, 400)) 
        # TAB 2

    def folder_analyze(self):
        self.fileName_folder = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path = "/Users/anagtv/GUI_CYCLOTRON_BOTH_TARGETS/Test_results/"
        self.plot_evolution_temporal.axes.clear()
        if self.parameters_information.text() == "SOURCE":
            self.label_to_plot = ["PRESSURE_","CURRENT_"]
            self.legend_to_plot = ["VACUUM","ION SOURCE"]
            self.file_name = ["vacuum_evolution.pdf","ion_source_evolution.pdf"]
            self.vertical_value = [r"PRESSURE [10e-5 mbar]","CURRENT [mA]"]
            self.tfs_input = [tfs.read(os.path.join(self.output_path,columns_names.SUMMARY_FILE_NAMES[4])),tfs.read(os.path.join(self.output_path,columns_names.SUMMARY_FILE_NAMES[0])) ]
            self.column_names = ["CURRENT [mA]",r"PRESSURE [10e-5 mbar]"]
            self.column_ave = columns_names.COLUMNS_ION_SOURCE_AVE
            self.column_std = columns_names.COLUMNS_ION_SOURCE_STD
        elif self.parameters_information.text() == "VACUUM":
            self.label_to_plot = ["CURRENT_","PRESSURE_"]
            self.legend_to_plot = ["ION SOURCE","VACUUM"]
            self.file_name = ["ion_source_evolution.pdf","vacuum_evolution.pdf"]
            self.vertical_value = ["CURRENT [mA]",r"PRESSURE [10e-5 mbar]"]
            self.tfs_input = [tfs.read(os.path.join(self.output_path,columns_names.SUMMARY_FILE_NAMES[0])),tfs.read(os.path.join(self.output_path,columns_names.SUMMARY_FILE_NAMES[4]))]
            self.column_names = [r"PRESSURE [10e-5 mbar]","CURRENT [mA]"]
            self.column_ave = columns_names.COLUMNS_VACUUM_AVE
            self.column_std = columns_names.COLUMNS_VACUUM_STD
            self.tfs_input = tfs.read(os.path.join(self.output_path,columns_names.SUMMARY_FILE_NAMES[4]))  
        self.tfs_input_cyclotron = tfs.read(os.path.join(self.output_path,"table_summary_extraction.out")) 
        target_information_1 = target_information_class.target_information() 
        target_information_2 = target_information_class.target_information()
        self.target_information_summary = [target_information_1,target_information_2]
        self.place_to_plot = [self.plot_average_value,self.plot_evolution_temporal]
        self.targets_summary = [self.target_information_summary]
        for i in range(len(self.label_to_plot)):
            print ("PLOTTING")
            print (self.label_to_plot[i])
            print (self.place_to_plot[i])
            self.place_to_plot_i = self.place_to_plot[i]
            self.place_to_plot_i.axes.clear() 
            self.column = [self.label_to_plot[i],self.label_to_plot[i]]
            self.vertical_value_to_plot = self.vertical_value[i]
            self.file_name_to_plot = self.file_name[i]
            print (self.tfs_input[i])
            self.tfs_input_to_plot = self.tfs_input[i]
            last_week = (datetime.strptime(self.tfs_input_to_plot.DATE.iloc[-1], '%Y-%m-%d').isocalendar()[1])
            first_week =  (int(last_week)-int(self.weeks_number.text()))
            print ("WEEEKS")
            print (last_week)
            print (first_week)
            self.firstday = (datetime.strptime(f'{2021}-W{int(first_week)-1}-1',"%Y-W%W-%w").date() + timedelta(days=7.9) ).strftime("%Y-%m-%d") 
            self.lastday = (datetime.strptime(f'{2021}-W{last_week-1}-1',"%Y-W%W-%w").date() + timedelta(days=6.9)).strftime("%Y-%m-%d")
            self.tfs_input_to_plot = self.tfs_input_to_plot[self.tfs_input_to_plot.DATE > self.firstday].reset_index(drop=True)
            print ("DATE")
            print (self.tfs_input_to_plot)
            self.targets = self.tfs_input_to_plot.drop_duplicates(subset="TARGET",keep = "first").TARGET
            self.targets = [int(np.min(self.targets)),int(np.max(self.targets))]
            print ("TARGETS")
            print (self.targets)
            print ("VALUE")         
            self.column_stat = self.label_to_plot[i]
            for j in range(len(self.targets)):
                print ("HEREEE")
                print ("TARGET")
                print (self.targets[j])
                self.target_information_summary[j].selecting_data_to_plot_reset(self.targets[j],self.tfs_input_to_plot) 
                plotting_summary_files_one_target_1_4.getting_stadistic_values(self,self.target_information_summary[j])
                self.target_information_summary[j].x_values = (self.tfs_input_to_plot.TARGET[self.tfs_input_to_plot.TARGET == str(self.targets[j])].index)
            self.plotting_evolution()   
        # Defining the classes for the two targets 
        #self.plot_evolution_source.ax.set_xlim([self.min_x-2,self.max_x+2])
    def plotting_evolution(self):    
        self.plot_evolution_temporal.fig.canvas.mpl_connect('pick_event', self.onpick_trends)  
        columns_names.initial_df(self)
        saving_trends.getting_summary(self)
        self.targets_summary_selected = self.target_information_summary
        #plotting_summary_files_one_target_1_4.plotting_trends(self)
        colors_i = [COLORS[4],COLORS[8]]
        colors_min = [COLORS[9],COLORS[10]]
        x_values = []
        self.fmts = ["o","^","v"]
        self.set_configuration = 1.035*np.max(self.target_information_summary[0].max_value)
        for j in list(range(0,len(self.tfs_input_to_plot.DATE),10)):
               print ("HEREEEEEEE!!!!")
               print (j)
               x_values.append(j)
               print (self.set_configuration)
               print (self.tfs_input_to_plot.DATE.iloc[j][5:])
               self.place_to_plot_i.axes.text(j-0.3, self.set_configuration,self.tfs_input_to_plot.DATE.iloc[j][5:], fontsize=10,rotation=90)
        for i in range(len(self.target_information_summary)):
            print ("INFORMATION")
            print (self.target_information_summary[i].x_values)
            print (self.target_information_summary[i].ave_value)
            ticks_to_use = list(range(1,len(self.tfs_input_to_plot.FILE),10))
            ticks_to_use_list = self.tfs_input_to_plot.FILE[::int(len(self.tfs_input_to_plot.FILE)/15)] 
            self.place_to_plot_i.axes.set_xlabel("FILE",fontsize=10)
            self.place_to_plot_i.axes.set_ylabel(str(self.vertical_value_to_plot),fontsize=10)
            self.place_to_plot_i.axes.set_xticks(ticks_to_use)
            self.place_to_plot_i.axes.set_xticklabels(ticks_to_use_list.astype(float),rotation=45)
            self.place_to_plot_i.axes.errorbar(self.target_information_summary[i].x_values,self.target_information_summary[i].ave_value,yerr=self.target_information_summary[i].std_value,color=colors_i[i],fmt=self.fmts[0], picker=5)  
            self.place_to_plot_i.axes.errorbar(self.target_information_summary[i].x_values,self.target_information_summary[i].max_value,fmt=self.fmts[1], color=colors_min[i], picker=5)
            self.place_to_plot_i.axes.errorbar(self.target_information_summary[i].x_values,self.target_information_summary[i].min_value,fmt=self.fmts[2], color=colors_min[i], picker=5)
            self.place_to_plot_i.draw()
            self.place_to_plot_i.show() 
    
    def onpick_trends(self,event):
         thisline = event.artist
         xdata = thisline.get_xdata()
         ydata = thisline.get_ydata()
         ind = event.ind
         self.coordinates_x = xdata[ind][0]
         COLUMNS_GENERAL = ["DATE","FILE","FOIL"]
         for i in range(0,3,1): 
         #     self.tablestatistic_tab2.setItem(0,i, QTableWidgetItem(COLUMNS_GENERAL[i]))
               self.tablestatistic_tab2.setItem(0,i,QTableWidgetItem(str(getattr(self.tfs_input_to_plot,COLUMNS_GENERAL[i]).loc[self.coordinates_x])))
               #self.tablestatistic_tab2.setItem(0,i+3, QTableWidgetItem(str(self.column_names[i])))
         value = str(round(getattr(self.tfs_input_to_plot,self.column_ave[0]).loc[self.coordinates_x],1)) + "+-" + str(round(getattr(self.tfs_input_to_plot,self.column_std[0]).loc[self.coordinates_x],3))
         print ("VALUE")
         print (value)
         self.tablestatistic_tab2.setItem(0,3, QTableWidgetItem(value))

         
        
    def file_folder(self,values):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.dir_ = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        filename_completed = []
        for file in os.listdir(self.dir_):
             filename_completed.append(os.path.join(self.dir_,file))
        target = source_studies_no_foil.target_information()
        for file in filename_completed:
            [target_number,date_stamp,name,file_number,data_df] = source_studies_no_foil.selecting_data(file)
            target.selecting_data_to_plot_reset(data_df,target_number,datetime.strptime(date_stamp, '%Y-%m-%d'),datetime.strptime(date_stamp, '%Y-%m-%d').isocalendar()[1],file_number)
        self.df_target = source_studies_no_foil.cumulative_charge_target_collimators(target)
        self.df_source = source_studies_no_foil.cumulative_charge_folder(target)
        tfs.write("charge_collimators_target_2021.out",self.df_target)
        tfs.write("charge_source_2021_tcp.out",self.df_source)    
        self.plot_source()
        self.plot_target_1()
        self.plot_target_4()
        self.plot_collimator_1()
        self.plot_collimator_2()

    def plotting_trends(self):
        self.final_legend = []
        self.fmts = ["o","^","v"]
        for i in range(len(self.targets_summary)):
            getting_stadistic_values(self.targets_summary[i],self.column[i])
            self.targets_summary[i].x_values = (self.tfs_input_to_plot.TARGET[self.tfs_input_to_plot.TARGET == self.targets[i]].index)


    def plot_source(self):
        self.name_to_plot = "SOURCE"
        self.name_to_show = "SOURCE"
        self.limit_charge = 100000
        self.factor = 1000
        self.units = "Ah"
        self.df = self.df_source
        #self.df = tfs.read("/Users/anagtv/GUI_CYCLOTRON_BOTH_TARGETS/charge_source_2021_tcp.out")
        self.create_radial_chart(self.plot_evolution_source)

    def plot_collimator_1(self):
        #self.df = tfs.read("/Users/anagtv/GUI_CYCLOTRON_BOTH_TARGETS/charge_collimators_target_2021.out")
        self.df = self.df_target
        self.target = np.min(self.df.TARGET_NUMBER)
        self.place_collimator = self.plot_evolution_collimator_1
        self.plot_collimator()

    def plot_collimator_2(self):
        #self.df = tfs.read("/Users/anagtv/GUI_CYCLOTRON_BOTH_TARGETS/charge_collimators_target_2021.out")
        self.df = self.df_target
        self.target = np.max(self.df.TARGET_NUMBER)
        self.place_collimator = self.plot_evolution_collimator_2
        self.plot_collimator()

    def plot_collimator(self):
        self.name_to_plot = "COLLIMATORS"
        self.name_to_show = "COLLIMATOR " + str(int(self.target))
        self.df = self.df[self.df.TARGET_NUMBER == self.target]
        self.limit_charge = 5000
        self.factor = 1
        self.units = "uAh"
        #self.df = tfs.read("/Users/anagtv/GUI_CYCLOTRON_BOTH_TARGETS/charge_source_2021_tcp.out")
        self.create_radial_chart(self.place_collimator)

    def plot_target_1(self):
        #self.df = tfs.read("/Users/anagtv/GUI_CYCLOTRON_BOTH_TARGETS/charge_collimators_target_2021.out")
        self.df = self.df_target
        self.target = np.min(self.df.TARGET_NUMBER)
        self.place_target = self.plot_evolution_target_1
        self.plot_target()

    def plot_target_4(self):
        self.df = self.df_target
        #self.df = tfs.read("/Users/anagtv/GUI_CYCLOTRON_BOTH_TARGETS/charge_collimators_target_2021.out")
        self.target = np.max(self.df.TARGET_NUMBER)
        self.place_target = self.plot_evolution_target_4
        self.plot_target()
        
    
    def plot_target(self):
        self.name_to_plot = "TARGET_TOTAL"
        self.name_to_show = "TARGET " + str(int(self.target))
        self.target_min = np.min(self.df.TARGET_NUMBER)
        self.df = self.df[self.df.TARGET_NUMBER == self.target]
        self.df_foils = self.df.FOIL.drop_duplicates().sort_values()
        self.limit_charge = 15000
        self.factor = 1
        self.units = "uAh"
        self.create_radial_chart(self.place_target) 
        print ("TARGET")
        print (self.target)
        print ("MIN")
        print (np.min(self.df.TARGET_NUMBER))
        if self.target == self.target_min: 
            print ("FIRST TARGET")     
            place_foils = {"1": self.plot_evolution_foil_1,
                           "2": self.plot_evolution_foil_2,
                           "3": self.plot_evolution_foil_3,
                           "4": self.plot_evolution_foil_4,
                           "5": self.plot_evolution_foil_5,
                           "6": self.plot_evolution_foil_6}
        else:
            print ("SECOND TARGET")
            place_foils = {"1": self.plot_evolution_foil_1_2,
                           "2": self.plot_evolution_foil_2_2,
                           "3": self.plot_evolution_foil_3_2,
                           "4": self.plot_evolution_foil_4_2,
                           "5": self.plot_evolution_foil_5_2,
                           "6": self.plot_evolution_foil_6_2}
        for i in list(range(1,7,1)):
            place_foils[str(i)].ax.clear()
            self.name_to_show = "FOIL " + str(i)
            self.initial_plot(place_foils[str(i)])
        for foil in self.df_foils:         
           self.plot_foil(foil,place_foils[str(foil)])
        self.place_target.fig.canvas.mpl_connect('button_press_event', self.onpick) 
        #self.tab1.mousePressEvent(self,QMouseEvent)
    
    def plot_foil(self,foil,place_foil):
        self.name_to_plot = "FOIL_TOTAL"
        self.name_to_show = "FOIL " + str(foil)
        self.df = tfs.read("/Users/anagtv/GUI_CYCLOTRON_BOTH_TARGETS/charge_collimators_target_2021.out")
        self.df = self.df[self.df.TARGET_NUMBER == (self.target)]
        self.df = self.df[self.df.FOIL == str(foil)]
        self.limit_charge = 2500
        self.factor = 1
        self.units = "uAh"
        print ("DF")
        print (foil)
        print (self.df) 
        print (self.df.iloc[-1])   
        self.create_radial_chart(place_foil)

    def initial_plot(self,place):
        ring_width = 0.3
        outer_radius = 1.5
        inner_radius = outer_radius - ring_width
        color_theme = 'Green'
        color = plt.get_cmap(color_theme + 's')
        outer_edge_color, inner_edge_color = ['white', None]
        outer_ring, _ = place.ax.pie([10,1000],radius=1.2,
                        colors=[color(0.7), color(0.15)],
                        startangle = 90,
                       counterclock = False)
        place.ax.text(0,
                -1.5,
                str(self.name_to_show),
                horizontalalignment='center',
                verticalalignment='top',
                fontsize = 12,family = 'sans-serif')
        plt.setp( outer_ring, width=ring_width, edgecolor=outer_edge_color)
        plt.xticks(fontsize=10,rotation=90)
        plt.yticks(fontsize=10)
        place.draw()
        place.show()

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def calculate_rings(self,df,column_name,reset_value):
      if (getattr(df,column_name).iloc[-1]) < reset_value:
        rings=[[getattr(df,column_name).iloc[-1],reset_value-getattr(df,column_name).iloc[-1]],[0,0]]
        print ("HEREEEE")
      elif getattr(df,column_name).iloc[-1]/ reset_value < 2:
        print ("OR HEREEE")
        rings=[[getattr(df,column_name).iloc[-1],0],getattr(df,column_name).iloc[-1] % reset_value, reset_value-getattr(df,column_name).iloc[-1]% reset_value]
      else:
        print ("FINALLY")
        rings = [[0,0],[0,0]]
      return rings
    #USE: Create a center label in the middle of the radial chart.
    #INPUT: a df of row length 1 with the first column as the current metric value and the second column is the target metric value
    #OUTPUT: the proper text label
    def add_center_label(self,df,column_name,reset_value,place):
        percent = str(int(1.0*getattr(df,column_name).iloc[-1]/reset_value*100)) + '%'
        return place.ax.text(0,
               0.2,
               percent,
               horizontalalignment='center',
               verticalalignment='center',
               fontsize = 14,
               family = 'sans-serif')

    def add_sub_center_label(self,df,name,name_to_show,place):
        amount = str(int(getattr(df,name).iloc[-1]/self.factor)) + " " + self.units 
        place.ax.text(0,
                -1.6,
                str(name_to_show),
                horizontalalignment='center',
                verticalalignment='top',
                fontsize = 12,family = 'sans-serif')
        return place.ax.text(0,
                -.1,
                amount,
                horizontalalignment='center',
                verticalalignment='top',
                fontsize = 12,family = 'sans-serif')
        

    def create_radial_chart(self,place):
      # base styling logic
      #color_theme = 'Red'
      ring_width = 0.3
      outer_radius = 1.5
      inner_radius = outer_radius - ring_width
      # set up plot
      ind = self.name_to_plot
      if (getattr(self.df,self.name_to_plot).iloc[-1] < 0.35*self.limit_charge):
           print ("IT'S OK")
           color_theme = "Green"
      elif (getattr(self.df,self.name_to_plot).iloc[-1] > 0.35*self.limit_charge) & (getattr(self.df,self.name_to_plot).iloc[-1] < 0.7*self.limit_charge):
           color_theme = "Orange"
      else: 
           print ("IT'S NOT OK")
           print ("BAD")
           color_theme = "Red"
      color = plt.get_cmap(color_theme + 's')
      ring_arrays = self.calculate_rings(self.df,ind,self.limit_charge)   
      #fig, ax = plt.subplots()
      if getattr(self.df,ind).iloc[-1] > self.limit_charge:
        ring_to_label = 0
        outer_edge_color = None
        inner_edge_color = 'white'
      else:
        ring_to_label = 1
        outer_edge_color, inner_edge_color = ['white', None]
      # plot logic
      place.ax.clear()
      outer_ring, _ = place.ax.pie(ring_arrays[0],radius=1.5,
                        colors=[color(0.7), color(0.15)],
                        startangle = 90,
                        counterclock = False)
      plt.setp( outer_ring, width=ring_width, edgecolor=outer_edge_color)
      inner_ring, _ = place.ax.pie(ring_arrays[1],
                             radius=inner_radius,
                             colors=[color(0.55), color(0.05)],
                             startangle = 90,
                             counterclock = False,)
      plt.setp(inner_ring, width=ring_width, edgecolor=inner_edge_color)
      # add labels and format plots
      self.add_center_label(self.df,ind,self.limit_charge,place)
      self.add_sub_center_label(self.df,self.name_to_plot,self.name_to_show,place)
      #self.add_sub_sub_center_label(df,ind)
      #ax.axis('equal')
      place.ax.margins(0,0)
      place.ax.autoscale('enable')
      place.draw()
      place.show()
      #return self.plot_evolution_source

    def onClick(self,event):
       items = event.scenePos()

    def onpick(self,event):
        print ("HEREEE")
        #thisline = event.artist
        xdata = event.x
        ydata = event.y
        print ("XDATA")
        print (xdata)
        print (ydata)
        print (self.place_target)

    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
    


    def Clear(self):
        self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.draw()
        self.axes_1.clear()
        self.ui.widget_2.canvas.draw()
        self.ui.widget_3.canvas.ax.clear()
        self.ui.widget_3.canvas.draw()
        self.ui.widget_4.canvas.ax.clear()
        self.ui.widget_4.canvas.draw()


    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50 , 500, 300)


    def close_application(self):

        choice = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if choice == QMessageBox.Yes:
            print('quit application')
            sys.exit()
        else:
            pass


class Canvas(FigureCanvas):

    def __init__(self,name, width = 5, height = 5, dpi = 100, parent = None):
        #fig, (ax1, ax2) = plt.subplots(nrows=2)
        self.fig, self.ax = plt.subplots(nrows=1,ncols=1,figsize=(width,height))
        self.fig.patch.set_facecolor('xkcd:pale grey')
        self.fig.tight_layout(pad=3.0)
        plt.gcf().autofmt_xdate()
        self.ax.tick_params(labelsize=10)
        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)
        all_axes = self.fig.get_axes()
        for ax in all_axes:
            for sp in ax.spines.values():
                sp.set_visible(False)
        ring_width = 0.3
        outer_radius = 1.5
        inner_radius = outer_radius - ring_width
        color_theme = 'Green'
        color = plt.get_cmap(color_theme + 's')
        outer_edge_color, inner_edge_color = ['white', None]
        outer_ring, _ = self.ax.pie([10,1000],radius=1.2,
                        colors=[color(0.7), color(0.15)],
                        startangle = 90,
                        counterclock = False)
        self.ax.text(0,
                -1.5,
                str(name),
                horizontalalignment='center',
                verticalalignment='top',
                fontsize = 12,family = 'sans-serif')
        plt.setp( outer_ring, width=ring_width, edgecolor=outer_edge_color)
        plt.xticks(fontsize=10,rotation=90)
        plt.yticks(fontsize=10)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

class Canvas_tab2(FigureCanvas):
    def __init__(self,size_label, width = 5, height = 5, dpi = 100, parent = None):
        self.fig, self.axes = plt.subplots(1, sharex=True,figsize=(width,height))
        self.fig.tight_layout(pad=3.0)
        plt.gcf().autofmt_xdate()
        plt.rc('axes', titlesize=size_label)
        self.axes.tick_params(labelsize=10)
        plt.xticks(fontsize=12,rotation=90)
        plt.yticks(fontsize=12)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

class Canvas_half(FigureCanvas):
    def __init__(self,labels=['LOW','MEDIUM','HIGH'], width = 100, height = 30, dpi = 100, parent = None):
        self.fig, self.ax = plt.subplots(figsize=(width,height))
        self.N = len(labels) 
        self.ang_range, self.mid_points = self.degree_range(self.N)
        self.labels = labels[::-1]
        self.ax.axes.set_xticks([])
        self.ax.axes.set_yticks([])
        FigureCanvas.__init__(self, self.fig)
        self.gauge(labels, colors='RdYlGn', arrow=1, title='', fname=False)
        self.setParent(parent)

    def rot_text(self,ang): 
        rotation = np.degrees(np.radians(ang) * np.pi / np.pi - np.radians(90))
        return rotation

    def degree_range(self,n): 
        start = np.linspace(0,180,n+1, endpoint=True)[0:-1]
        end = np.linspace(0,180,n+1, endpoint=True)[1::]
        mid_points = start + ((end-start)/2.)
        return np.c_[start, end], mid_points

    def gauge(self,labels, \
          colors='jet_r', arrow=2, title='', fname=False):       
        if arrow > self.N: 
            raise Exception("\n\nThe category ({}) is greated than \
            the length\nof the labels ({})".format(arrow, self.N))
        if isinstance(colors, str):
            cmap = cm.get_cmap(colors, self.N)
            cmap = cmap(np.arange(self.N))
            colors = cmap[::-1,:].tolist()
        if isinstance(colors, list): 
            if len(colors) == self.N:
                colors = colors[::-1]
            else: 
                raise Exception("\n\nnumber of colors {} not equal \
                to number of categories{}\n".format(len(colors), self.N))
    
        patches = []
        for ang, c in zip(self.ang_range, colors): 
            # sectors
            patches.append(Wedge((0.,0.), .4, *ang, facecolor='w', lw=2))
            # arcs
            patches.append(Wedge((0.,0.), .4, *ang, width=0.10, facecolor=c, lw=2, alpha=0.5))
        
        [self.ax.add_patch(p) for p in patches]
        for mid, lab in zip(self.mid_points, labels): 

            self.ax.text(0.35 * np.cos(np.radians(mid)), 0.35 * np.sin(np.radians(mid)), lab, \
                horizontalalignment='center', verticalalignment='center', fontsize=14, \
                fontweight='bold', rotation = self.rot_text(mid))

        r = Rectangle((-0.4,-0.1),0.8,0.1, facecolor='w', lw=2)
        self.ax.add_patch(r)
        self.ax.text(0, -0.05, title, horizontalalignment='center', \
             verticalalignment='center', fontsize=22, fontweight='bold')
        pos = self.mid_points[abs(arrow - self.N)]    
        self.ax.arrow(0, 0, 0.225 * np.cos(np.radians(pos)), 0.225 * np.sin(np.radians(pos)), \
                 width=0.04, head_width=0.09, head_length=0.1, fc='k', ec='k')
        
        self.ax.add_patch(Circle((0, 0), radius=0.02, facecolor='k'))
        self.ax.add_patch(Circle((0, 0), radius=0.01, facecolor='w', zorder=11))       
        self.ax.set_frame_on(False)
        self.ax.axes.set_xticks([])
        self.ax.axes.set_yticks([])
        self.ax.axis('equal')
        plt.tight_layout()
        if fname:
            self.fig.savefig(fname, dpi=200)

if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()
