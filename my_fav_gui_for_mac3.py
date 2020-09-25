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
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon, QColor,QStandardItemModel
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
import matplotlib.pyplot as plt
import saving_files_summary
#import saving_files_summary_list
#import plotting_summary_files_one_target
#import saving_files_summary_list_20200420
import numpy as np
import os
import tfs
from matplotlib.widgets import CheckButtons
#import datetime
from datetime import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


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

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        for i in range(25):
            listFrame = QFrame()
            listFrame.setStyleSheet('background-color: white;'
                                    'border: 1px solid #4f4f51;'
                                    'border-radius: 0px;'
                                    'margin: 2px;'
                                    'padding: 2px')
            listFrame.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            listFrame.setGeometry(50, 50, 1500, 1000)
            
            layout.addWidget(listFrame)

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        frameWidget = UpdateFrame(self)

        # Set the frame widget to be part of the scroll area
        
        self.setGeometry(50, 50, 1500, 1000)
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

        openPlotPDD = QAction('Plot RF Dees', self)
        openPlotPDD.triggered.connect(self.file_plot)
        openPlotPDDR = QAction('Plot RF Dees (Reference)', self)
        openPlotPDDR.triggered.connect(self.file_plot_dr)
        openPlotPSP = QAction('Plot Source Performance', self)
        openPlotPSP.triggered.connect(self.file_plot_source)
        openPlotPSPR = QAction('Plot Source Performance (Reference)', self)
        openPlotPSPR.triggered.connect(self.file_plot_source_reference)
        openPlotPST = QAction('Plot Source Trendings', self)
        openPlotPST.triggered.connect(self.plot_source_trendings)
        openPlotPRFT = QAction('Plot RF Trendings (Height)', self)
        openPlotPRFT.triggered.connect(self.plot_rf_trendings_height)
        openPlotPRFTT = QAction('Plot RF Trendings (Thickness)', self)
        openPlotPRFTT.triggered.connect(self.plot_rf_trendings_thickness)

        openPlotLD1 = QAction('Load Dee 1', self)
        openPlotLD2 = QAction('Load Dee 2', self)
        openPlotLF = QAction('Load Flaps', self)
        openPlotLTV = QAction('Load Theorical Values', self)
        openPlotLD1.triggered.connect(self.on_click_load_rf1)
        openPlotLD2.triggered.connect(self.on_click_load_rf2)
        openPlotLF.triggered.connect(self.on_click_load_flaps)

        openPlotSD1 = QAction('Save Dee 1', self)
        openPlotSD2 = QAction('Save Dee 2', self)
        openPlotSMP = QAction('Save Mid Plane', self)
        openPlotFP = QAction('Save Flap Position', self)
        openPlotSD1.triggered.connect(self.on_click_rf_dee1)
        openPlotSD2.triggered.connect(self.on_click_rf_dee2)
        openPlotFP.triggered.connect(self.on_click_flaps)
        openPlotSMP.triggered.connect(self.on_click_midplane)
    
        openPlotLCR = QAction('Load Central Region', self)
        openPlotLBP = QAction('Load Beam Performance', self)
        openPlotLSPC = QAction('Load Source Performance (Current)', self)
        openPlotLC = QAction('Load Collimators', self)
        openPlotLM = QAction('Load Motors', self)
        openPlotLI = QAction('Load Impedance', self)
        openPlotLCR.triggered.connect(self.on_click_load_central)
        openPlotLBP.triggered.connect(self.on_click_load_beam_performance)
        openPlotLSPC.triggered.connect(self.on_click_load_source_performance)
        openPlotLC.triggered.connect(self.on_click_load_collimators)
        openPlotLM.triggered.connect(self.on_click_load_motors)
        openPlotLI.triggered.connect(self.on_click_load_impendance)

        openPlotSCR = QAction('Save Central Region', self)
        openPlotSBP = QAction('Save Beam Performance', self)
        openPlotSSPC = QAction('Save Source Performance (Current)', self)
        openPlotSSPV = QAction('Save Source Performance (Voltage)', self)
        openPlotSCR.triggered.connect(self.on_click_central)
        openPlotSBP.triggered.connect(self.on_click_beam_performance)
        openPlotSSPC.triggered.connect(self.on_click_source_performnance)
        openPlotSSPV.triggered.connect(self.on_click_source_performnance)
  
       
        openPlotSC1 = QAction('Save Collimator', self)
        openPlotSC1.triggered.connect(self.on_click_collimator)
        openPlotSM = QAction('Save Motor', self)
        openPlotSM.triggered.connect(self.on_click_motor)
        openPlotSC = QAction('Save Calibration', self)
        openPlotSC.triggered.connect(self.on_click_motor)
        openPlotSI = QAction('Save Impedance', self)
        openPlotSI.triggered.connect(self.on_click_impedance)
        #openPlotSMP.triggered.connect(self.on_click_midplane)

        editorMenu = mainMenu.addMenu('&Save Data Source')
        editorMenu.addAction(openPlotSCR)
        editorMenu.addAction(openPlotSBP)
        editorMenu.addAction(openPlotSSPC)
        editorMenu.addAction(openPlotSSPV)

        editorMenu = mainMenu.addMenu('&Load Data Source')
        editorMenu.addAction(openPlotLCR)
        editorMenu.addAction(openPlotLBP)
        editorMenu.addAction(openPlotLSPC)

        editorMenu_S = mainMenu.addMenu('&Save Data RF')
        editorMenu_S.addAction(openPlotSD1)
        editorMenu_S.addAction(openPlotSD2)
        editorMenu_S.addAction(openPlotSMP)
        editorMenu_S.addAction(openPlotFP)

        editorMenu_C = mainMenu.addMenu('&Save Data Collimators/Motors')
        editorMenu_C.addAction(openPlotSC1)
        editorMenu_C.addAction(openPlotSM)
        editorMenu_C.addAction(openPlotSC)
        editorMenu_C.addAction(openPlotSI)

        editorMenu_S = mainMenu.addMenu('&Load Data RF')
        editorMenu_S.addAction(openPlotLTV)
        editorMenu_S.addAction(openPlotLD1)
        editorMenu_S.addAction(openPlotLD2)
        editorMenu_S.addAction(openPlotLF)
        editorMenu_S.addAction(openPlotLC)
        editorMenu_S.addAction(openPlotLM)
        editorMenu_S.addAction(openPlotLI)


        
        editorMenuPlot = mainMenu.addMenu('&Plot')
        editorMenuPlot.addAction(openPlotPDD)
        editorMenuPlot.addAction(openPlotPDDR)
        editorMenuPlot.addAction(openPlotPSP)
        editorMenuPlot.addAction(openPlotPSPR)
        editorMenuPlot.addAction(openPlotPST)
        editorMenuPlot.addAction(openPlotPRFT)
        editorMenuPlot.addAction(openPlotPRFTT)
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
        self.tab4 = QtWidgets.QWidget()
        self.tab5 = QtWidgets.QWidget()
        self.tab6 = QtWidgets.QWidget()
        self.tab7 = QtWidgets.QWidget()
        #self.tabs.resize(300,200)

        # Add tabs
        #self.tabs.addTab(self.tab1,"Individual Files")
        #self.tabs.addTab(self.tab3,"Individual Files (source)")
        #self.tabs.addTab(self.tab2,"Trends")
        self.tabs.addTab(self.tab1,"Maintenance (Source)")
        self.tabs.addTab(self.tab2,"Maintenance (RF)")
        self.tabs.addTab(self.tab3,"Maintenance (Collimators & Flap)")
        self.tabs.addTab(self.tab4,"Maintenance (Extraction)")
        self.tabs.addTab(self.tab5,"Maintenance (Trendings)")
        self.tabs.addTab(self.tab6,"Maintenance (Trendings RF)")
        self.tabs.addTab(self.tab7,"Maintenance (Trendings RF (2))")
        # Create first tab
        
   
        # Add tabs to widget
                #self.setLayout(self.layout)


        # TAB 1

        
        widget = QtWidgets.QWidget(self.tab1)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.show()
        main_layout.addWidget(self.tabs)

        # TAB 4 (CENTRAL REGION)

        self.widget_tab1 = QtWidgets.QWidget(self.tab1)
        #self.widget_tab1.setLayout(main_layout)
        self.widget_tab1.setObjectName("widget")

        #self.textEdit = QtWidgets.QTextEdit()
        #self.toolbar_tab2.setGeometry(QtCore.QRect(250, 10, 1200, 800))

        #self.textEdit_files = QtWidgets.QTextEdit(self.tab1)
        #self.textEdit_files.setGeometry(QtCore.QRect(250, 10, 800, 600))

        self.label_cyclotron = QLabel("Location",self.tab1)
        self.label_cyclotron.setGeometry(QtCore.QRect(30, 5, 100, 30))
        self.textbox_cyclotron_location = QtWidgets.QLineEdit(self.tab1)
        self.textbox_cyclotron_location.setGeometry(QtCore.QRect(90, 5, 100, 30))

        self.label_cyclotron = QLabel("Date (YYYY/MM/DD)",self.tab1)
        self.label_cyclotron.setGeometry(QtCore.QRect(220, 5,125, 30))
        self.textbox_date_location = QtWidgets.QLineEdit(self.tab1)
        self.textbox_date_location.setGeometry(QtCore.QRect(360, 5, 100, 30))


        self.label_centralregion = QLabel("Central Region:",self.tab1)
        self.label_centralregion.setGeometry(QtCore.QRect(30, 40, 150, 30))
        #
        self.label_centralregion_before = QLabel("Before",self.tab1)
        self.label_centralregion_before.setGeometry(QtCore.QRect(60, 65, 150, 30))
        #
        self.label_centralregion_after = QLabel("After",self.tab1)
        self.label_centralregion_after.setGeometry(QtCore.QRect(160, 65, 150, 30))
        #
        self.label_centralregion_reference = QLabel("Reference",self.tab1)
        self.label_centralregion_reference.setGeometry(QtCore.QRect(260, 65, 150, 30))
        #
        self.label_centralregion_a = QLabel("(A):",self.tab1)
        self.label_centralregion_a.setGeometry(QtCore.QRect(30, 95, 80, 30))
        self.textbox_centralregion_a_before = QtWidgets.QLineEdit(self.tab1)
        self.textbox_centralregion_a_before.setGeometry(QtCore.QRect(60, 95, 100, 30))
        #
        self.textbox_centralregion_a_after = QtWidgets.QLineEdit(self.tab1)
        self.textbox_centralregion_a_after.setGeometry(QtCore.QRect(160, 95, 100, 30))
        #
        self.textbox_centralregion_a_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_centralregion_a_reference.setGeometry(QtCore.QRect(260, 95, 100, 30))
        #
        self.label_centralregion_b = QLabel("(B):",self.tab1)
        self.label_centralregion_b.setGeometry(QtCore.QRect(30, 125, 100, 30))
        self.textbox_centralregion_b_before = QtWidgets.QLineEdit(self.tab1)
        self.textbox_centralregion_b_before.setGeometry(QtCore.QRect(60, 125, 100, 30))
        #
        self.textbox_centralregion_b_after = QtWidgets.QLineEdit(self.tab1)
        self.textbox_centralregion_b_after.setGeometry(QtCore.QRect(160, 125, 100, 30))
        #
        self.textbox_centralregion_b_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_centralregion_b_reference.setGeometry(QtCore.QRect(260, 125, 100, 30))
        #
        self.label_centralregion_c = QLabel("(C):",self.tab1)
        self.label_centralregion_c.setGeometry(QtCore.QRect(30, 155, 100, 30))
        self.textbox_centralregion_c_before = QtWidgets.QLineEdit(self.tab1)
        self.textbox_centralregion_c_before.setGeometry(QtCore.QRect(60, 155, 100, 30))
        #
        self.textbox_centralregion_c_after = QtWidgets.QLineEdit(self.tab1)
        self.textbox_centralregion_c_after.setGeometry(QtCore.QRect(160, 155, 100, 30))
        #
        self.textbox_centralregion_c_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_centralregion_c_reference.setGeometry(QtCore.QRect(260, 155, 100, 30))
        #
        self.label_centralregion_d = QLabel("(D):",self.tab1)
        self.label_centralregion_d.setGeometry(QtCore.QRect(30, 185, 100, 30))
        self.textbox_centralregion_d_before = QtWidgets.QLineEdit(self.tab1)
        self.textbox_centralregion_d_before.setGeometry(QtCore.QRect(60, 185, 100, 30))
        #
        self.textbox_centralregion_d_after = QtWidgets.QLineEdit(self.tab1)
        self.textbox_centralregion_d_after.setGeometry(QtCore.QRect(160, 185, 100, 30))
        #
        self.textbox_centralregion_d_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_centralregion_d_reference.setGeometry(QtCore.QRect(260, 185, 100, 30))

        # ION SOURCE PERFORMANCE 

        self.label_source = QLabel("Ion Source",self.tab1)
        self.label_source.setGeometry(QtCore.QRect(380, 40, 120, 30))
        self.label_source_current = QLabel("Current [mA]",self.tab1)
        self.label_source_current.setGeometry(QtCore.QRect(380, 70, 120, 30))
        #
        self.label_is = QLabel("Ion Source",self.tab1)
        self.label_is.setGeometry(QtCore.QRect(480, 40, 120, 30))
        self.label_voltage = QLabel("Voltage [V]",self.tab1)
        self.label_voltage.setGeometry(QtCore.QRect(480, 60, 120, 30))
        #
        self.label_probe_current = QLabel("Probe Current",self.tab1)
        self.label_probe_current.setGeometry(QtCore.QRect(580, 40, 150, 30))
        self.label_probe_current2 = QLabel("[uA]",self.tab1)
        self.label_probe_current2.setGeometry(QtCore.QRect(580, 60, 150, 30))
        #
        self.label_probe_current_ref1 = QLabel("Probe Current [uA]",self.tab1)
        self.label_probe_current_ref1.setGeometry(QtCore.QRect(680, 40, 150, 30))
        self.label_probe_current_ref2 = QLabel("Reference",self.tab1)
        self.label_probe_current_ref2.setGeometry(QtCore.QRect(680, 60, 150, 30))
        #
        self.label_current_0 = QLabel("0",self.tab1)
        self.label_current_0.setGeometry(QtCore.QRect(380, 115, 80, 30))
        self.textbox_voltage_0 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_voltage_0.setGeometry(QtCore.QRect(480, 115, 100, 30))
        #
        self.textbox_current_0 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_0.setGeometry(QtCore.QRect(580, 115, 100, 30))
        #
        self.textbox_current_0_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_0_reference.setGeometry(QtCore.QRect(680, 115, 100, 30))
        #
        self.label_current_50 = QLabel("50",self.tab1)
        self.label_current_50.setGeometry(QtCore.QRect(380, 145, 100, 30))
        self.textbox_voltage_50 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_voltage_50.setGeometry(QtCore.QRect(480, 145, 100, 30))
        #
        self.textbox_current_50 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_50.setGeometry(QtCore.QRect(580, 145, 100, 30))
        #
        self.textbox_current_50_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_50_reference.setGeometry(QtCore.QRect(680, 145, 100, 30))
        #
        self.label_current_100 = QLabel("100",self.tab1)
        self.label_current_100.setGeometry(QtCore.QRect(380, 175, 100, 30))
        self.textbox_voltage_100 = QtWidgets.QTextEdit(self.tab1)
        self.textbox_voltage_100.setGeometry(QtCore.QRect(480, 175, 100, 30))
        #
        self.textbox_current_100 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_100.setGeometry(QtCore.QRect(580, 175, 100, 30))
        #
        self.textbox_current_100_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_100_reference.setGeometry(QtCore.QRect(680, 175, 100, 30))
        #
        self.label_current_150 = QLabel("150",self.tab1)
        self.label_current_150.setGeometry(QtCore.QRect(380, 205, 100, 30))
        self.textbox_voltage_150 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_voltage_150.setGeometry(QtCore.QRect(480, 205, 100, 30))
        #
        self.textbox_current_150 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_150.setGeometry(QtCore.QRect(580, 205, 100, 30))
        #
        self.textbox_current_150_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_150_reference.setGeometry(QtCore.QRect(680, 205, 100, 30))
        #
        self.label_current_200 = QLabel("200",self.tab1)
        self.label_current_200.setGeometry(QtCore.QRect(380, 235, 80, 30))
        self.textbox_voltage_200 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_voltage_200.setGeometry(QtCore.QRect(480, 235, 100, 30))
        #
        self.textbox_current_200 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_200.setGeometry(QtCore.QRect(580, 235, 100, 30))
        #
        self.textbox_current_200_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_200_reference.setGeometry(QtCore.QRect(680, 235, 100, 30))
        #
        self.label_current_250 = QLabel("250",self.tab1)
        self.label_current_250.setGeometry(QtCore.QRect(380, 265, 100, 30))
        self.textbox_voltage_250 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_voltage_250.setGeometry(QtCore.QRect(480, 265, 100, 30))
        #
        self.textbox_current_250 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_250.setGeometry(QtCore.QRect(580, 265, 100, 30))
        #
        self.textbox_current_250_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_250_reference.setGeometry(QtCore.QRect(680, 265, 100, 30))
        #
        self.label_current_300 = QLabel("300",self.tab1)
        self.label_current_300.setGeometry(QtCore.QRect(380, 295, 100, 30))
        self.textbox_voltage_300 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_voltage_300.setGeometry(QtCore.QRect(480, 295, 100, 30))
        #
        self.textbox_current_300 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_300.setGeometry(QtCore.QRect(580, 295, 100, 30))
        #
        self.textbox_current_300_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_300_reference.setGeometry(QtCore.QRect(680, 295, 100, 30))
        #
        self.label_current_350 = QLabel("350",self.tab1)
        self.label_current_350.setGeometry(QtCore.QRect(380, 325, 100, 30))
        self.textbox_voltage_350 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_voltage_350.setGeometry(QtCore.QRect(480, 325, 100, 30))
        #
        self.textbox_current_350 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_350.setGeometry(QtCore.QRect(580, 325, 100, 30))
        #
        self.textbox_current_350_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_350_reference.setGeometry(QtCore.QRect(680, 325, 100, 30))
        #
        self.label_current_400 = QLabel("400",self.tab1)
        self.label_current_400.setGeometry(QtCore.QRect(380, 355, 100, 30))
        self.textbox_voltage_400 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_voltage_400.setGeometry(QtCore.QRect(480, 355, 100, 30))
        #
        self.textbox_current_400 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_400.setGeometry(QtCore.QRect(580, 355, 100, 30))
        #
        self.textbox_current_400_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_400_reference.setGeometry(QtCore.QRect(680, 355, 100, 30))
        #
        self.label_current_450 = QLabel("450",self.tab1)
        self.label_current_450.setGeometry(QtCore.QRect(380, 385, 100, 30))
        self.textbox_voltage_450 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_voltage_450.setGeometry(QtCore.QRect(480, 385, 100, 30))
        #
        self.textbox_current_450 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_450.setGeometry(QtCore.QRect(580, 385, 100, 30))
        #
        self.textbox_current_450_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_450_reference.setGeometry(QtCore.QRect(680, 385, 100, 30))
        #
        self.label_current_500 = QLabel("500",self.tab1)
        self.label_current_500.setGeometry(QtCore.QRect(380, 415, 100, 30))
        self.textbox_voltage_500 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_voltage_500.setGeometry(QtCore.QRect(480, 415, 100, 30))
        #
        self.textbox_current_500 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_500.setGeometry(QtCore.QRect(580, 415, 100, 30))
        #
        self.textbox_current_500_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_500_reference.setGeometry(QtCore.QRect(680, 415, 100, 30))
        #
        self.label_current_550 = QLabel("550",self.tab1)
        self.label_current_550.setGeometry(QtCore.QRect(380, 445, 100, 30))
        self.textbox_voltage_550 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_voltage_550.setGeometry(QtCore.QRect(480, 445, 100, 30))
        #
        self.textbox_current_550 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_550.setGeometry(QtCore.QRect(580, 445, 100, 30))
        #
        self.textbox_current_550_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_550_reference.setGeometry(QtCore.QRect(680, 445, 100, 30))
        #
        self.label_current_600 = QLabel("600",self.tab1)
        self.label_current_600.setGeometry(QtCore.QRect(380, 475, 100, 30))
        self.textbox_voltage_600 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_voltage_600.setGeometry(QtCore.QRect(480, 475, 100, 30))
        #
        self.textbox_current_600 = QtWidgets.QLineEdit(self.tab1)
        self.textbox_current_600.setGeometry(QtCore.QRect(580, 475, 100, 30))
        #
        self.textbox_current_600_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_current_600_reference.setGeometry(QtCore.QRect(680, 475, 100, 30))
        self.plot_central = Canvas_tab2(width=8, height=20, dpi=100, parent=self.tab1) 
        self.plot_central.setGeometry(QtCore.QRect(800, 10, 450, 600))
        #self.toolbar_tab2 = NavigationToolbar(self.sc3, self.tab2)
        #self.toolbar_tab2.setGeometry(QtCore.QRect(250, 790, 1200, 30))
        #
        self.label_beam_performance = QLabel("Beam Performance:",self.tab1)
        self.label_beam_performance.setGeometry(QtCore.QRect(30, 210, 150, 30))
        self.label_beam_performance = QLabel("Current",self.tab1)
        self.label_beam_performance.setGeometry(QtCore.QRect(220, 210, 70, 30))
        self.label_beam_performance = QLabel("Reference",self.tab1)
        self.label_beam_performance.setGeometry(QtCore.QRect(290, 210, 70, 30))
        #
        self.label_dee_voltage = QLabel("Dee Voltage",self.tab1)
        self.label_dee_voltage.setGeometry(QtCore.QRect(30, 235, 200, 30))
        self.textbox_beam_dee_voltage = QtWidgets.QLineEdit(self.tab1)
        self.textbox_beam_dee_voltage.setGeometry(QtCore.QRect(220, 235, 70, 30))
        self.textbox_beam_dee_voltage_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_beam_dee_voltage_reference.setGeometry(QtCore.QRect(290, 235, 70, 30))
        #
        self.label_magnet_i = QLabel("Magnet Current",self.tab1)
        self.label_magnet_i.setGeometry(QtCore.QRect(30, 265, 100, 30))
        self.textbox_magnet_i = QtWidgets.QLineEdit(self.tab1)
        self.textbox_magnet_i.setGeometry(QtCore.QRect(220, 265, 70, 30))
        self.textbox_magnet_i_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_magnet_i_reference.setGeometry(QtCore.QRect(290, 265, 70, 30))
        #
        self.label_gas_flow = QLabel("Gas flow",self.tab1)
        self.label_gas_flow.setGeometry(QtCore.QRect(30, 295, 100, 30))
        self.textbox_gas_flow = QtWidgets.QLineEdit(self.tab1)
        self.textbox_gas_flow.setGeometry(QtCore.QRect(220, 295, 70, 30))
        self.textbox_gas_flow_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_gas_flow_reference.setGeometry(QtCore.QRect(290, 295, 70, 30))
        #
        self.label_vacuum = QLabel("Vacuum",self.tab1)
        self.label_vacuum.setGeometry(QtCore.QRect(30, 325, 100, 30))
        self.textbox_vacuum = QtWidgets.QLineEdit(self.tab1)
        self.textbox_vacuum.setGeometry(QtCore.QRect(220, 325, 70, 30))
        self.textbox_vacuum_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_vacuum_reference.setGeometry(QtCore.QRect(290, 325, 70, 30))
        # 
        self.label_i_probe = QLabel("I ion source [uA]",self.tab1)
        self.label_i_probe.setGeometry(QtCore.QRect(30, 355, 100, 30))
        self.textbox_i_ion_source = QtWidgets.QLineEdit(self.tab1)
        self.textbox_i_ion_source.setGeometry(QtCore.QRect(220, 355, 70, 30))
        self.textbox_i_ion_source_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_i_ion_source_reference.setGeometry(QtCore.QRect(290, 355, 70, 30))
        # 
        self.label_i_probe = QLabel("I probe [uA]",self.tab1)
        self.label_i_probe.setGeometry(QtCore.QRect(30, 385, 100, 30))
        self.textbox_i_probe = QtWidgets.QLineEdit(self.tab1)
        self.textbox_i_probe.setGeometry(QtCore.QRect(220, 385, 70, 30))
        self.textbox_i_probe_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_i_probe_reference.setGeometry(QtCore.QRect(290, 385, 70, 30))
        #
        self.label_i_foil = QLabel("I foil [uA]",self.tab1)
        self.label_i_foil .setGeometry(QtCore.QRect(30, 415, 100, 30))
        self.textbox_i_foil  = QtWidgets.QLineEdit(self.tab1)
        self.textbox_i_foil .setGeometry(QtCore.QRect(220, 415, 70, 30))
        self.textbox_i_foil_reference  = QtWidgets.QTextEdit(self.tab1)
        self.textbox_i_foil_reference .setGeometry(QtCore.QRect(290, 415, 70, 30))
        #
        self.label_i_target = QLabel("I target [uA]",self.tab1)
        self.label_i_target .setGeometry(QtCore.QRect(30, 445, 100, 30))
        self.textbox_i_target  = QtWidgets.QLineEdit(self.tab1)
        self.textbox_i_target .setGeometry(QtCore.QRect(220, 445, 70, 30))
        self.textbox_i_target_reference  = QtWidgets.QTextEdit(self.tab1)
        self.textbox_i_target_reference .setGeometry(QtCore.QRect(290, 445, 70, 30))
        #
        self.label_i_coll_low = QLabel("I coll low [uA]",self.tab1)
        self.label_i_coll_low.setGeometry(QtCore.QRect(30, 475, 100, 30))
        self.textbox_i_coll_low = QtWidgets.QLineEdit(self.tab1)
        self.textbox_i_coll_low.setGeometry(QtCore.QRect(220, 475, 70, 30))
        self.textbox_i_coll_low_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_i_coll_low_reference.setGeometry(QtCore.QRect(290, 475, 70, 30))
        #
        self.label_i_coll_up = QLabel("I coll up [uA]",self.tab1)
        self.label_i_coll_up.setGeometry(QtCore.QRect(30, 505, 100, 30))
        self.textbox_i_coll_up = QtWidgets.QLineEdit(self.tab1)
        self.textbox_i_coll_up.setGeometry(QtCore.QRect(220, 505, 70, 30))
        self.textbox_i_coll_up_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_i_coll_up_reference.setGeometry(QtCore.QRect(290, 505, 70, 30))
        #
        self.label_probe_source = QLabel("I probe/I ion source [uA/mA]",self.tab1)
        self.label_probe_source.setGeometry(QtCore.QRect(30, 535, 200, 30))
        self.textbox_probe_source = QtWidgets.QTextEdit(self.tab1)
        self.textbox_probe_source.setGeometry(QtCore.QRect(220, 535,70, 30))
        self.textbox_probe_source_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_probe_source_reference.setGeometry(QtCore.QRect(290, 535, 70, 30))
        #
        self.label_foil_probe = QLabel("I foil/I probe [uA/uA]",self.tab1)
        self.label_foil_probe.setGeometry(QtCore.QRect(30, 565, 200, 30))
        self.textbox_foil_probe = QtWidgets.QTextEdit(self.tab1)
        self.textbox_foil_probe.setGeometry(QtCore.QRect(220, 565, 70, 30))
        self.textbox_foil_probe_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_foil_probe_reference.setGeometry(QtCore.QRect(290, 565, 70, 30))
        #
        self.label_target_probe = QLabel("I target/I probe [uA/uA]",self.tab1)
        self.label_target_probe.setGeometry(QtCore.QRect(30,595, 200, 30))
        self.textbox_target_probe = QtWidgets.QTextEdit(self.tab1)
        self.textbox_target_probe.setGeometry(QtCore.QRect(220,595, 70, 30))
        self.textbox_target_probe_reference = QtWidgets.QTextEdit(self.tab1)
        self.textbox_target_probe_reference.setGeometry(QtCore.QRect(290, 595, 70, 30))
        #
        
        #pixmap = pixmap.scaled(350, 350, QtCore.Qt.KeepAspectRatio)
        #pixmap_rf = QPixmap('rf_position.png')
        #pixmap_rf = pixmap_rf.scaled(350, 350, QtCore.Qt.KeepAspectRatio)
        #self.label_ion_source.setPixmap(pixmap)
        #self.label_rf_position.setPixmap(pixmap_rf)
        #self.label_ion_source.setGeometry(QtCore.QRect(50, 150,pixmap.width(), pixmap.height()))
        #self.label_rf_position.setGeometry(QtCore.QRect(50, 550,pixmap.width(), pixmap.height()))
        #self.resize(pixmap.width(), pixmap.height())

 

        self.compute_current_ratios = QPushButton('Compute current ratios', self.tab1)
        self.compute_current_ratios.setGeometry(QtCore.QRect(400, 520, 200, 30))
        self.compute_current_ratios.clicked.connect(self.on_click_ratio_computation)
        
        self.compute_current_ratios = QPushButton('Compute current ratios (reference)', self.tab1)
        self.compute_current_ratios.setGeometry(QtCore.QRect(400, 550, 250, 30))
        self.compute_current_ratios.clicked.connect(self.on_click_ratio_computation_reference)

        # TAB 2
        
        self.label_cyclotron = QLabel("Location",self.tab2)
        self.label_cyclotron.setGeometry(QtCore.QRect(30, 5, 100, 30))
        self.textbox_cyclotron_rf = QtWidgets.QLineEdit(self.tab2)
        self.textbox_cyclotron_rf.setGeometry(QtCore.QRect(90, 5, 100, 30))

        self.label_cyclotron_rf = QLabel("Date (YYYY/MM/DD)",self.tab2)
        self.label_cyclotron_rf.setGeometry(QtCore.QRect(220, 5,125, 30))
        self.textbox_date_rf = QtWidgets.QLineEdit(self.tab2)
        self.textbox_date_rf.setGeometry(QtCore.QRect(360, 5, 100, 30))


        self.label_dee1h = QLabel("Dee 1 Height [mm]:",self.tab2)
        self.label_dee1h.setGeometry(QtCore.QRect(30, 40, 150, 30))
        #
        self.label_dee1h_before = QLabel("Before",self.tab2)
        self.label_dee1h_before.setGeometry(QtCore.QRect(60, 65, 150, 30))
        #
        self.label_dee1h_after = QLabel("After",self.tab2)
        self.label_dee1h_after.setGeometry(QtCore.QRect(160, 65, 150, 30))
        #
        self.label_dee1h_reference = QLabel("Reference",self.tab2)
        self.label_dee1h_reference.setGeometry(QtCore.QRect(260, 65, 150, 30))
        #
        self.label_dee1h_a = QLabel("(A):",self.tab2)
        self.label_dee1h_a.setGeometry(QtCore.QRect(30, 95, 80, 30))
        self.textbox_dee1h_a_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1h_a_before.setGeometry(QtCore.QRect(60, 95, 100, 30))
        #
        self.textbox_dee1h_a_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1h_a_after.setGeometry(QtCore.QRect(160, 95, 100, 30))
        #
        self.textbox_dee1h_a_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee1h_a_reference.setGeometry(QtCore.QRect(260, 95, 100, 30))
        #
        self.label_dee1h_b = QLabel("(B):",self.tab2)
        self.label_dee1h_b.setGeometry(QtCore.QRect(30, 125, 100, 30))
        self.textbox_dee1h_b_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1h_b_before.setGeometry(QtCore.QRect(60, 125, 100, 30))
        #
        self.textbox_dee1h_b_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1h_b_after.setGeometry(QtCore.QRect(160, 125, 100, 30))
        #
        self.textbox_dee1h_b_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee1h_b_reference.setGeometry(QtCore.QRect(260, 125, 100, 30))
        #
        self.label_dee1h_c = QLabel("(C):",self.tab2)
        self.label_dee1h_c.setGeometry(QtCore.QRect(30, 155, 100, 30))
        self.textbox_dee1h_c_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1h_c_before.setGeometry(QtCore.QRect(60, 155, 100, 30))
        #
        self.textbox_dee1h_c_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1h_c_after.setGeometry(QtCore.QRect(160, 155, 100, 30))
        #
        self.textbox_dee1h_c_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee1h_c_reference.setGeometry(QtCore.QRect(260, 155, 100, 30))
        #
        self.label_dee1h_d = QLabel("(D):",self.tab2)
        self.label_dee1h_d.setGeometry(QtCore.QRect(30, 185, 100, 30))
        self.textbox_dee1h_d_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1h_d_before.setGeometry(QtCore.QRect(60, 185, 100, 30))
        #
        self.textbox_dee1h_d_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1h_d_after.setGeometry(QtCore.QRect(160, 185, 100, 30))
        #
        self.textbox_dee1h_d_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee1h_d_reference.setGeometry(QtCore.QRect(260, 185, 100, 30))
        #
        self.label_dee2h = QLabel("Dee 2 Height [mm]:",self.tab2)
        self.label_dee2h.setGeometry(QtCore.QRect(380, 40, 150, 30))
        #
        self.label_dee2h_before = QLabel("Before",self.tab2)
        self.label_dee2h_before.setGeometry(QtCore.QRect(410, 65, 150, 30))
        #
        self.label_dee2h_after = QLabel("After",self.tab2)
        self.label_dee2h_after.setGeometry(QtCore.QRect(510, 65, 150, 30))
        #
        self.label_dee2h_reference = QLabel("Reference",self.tab2)
        self.label_dee2h_reference.setGeometry(QtCore.QRect(610, 65, 150, 30))
        #
        self.label_dee2h_e = QLabel("(E):",self.tab2)
        self.label_dee2h_e.setGeometry(QtCore.QRect(380, 95, 80, 30))
        self.textbox_dee2h_e_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2h_e_before.setGeometry(QtCore.QRect(410, 95, 100, 30))
        #
        self.textbox_dee2h_e_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2h_e_after.setGeometry(QtCore.QRect(510, 95, 100, 30))
        #
        self.textbox_dee2h_e_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee2h_e_reference.setGeometry(QtCore.QRect(610, 95, 100, 30))
        #
        self.label_dee2h_f = QLabel("(F):",self.tab2)
        self.label_dee2h_f.setGeometry(QtCore.QRect(380, 125, 100, 30))
        self.textbox_dee2h_f_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2h_f_before.setGeometry(QtCore.QRect(410, 125, 100, 30))
        #
        self.textbox_dee2h_f_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2h_f_after.setGeometry(QtCore.QRect(510, 125, 100, 30))
        #
        self.textbox_dee2h_f_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee2h_f_reference.setGeometry(QtCore.QRect(610, 125, 100, 30))
        #
        self.label_dee2h_g = QLabel("(G):",self.tab2)
        self.label_dee2h_g.setGeometry(QtCore.QRect(380, 155, 100, 30))
        self.textbox_dee2h_g_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2h_g_before.setGeometry(QtCore.QRect(410, 155, 100, 30))
        #
        self.textbox_dee2h_g_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2h_g_after.setGeometry(QtCore.QRect(510, 155, 100, 30))
        #
        self.textbox_dee2h_g_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee2h_g_reference.setGeometry(QtCore.QRect(610, 155, 100, 30))
        #
        self.label_dee2h_h = QLabel("(H):",self.tab2)
        self.label_dee2h_h.setGeometry(QtCore.QRect(380, 185, 100, 30))
        self.textbox_dee2h_h_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2h_h_before.setGeometry(QtCore.QRect(410, 185, 100, 30))
        #
        self.textbox_dee2h_h_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2h_h_after.setGeometry(QtCore.QRect(510, 185, 100, 30))
        #
        self.textbox_dee2h_h_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee2h_h_reference.setGeometry(QtCore.QRect(610, 185, 100, 30))

        # DEE 2

        self.label_dee1 = QLabel("Dee 1 Thickness (mm): ",self.tab2)
        self.label_dee1.setGeometry(QtCore.QRect(30, 220, 150, 30))
        #
        self.label_dee1_before = QLabel("Before",self.tab2)
        self.label_dee1_before.setGeometry(QtCore.QRect(60, 245, 150, 30))
        #
        self.label_dee1_after = QLabel("After",self.tab2)
        self.label_dee1_after.setGeometry(QtCore.QRect(160, 245, 150, 30))
        #
        self.label_dee1_reference = QLabel("Reference",self.tab2)
        self.label_dee1_reference.setGeometry(QtCore.QRect(260, 245, 150, 30))
        #
        self.label_dee1_a = QLabel("(A):",self.tab2)
        self.label_dee1_a.setGeometry(QtCore.QRect(30, 275, 80, 30))
        self.textbox_dee1_a_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1_a_before.setGeometry(QtCore.QRect(60, 275, 100, 30))
        #
        self.textbox_dee1_a_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1_a_after.setGeometry(QtCore.QRect(160, 275, 100, 30))
        #
        self.textbox_dee1_a_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee1_a_reference.setGeometry(QtCore.QRect(260, 275, 100, 30))
        #
        self.label_dee1_b = QLabel("(B):",self.tab2)
        self.label_dee1_b.setGeometry(QtCore.QRect(30, 305, 100, 30))
        self.textbox_dee1_b_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1_b_before.setGeometry(QtCore.QRect(60, 305, 100, 30))
        #
        self.textbox_dee1_b_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1_b_after.setGeometry(QtCore.QRect(160, 305, 100, 30))
        #
        self.textbox_dee1_b_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee1_b_reference.setGeometry(QtCore.QRect(260, 305, 100, 30))
        #
        self.label_dee1_c = QLabel("(C):",self.tab2)
        self.label_dee1_c.setGeometry(QtCore.QRect(30, 335, 100, 30))
        self.textbox_dee1_c_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1_c_before.setGeometry(QtCore.QRect(60, 335, 100, 30))
        #
        self.textbox_dee1_c_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1_c_after.setGeometry(QtCore.QRect(160, 335, 100, 30))
        #
        self.textbox_dee1_c_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee1_c_reference.setGeometry(QtCore.QRect(260, 335, 100, 30))
        #
        self.label_dee1_d = QLabel("(D):",self.tab2)
        self.label_dee1_d.setGeometry(QtCore.QRect(30, 365, 100, 30))
        self.textbox_dee1_d_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1_d_before.setGeometry(QtCore.QRect(60, 365, 100, 30))
        #
        self.textbox_dee1_d_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee1_d_after.setGeometry(QtCore.QRect(160, 365, 100, 30))
        #
        self.textbox_dee1_d_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee1_d_reference.setGeometry(QtCore.QRect(260, 365, 100, 30))

        self.label_dee2 = QLabel("Dee 2 Thickness (mm):",self.tab2)
        self.label_dee2.setGeometry(QtCore.QRect(380, 220, 150, 30))
        #
        self.label_dee2_before = QLabel("Before",self.tab2)
        self.label_dee2_before.setGeometry(QtCore.QRect(410, 245, 150, 30))
        #
        self.label_dee2_after = QLabel("After",self.tab2)
        self.label_dee2_after.setGeometry(QtCore.QRect(510, 245, 150, 30))
        #
        self.label_dee2_reference = QLabel("Reference",self.tab2)
        self.label_dee2_reference.setGeometry(QtCore.QRect(610, 245, 150, 30))
        #
        self.label_dee2_e_before = QLabel("(E):",self.tab2)
        self.label_dee2_e_before.setGeometry(QtCore.QRect(380, 275, 80, 30))
        self.textbox_dee2_e_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2_e_before.setGeometry(QtCore.QRect(410, 275, 100, 30))
        #
        self.textbox_dee2_e_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2_e_after.setGeometry(QtCore.QRect(510, 275, 100, 30))
        #
        self.textbox_dee2_e_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee2_e_reference.setGeometry(QtCore.QRect(610, 275, 100, 30))
        #
        self.label_dee2_f = QLabel("(F):",self.tab2)
        self.label_dee2_f.setGeometry(QtCore.QRect(380, 305, 100, 30))
        self.textbox_dee2_f_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2_f_before.setGeometry(QtCore.QRect(410, 305, 100, 30))
        #
        self.textbox_dee2_f_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2_f_after.setGeometry(QtCore.QRect(510, 305, 100, 30))
        #
        self.textbox_dee2_f_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee2_f_reference.setGeometry(QtCore.QRect(610, 305, 100, 30))
        #
        self.label_dee2_g = QLabel("(G):",self.tab2)
        self.label_dee2_g.setGeometry(QtCore.QRect(380, 335, 100, 30))
        self.textbox_dee2_g_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2_g_before.setGeometry(QtCore.QRect(410, 335, 100, 30))
        #
        self.textbox_dee2_g_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2_g_after.setGeometry(QtCore.QRect(510, 335, 100, 30))
        #
        self.textbox_dee2_g_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee2_g_reference.setGeometry(QtCore.QRect(610, 335, 100, 30))
        #
        self.label_dee2_h = QLabel("(H):",self.tab2)
        self.label_dee2_h.setGeometry(QtCore.QRect(380, 365, 100, 30))
        self.textbox_dee2_h_before = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2_h_before.setGeometry(QtCore.QRect(410, 365, 100, 30))
        #
        self.textbox_dee2_h_after = QtWidgets.QLineEdit(self.tab2)
        self.textbox_dee2_h_after.setGeometry(QtCore.QRect(510, 365, 100, 30))
        #
        self.textbox_dee2_h_reference = QtWidgets.QTextEdit(self.tab2)
        self.textbox_dee2_h_reference.setGeometry(QtCore.QRect(610, 365, 100, 30))

        # MIDPLANE 

        self.label_midplane = QLabel("Midplane from pole (mm):",self.tab2)
        self.label_midplane.setGeometry(QtCore.QRect(30, 405, 160, 30))

        self.label_midplane = QtWidgets.QPushButton("Compute Midplane from pole (mm)",self.tab2)
        self.label_midplane.setGeometry(QtCore.QRect(210, 405, 350, 30))
   
        self.label_midplane_ref = QtWidgets.QPushButton("Compute Midplane from pole (Reference) (mm)",self.tab2)
        self.label_midplane_ref.setGeometry(QtCore.QRect(210, 435, 350, 30))

        self.label_midplane.clicked.connect(self.compute_mid_plane_dee1)
        self.label_midplane.clicked.connect(self.compute_mid_plane_dee2)
        self.label_midplane_ref.clicked.connect(self.compute_mid_plane_dee1_ref)
        self.label_midplane_ref.clicked.connect(self.compute_mid_plane_dee2_ref)
        #
        self.label_midplane_a = QLabel("A",self.tab2)
        self.label_midplane_a.setGeometry(QtCore.QRect(190, 465, 50, 30))
        #
        self.label_midplane_b = QLabel("B",self.tab2)
        self.label_midplane_b.setGeometry(QtCore.QRect(240, 465, 50, 30))
        #
        self.label_midplane_c = QLabel("C",self.tab2)
        self.label_midplane_c.setGeometry(QtCore.QRect(290, 465, 50, 30))
        #
        self.label_midplane_d = QLabel("D",self.tab2)
        self.label_midplane_d.setGeometry(QtCore.QRect(340, 465, 50, 30))
        #
        self.label_midplane_e = QLabel("E",self.tab2)
        self.label_midplane_e.setGeometry(QtCore.QRect(390, 465, 50, 30))
        #
        self.label_midplane_f = QLabel("F",self.tab2)
        self.label_midplane_f.setGeometry(QtCore.QRect(440, 465, 50, 30))
        #
        self.label_midplane_g = QLabel("G",self.tab2)
        self.label_midplane_g.setGeometry(QtCore.QRect(490, 465, 50, 30))
        #
        self.label_midplane_h = QLabel("H",self.tab2)
        self.label_midplane_h.setGeometry(QtCore.QRect(540, 465, 50, 30))
        #
        self.label_midplane_theorical = QLabel("Theorical [mm]",self.tab2)
        self.label_midplane_theorical.setGeometry(QtCore.QRect(30, 495, 90, 30))
        self.textbox_midplane_theorical_a = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_theorical_a.setGeometry(QtCore.QRect(190, 495, 50, 30))
        self.textbox_midplane_theorical_a.setPlainText("30")
        #
        self.textbox_midplane_theorical_b = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_theorical_b.setGeometry(QtCore.QRect(240, 495, 50, 30))
        self.textbox_midplane_theorical_b.setPlainText("58")
        #
        self.textbox_midplane_theorical_c = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_theorical_c.setGeometry(QtCore.QRect(290, 495, 50, 30))
        self.textbox_midplane_theorical_c.setPlainText("30")
        #
        self.textbox_midplane_theorical_d = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_theorical_d.setGeometry(QtCore.QRect(340, 495, 50, 30))
        self.textbox_midplane_theorical_d.setPlainText("30")
        #
        self.textbox_midplane_theorical_e = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_theorical_e.setGeometry(QtCore.QRect(390, 495, 50, 30))
        self.textbox_midplane_theorical_e.setPlainText("58")
        #
        self.textbox_midplane_theorical_f = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_theorical_f.setGeometry(QtCore.QRect(440, 495, 50, 30))
        self.textbox_midplane_theorical_f.setPlainText("30")
        #
        self.textbox_midplane_theorical_g = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_theorical_g.setGeometry(QtCore.QRect(490, 495, 50, 30))
        self.textbox_midplane_theorical_g.setPlainText("58")
        #
        self.textbox_midplane_theorical_h = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_theorical_h.setGeometry(QtCore.QRect(540, 495, 50, 30))
        self.textbox_midplane_theorical_h.setPlainText("58")
        #
        self.label_midplane_actual = QLabel("Actual [mm]",self.tab2)
        self.label_midplane_actual.setGeometry(QtCore.QRect(30, 525, 80, 30))
        self.textbox_midplane_actual_a = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_actual_a.setGeometry(QtCore.QRect(190, 525, 50, 30))
        #
        self.textbox_midplane_actual_b = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_actual_b.setGeometry(QtCore.QRect(240, 525, 50, 30))
        #
        self.textbox_midplane_actual_c = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_actual_c.setGeometry(QtCore.QRect(290, 525, 50, 30))
        #
        self.textbox_midplane_actual_d = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_actual_d.setGeometry(QtCore.QRect(340, 525, 50, 30))
        #
        self.textbox_midplane_actual_e = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_actual_e.setGeometry(QtCore.QRect(390, 525, 50, 30))
        #
        self.textbox_midplane_actual_f = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_actual_f.setGeometry(QtCore.QRect(440, 525, 50, 30))
        #
        self.textbox_midplane_actual_g = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_actual_g.setGeometry(QtCore.QRect(490, 525, 50, 30))
        #
        self.textbox_midplane_actual_h = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_actual_h.setGeometry(QtCore.QRect(540, 525, 50, 30))
        #
        self.label_midplane_variance = QLabel("Variance [mm]",self.tab2)
        self.label_midplane_variance.setGeometry(QtCore.QRect(30, 555, 90, 30))
        self.textbox_midplane_variance_a = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_variance_a.setGeometry(QtCore.QRect(190, 555, 50, 30))
        #
        self.textbox_midplane_variance_b = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_variance_b.setGeometry(QtCore.QRect(240, 555, 50, 30))
        #
        self.textbox_midplane_variance_c = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_variance_c.setGeometry(QtCore.QRect(290, 555, 50, 30))
        #
        self.textbox_midplane_variance_d = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_variance_d.setGeometry(QtCore.QRect(340, 555, 50, 30))
        #
        self.textbox_midplane_variance_e = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_variance_e.setGeometry(QtCore.QRect(390, 555, 50, 30))
        #
        self.textbox_midplane_variance_f = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_variance_f.setGeometry(QtCore.QRect(440, 555, 50, 30))
        #
        self.textbox_midplane_variance_g = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_variance_g.setGeometry(QtCore.QRect(490, 555, 50, 30))
        #
        self.textbox_midplane_variance_h = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_variance_h.setGeometry(QtCore.QRect(540, 555, 50, 30))

        self.label_midplane_reference = QLabel("Actual Reference [mm]",self.tab2)
        self.label_midplane_reference.setGeometry(QtCore.QRect(30, 585, 160, 30))
        self.textbox_midplane_reference_a = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_reference_a.setGeometry(QtCore.QRect(190, 585, 50, 30))
        #
        self.textbox_midplane_reference_b = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_reference_b.setGeometry(QtCore.QRect(240, 585, 50, 30))
        #
        self.textbox_midplane_reference_c = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_reference_c.setGeometry(QtCore.QRect(290, 585, 50, 30))
        #
        self.textbox_midplane_reference_d = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_reference_d.setGeometry(QtCore.QRect(340, 585, 50, 30))
        #
        self.textbox_midplane_reference_e = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_reference_e.setGeometry(QtCore.QRect(390, 585, 50, 30))
        #
        self.textbox_midplane_reference_f = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_reference_f.setGeometry(QtCore.QRect(440, 585, 50, 30))
        #
        self.textbox_midplane_reference_g = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_reference_g.setGeometry(QtCore.QRect(490, 585, 50, 30))
        #
        self.textbox_midplane_reference_h = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_reference_h.setGeometry(QtCore.QRect(540, 585, 50, 30))
        #
        self.label_midplane_vreference = QLabel("Variance Reference [mm]",self.tab2)
        self.label_midplane_vreference.setGeometry(QtCore.QRect(30, 615, 160, 30))
        self.textbox_midplane_vreference_a = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_vreference_a.setGeometry(QtCore.QRect(190, 615, 50, 30))
        #
        self.textbox_midplane_vreference_b = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_vreference_b.setGeometry(QtCore.QRect(240, 615, 50, 30))
        #
        self.textbox_midplane_vreference_c = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_vreference_c.setGeometry(QtCore.QRect(290, 615, 50, 30))
        #
        self.textbox_midplane_vreference_d = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_vreference_d.setGeometry(QtCore.QRect(340, 615, 50, 30))
        #
        self.textbox_midplane_vreference_e = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_vreference_e.setGeometry(QtCore.QRect(390, 615, 50, 30))
        #
        self.textbox_midplane_vreference_f = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_vreference_f.setGeometry(QtCore.QRect(440, 615, 50, 30))
        #
        self.textbox_midplane_vreference_g = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_vreference_g.setGeometry(QtCore.QRect(490, 615, 50, 30))
        #
        self.textbox_midplane_vreference_h = QtWidgets.QTextEdit(self.tab2)
        self.textbox_midplane_vreference_h.setGeometry(QtCore.QRect(540, 615, 50, 30))

        self.plot_rf = Canvas(width=7, height=20, dpi=100, parent=self.tab2) 
        self.plot_rf.setGeometry(QtCore.QRect(730, 10, 530, 600))


        #IMPEDANCES

        self.label_cyclotron = QLabel("Location",self.tab3)
        self.label_cyclotron.setGeometry(QtCore.QRect(30, 5, 100, 30))
        self.textbox_cyclotron_collimators = QtWidgets.QLineEdit(self.tab3)
        self.textbox_cyclotron_collimators.setGeometry(QtCore.QRect(90, 5, 100, 30))

        self.label_cyclotron_impedances = QLabel("Date (YYYY/MM/DD)",self.tab3)
        self.label_cyclotron_impedances.setGeometry(QtCore.QRect(220, 5,125, 30))
        self.textbox_date_collimators = QtWidgets.QLineEdit(self.tab3)
        self.textbox_date_collimators.setGeometry(QtCore.QRect(360, 5, 100, 30))


        self.label_imp = QLabel("Impedances:",self.tab3)
        self.label_imp.setGeometry(QtCore.QRect(30, 40, 150, 30))
        #
        self.label_imp_before = QLabel("Before",self.tab3)
        self.label_imp_before.setGeometry(QtCore.QRect(120, 65, 150, 30))
        #
        self.label_imp_after = QLabel("After",self.tab3)
        self.label_imp_after.setGeometry(QtCore.QRect(220, 65, 150, 30))
        #
        self.label_imp_reference = QLabel("Reference",self.tab3)
        self.label_imp_reference.setGeometry(QtCore.QRect(320, 65, 150, 30))
        #
        #
        self.label_icollimator1_l = QLabel("Collimator 1 L:",self.tab3)
        self.label_icollimator1_l.setGeometry(QtCore.QRect(30, 95, 100, 30))
        self.textbox_icollimator1_l_before = QtWidgets.QLineEdit(self.tab3)
        self.textbox_icollimator1_l_before.setGeometry(QtCore.QRect(120, 95, 100, 30))
        #
        self.textbox_icollimator1_l_after = QtWidgets.QLineEdit(self.tab3)
        self.textbox_icollimator1_l_after.setGeometry(QtCore.QRect(220, 95, 100, 30))
        #
        self.textbox_icollimator1_l_reference = QtWidgets.QTextEdit(self.tab3)
        self.textbox_icollimator1_l_reference.setGeometry(QtCore.QRect(320, 95, 100, 30))
        #
        self.label_icollimator1_u = QLabel("Collimator 1 U:",self.tab3)
        self.label_icollimator1_u.setGeometry(QtCore.QRect(30, 125, 100, 30))
        self.textbox_icollimator1_u_before = QtWidgets.QLineEdit(self.tab3)
        self.textbox_icollimator1_u_before.setGeometry(QtCore.QRect(120, 125, 100, 30))
        #
        self.textbox_icollimator1_u_after = QtWidgets.QLineEdit(self.tab3)
        self.textbox_icollimator1_u_after.setGeometry(QtCore.QRect(220, 125, 100, 30))
        #
        self.textbox_icollimator1_u_reference = QtWidgets.QTextEdit(self.tab3)
        self.textbox_icollimator1_u_reference.setGeometry(QtCore.QRect(320, 125, 100, 30))
        #
        self.label_icollimator2_l = QLabel("Collimator 2 L:",self.tab3)
        self.label_icollimator2_l.setGeometry(QtCore.QRect(30, 155, 100, 30))
        self.textbox_icollimator2_l_before = QtWidgets.QLineEdit(self.tab3)
        self.textbox_icollimator2_l_before.setGeometry(QtCore.QRect(120, 155, 100, 30))
        #
        self.textbox_icollimator2_l_after = QtWidgets.QLineEdit(self.tab3)
        self.textbox_icollimator2_l_after.setGeometry(QtCore.QRect(220, 155, 100, 30))
        #
        self.textbox_icollimator2_l_reference = QtWidgets.QTextEdit(self.tab3)
        self.textbox_icollimator2_l_reference.setGeometry(QtCore.QRect(320, 155, 100, 30))
        #
        self.label_icollimator2_u = QLabel("Collimator 2 U:",self.tab3)
        self.label_icollimator2_u.setGeometry(QtCore.QRect(30, 185, 100, 30))
        self.textbox_icollimator2_u_before = QtWidgets.QLineEdit(self.tab3)
        self.textbox_icollimator2_u_before.setGeometry(QtCore.QRect(120, 185, 100, 30))
        #
        self.textbox_icollimator2_u_after = QtWidgets.QLineEdit(self.tab3)
        self.textbox_icollimator2_u_after.setGeometry(QtCore.QRect(220, 185, 100, 30))
        #
        self.textbox_icollimator2_u_reference = QtWidgets.QTextEdit(self.tab3)
        self.textbox_icollimator2_u_reference.setGeometry(QtCore.QRect(320, 185, 100, 30))
        #

        # COLLIMATORS APERTURE AND SEPARATION
        self.label_centralregion = QLabel("Collimators Settings:",self.tab3)
        self.label_centralregion.setGeometry(QtCore.QRect(30, 245, 150, 30))
        #
        self.label_collimator_before = QLabel("Before",self.tab3)
        self.label_collimator_before.setGeometry(QtCore.QRect(120, 275, 100, 30))
        #
        self.label_collimator_after = QLabel("After",self.tab3)
        self.label_collimator_after.setGeometry(QtCore.QRect(220, 275, 100, 30))
        #
        self.label_collimator_reference = QLabel("Reference",self.tab3)
        self.label_collimator_reference.setGeometry(QtCore.QRect(320, 275, 100, 30))
        #
        self.label_coll1_aperture = QLabel("Aperture 1:",self.tab3)
        self.label_coll1_aperture.setGeometry(QtCore.QRect(30, 305, 75, 30))
        self.textbox_coll1_aperture_before = QtWidgets.QLineEdit(self.tab3)
        self.textbox_coll1_aperture_before.setGeometry(QtCore.QRect(120, 305, 100, 30))
        #
        self.textbox_coll1_aperture_after = QtWidgets.QLineEdit(self.tab3)
        self.textbox_coll1_aperture_after.setGeometry(QtCore.QRect(220, 305, 100, 30))
        #
        self.textbox_coll1_aperture_reference = QtWidgets.QTextEdit(self.tab3)
        self.textbox_coll1_aperture_reference.setGeometry(QtCore.QRect(320, 305, 100, 30))
        #
        self.label_coll1_separation = QLabel("Separation 1:",self.tab3)
        self.label_coll1_separation.setGeometry(QtCore.QRect(30, 335, 95, 30))
        self.textbox_coll1_separation_before = QtWidgets.QLineEdit(self.tab3)
        self.textbox_coll1_separation_before.setGeometry(QtCore.QRect(120, 335, 100, 30))
        #
        self.textbox_coll1_separation_after = QtWidgets.QLineEdit(self.tab3)
        self.textbox_coll1_separation_after.setGeometry(QtCore.QRect(220, 335, 100, 30))
        #
        self.textbox_coll1_separation_reference = QtWidgets.QTextEdit(self.tab3)
        self.textbox_coll1_separation_reference.setGeometry(QtCore.QRect(320, 335, 100, 30))
        #
        self.label_coll2_aperture = QLabel("Aperture 2:",self.tab3)
        self.label_coll2_aperture.setGeometry(QtCore.QRect(30, 365, 95, 30))
        self.textbox_coll2_aperture_before = QtWidgets.QLineEdit(self.tab3)
        self.textbox_coll2_aperture_before.setGeometry(QtCore.QRect(120, 365, 100, 30))
        #
        self.textbox_coll2_aperture_after = QtWidgets.QLineEdit(self.tab3)
        self.textbox_coll2_aperture_after.setGeometry(QtCore.QRect(220, 365, 100, 30))
        #
        self.textbox_coll2_aperture_reference = QtWidgets.QTextEdit(self.tab3)
        self.textbox_coll2_aperture_reference.setGeometry(QtCore.QRect(320, 365, 100, 30))
        #
        self.label_coll2_separation = QLabel("Separation 2:",self.tab3)
        self.label_coll2_separation.setGeometry(QtCore.QRect(30, 395, 95, 30))
        self.textbox_coll2_separation_before = QtWidgets.QLineEdit(self.tab3)
        self.textbox_coll2_separation_before.setGeometry(QtCore.QRect(120, 395, 100, 30))
        #
        self.textbox_coll2_separation_after = QtWidgets.QLineEdit(self.tab3)
        self.textbox_coll2_separation_after.setGeometry(QtCore.QRect(220, 395, 100, 30))
        #
        self.textbox_coll2_separation_reference = QtWidgets.QTextEdit(self.tab3)
        self.textbox_coll2_separation_reference.setGeometry(QtCore.QRect(320, 395, 100, 30))
        ###
        self.label_centralregion = QLabel("Collimators Settings:",self.tab3)
        self.label_centralregion.setGeometry(QtCore.QRect(30, 445, 150, 30))
        #
        self.label_flap_before = QLabel("0%",self.tab3)
        self.label_flap_before.setGeometry(QtCore.QRect(150, 475, 100, 30))
        #
        self.label_flap_after = QLabel("50%",self.tab3)
        self.label_flap_after.setGeometry(QtCore.QRect(270, 475, 100, 30))
        #
        self.label_flap_reference = QLabel("100%",self.tab3)
        self.label_flap_reference.setGeometry(QtCore.QRect(370, 475, 100, 30))
        #
        self.label_flap1_position_0 = QLabel("Flap 1 (position):",self.tab3)
        self.label_flap1_position_0.setGeometry(QtCore.QRect(30, 505, 125, 30))
        self.textbox_flap1_position_0 = QtWidgets.QLineEdit(self.tab3)
        self.textbox_flap1_position_0.setGeometry(QtCore.QRect(150, 505, 100, 30))
        #
        self.textbox_flap1_position_50 = QtWidgets.QLineEdit(self.tab3)
        self.textbox_flap1_position_50.setGeometry(QtCore.QRect(250, 505, 100, 30))
        #
        self.textbox_flap1_position_100 = QtWidgets.QTextEdit(self.tab3)
        self.textbox_flap1_position_100.setGeometry(QtCore.QRect(350, 505, 100, 30))
        #
        self.label_flap2_position = QLabel("Flap 2 (position):",self.tab3)
        self.label_flap2_position.setGeometry(QtCore.QRect(30, 535, 125, 30))
        self.textbox_flap2_position_0 = QtWidgets.QLineEdit(self.tab3)
        self.textbox_flap2_position_0.setGeometry(QtCore.QRect(150, 535, 100, 30))
        #
        self.textbox_flap2_position_50 = QtWidgets.QLineEdit(self.tab3)
        self.textbox_flap2_position_50.setGeometry(QtCore.QRect(250, 535, 100, 30))
        #
        self.textbox_flap2_position_100 = QtWidgets.QTextEdit(self.tab3)
        self.textbox_flap2_position_100.setGeometry(QtCore.QRect(350, 535, 100, 30))
    
        #

        self.plot_collimators = Canvas(width=7, height=20, dpi=100, parent=self.tab3) 
        self.plot_collimators.setGeometry(QtCore.QRect(460, 10, 730, 600))

        #pixmap = pixmap.scaled(350, 350, QtCore.Qt.KeepAspectRatio)
        #pixmap_rf = QPixmap('rf_position.png')
        #pixmap_rf = pixmap_rf.scaled(350, 350, QtCore.Qt.KeepAspectRatio)
        #self.label_ion_source.setPixmap(pixmap)


        # CALIBRATION EXTRACTION

        self.label_cyclotron = QLabel("Location",self.tab4)
        self.label_cyclotron.setGeometry(QtCore.QRect(30, 5, 100, 30))
        self.textbox_cyclotron_calibration = QtWidgets.QLineEdit(self.tab4)
        self.textbox_cyclotron_calibration.setGeometry(QtCore.QRect(90, 5, 100, 30))

        self.label_cyclotron_calibration = QLabel("Date (YYYY/MM/DD)",self.tab4)
        self.label_cyclotron_calibration.setGeometry(QtCore.QRect(220, 5,125, 30))
        self.textbox_date_calibration = QtWidgets.QLineEdit(self.tab4)
        self.textbox_date_calibration.setGeometry(QtCore.QRect(360, 5, 100, 30))


        self.label_motor_calibration = QLabel("Motor calibration (mA): ",self.tab4)
        self.label_motor_calibration.setGeometry(QtCore.QRect(30, 40, 150, 30))
        #
        self.label_motor_calibration_before = QLabel("Before",self.tab4)
        self.label_motor_calibration_before.setGeometry(QtCore.QRect(120, 65, 150, 30))
        #
        self.label_motor_calibration_after = QLabel("After",self.tab4)
        self.label_motor_calibration_after.setGeometry(QtCore.QRect(220, 65, 150, 30))
        #
        self.label_motor_calibration_reference = QLabel("Reference",self.tab4)
        self.label_motor_calibration_reference.setGeometry(QtCore.QRect(320, 65, 150, 30))
        #
        self.label_motor_calibration_flap1 = QLabel("Flap 1:",self.tab4)
        self.label_motor_calibration_flap1.setGeometry(QtCore.QRect(30, 95, 70, 30))
        self.textbox_motor_calibration_flap1_before = QtWidgets.QLineEdit(self.tab4)
        self.textbox_motor_calibration_flap1_before.setGeometry(QtCore.QRect(120, 95, 100, 30))
        #
        self.textbox_motor_calibration_flap1_after = QtWidgets.QLineEdit(self.tab4)
        self.textbox_motor_calibration_flap1_after.setGeometry(QtCore.QRect(220, 95, 100, 30))
        #
        self.textbox_motor_calibration_flap1_reference = QtWidgets.QTextEdit(self.tab4)
        self.textbox_motor_calibration_flap1_reference.setGeometry(QtCore.QRect(320, 95, 100, 30))
        #
        self.label_calibration_flap2 = QLabel("Flap 2:",self.tab4)
        self.label_calibration_flap2.setGeometry(QtCore.QRect(30, 125, 70, 30))
        self.textbox_calibration_flap2_before = QtWidgets.QLineEdit(self.tab4)
        self.textbox_calibration_flap2_before.setGeometry(QtCore.QRect(120, 125, 100, 30))
        #
        self.textbox_calibration_flap2_after = QtWidgets.QLineEdit(self.tab4)
        self.textbox_calibration_flap2_after.setGeometry(QtCore.QRect(220, 125, 100, 30))
        #
        self.textbox_calibration_flap2_reference = QtWidgets.QTextEdit(self.tab4)
        self.textbox_calibration_flap2_reference.setGeometry(QtCore.QRect(320, 125, 100, 30))
        #
        #
        #
        self.label_caroussel1 = QLabel("Caroussel 1:",self.tab4)
        self.label_caroussel1.setGeometry(QtCore.QRect(30, 155, 75, 30))
        self.textbox_caroussel1_before = QtWidgets.QLineEdit(self.tab4)
        self.textbox_caroussel1_before.setGeometry(QtCore.QRect(120, 155, 100, 30))
        #
        self.textbox_caroussel1_after = QtWidgets.QLineEdit(self.tab4)
        self.textbox_caroussel1_after.setGeometry(QtCore.QRect(220, 155, 100, 30))
        #
        self.textbox_caroussel1_reference = QtWidgets.QTextEdit(self.tab4)
        self.textbox_caroussel1_reference.setGeometry(QtCore.QRect(320, 155, 100, 30))
        #
        self.label_caroussel2 = QLabel("Caroussel 2:",self.tab4)
        self.label_caroussel2.setGeometry(QtCore.QRect(30, 185, 75, 30))
        self.textbox_caroussel2_before = QtWidgets.QLineEdit(self.tab4)
        self.textbox_caroussel2_before.setGeometry(QtCore.QRect(120, 185, 100, 30))
        #
        self.textbox_caroussel2_after = QtWidgets.QLineEdit(self.tab4)
        self.textbox_caroussel2_after.setGeometry(QtCore.QRect(220, 185, 100, 30))
        #
        self.textbox_caroussel2_reference = QtWidgets.QTextEdit(self.tab4)
        self.textbox_caroussel2_reference.setGeometry(QtCore.QRect(320, 185, 100, 30))
        #
        self.label_balance = QLabel("Balance:",self.tab4)
        self.label_balance.setGeometry(QtCore.QRect(30, 215, 75, 30))
        self.textbox_balance_before = QtWidgets.QLineEdit(self.tab4)
        self.textbox_balance_before.setGeometry(QtCore.QRect(120, 215, 100, 30))
        #
        self.textbox_balance_after = QtWidgets.QLineEdit(self.tab4)
        self.textbox_balance_after.setGeometry(QtCore.QRect(220, 215, 100, 30))
        #
        self.textbox_balance_reference = QtWidgets.QTextEdit(self.tab4)
        self.textbox_balance_reference.setGeometry(QtCore.QRect(320, 215, 100, 30))
        #

        # IMPEDANCES EXTRACTION

        self.label_imp = QLabel("Impedances:",self.tab4)
        self.label_imp.setGeometry(QtCore.QRect(30, 270, 150, 30))
        #
        self.label_imp_before = QLabel("Before",self.tab4)
        self.label_imp_before.setGeometry(QtCore.QRect(120, 305, 150, 30))
        #
        self.label_imp_after = QLabel("After",self.tab4)
        self.label_imp_after.setGeometry(QtCore.QRect(220, 305, 150, 30))
        #
        self.label_imp_reference = QLabel("Reference",self.tab4)
        self.label_imp_reference.setGeometry(QtCore.QRect(320, 305, 150, 30))
        #
        self.label_iprobe = QLabel("Probe:",self.tab4)
        self.label_iprobe.setGeometry(QtCore.QRect(30, 335, 70, 30))
        self.textbox_iprobe_before = QtWidgets.QLineEdit(self.tab4)
        self.textbox_iprobe_before.setGeometry(QtCore.QRect(120, 335, 100, 30))
        #
        self.textbox_iprobe_after = QtWidgets.QLineEdit(self.tab4)
        self.textbox_iprobe_after.setGeometry(QtCore.QRect(220, 335, 100, 30))
        #
        self.textbox_iprobe_reference = QtWidgets.QTextEdit(self.tab4)
        self.textbox_iprobe_reference.setGeometry(QtCore.QRect(320, 335, 100, 30))
        #
        self.label_icaroussel1 = QLabel("Caroussel 1",self.tab4)
        self.label_icaroussel1.setGeometry(QtCore.QRect(30, 365, 100, 30))
        self.textbox_icaroussel1_before = QtWidgets.QLineEdit(self.tab4)
        self.textbox_icaroussel1_before.setGeometry(QtCore.QRect(120, 365, 100, 30))
        #
        self.textbox_icaroussel1_after = QtWidgets.QLineEdit(self.tab4)
        self.textbox_icaroussel1_after.setGeometry(QtCore.QRect(220, 365, 100, 30))
        #
        self.textbox_icaroussel1_reference= QtWidgets.QTextEdit(self.tab4)
        self.textbox_icaroussel1_reference.setGeometry(QtCore.QRect(320, 365, 100, 30))
        #
        self.label_icaroussel2 = QLabel("Caroussel 2:",self.tab4)
        self.label_icaroussel2.setGeometry(QtCore.QRect(30, 395, 100, 30))
        self.textbox_icaroussel2_before = QtWidgets.QLineEdit(self.tab4)
        self.textbox_icaroussel2_before.setGeometry(QtCore.QRect(120, 395, 100, 30))
        #
        self.textbox_icaroussel2_after = QtWidgets.QLineEdit(self.tab4)
        self.textbox_icaroussel2_after.setGeometry(QtCore.QRect(220, 395, 100, 30))
        #
        self.textbox_icaroussel2_reference = QtWidgets.QTextEdit(self.tab4)
        self.textbox_icaroussel2_reference.setGeometry(QtCore.QRect(320, 395, 100, 30))
        #
        self.label_iTarget1 = QLabel("Target 1:",self.tab4)
        self.label_iTarget1.setGeometry(QtCore.QRect(30, 425, 100, 30))
        self.textbox_iTarget1_before = QtWidgets.QLineEdit(self.tab4)
        self.textbox_iTarget1_before.setGeometry(QtCore.QRect(120, 425, 100, 30))
        #
        self.textbox_iTarget1_after = QtWidgets.QLineEdit(self.tab4)
        self.textbox_iTarget1_after.setGeometry(QtCore.QRect(220, 425, 100, 30))
        #
        self.textbox_iTarget1_reference = QtWidgets.QTextEdit(self.tab4)
        self.textbox_iTarget1_reference.setGeometry(QtCore.QRect(320, 425, 100, 30))
        #
        self.label_iTarget4 = QLabel("Target 4:",self.tab4)
        self.label_iTarget4.setGeometry(QtCore.QRect(30, 455, 100, 30))
        self.textbox_iTarget4_before = QtWidgets.QLineEdit(self.tab4)
        self.textbox_iTarget4_before.setGeometry(QtCore.QRect(120, 455, 100, 30))
        #
        self.textbox_iTarget4_after = QtWidgets.QLineEdit(self.tab4)
        self.textbox_iTarget4_after.setGeometry(QtCore.QRect(220, 455, 100, 30))
        #
        self.textbox_iTarget4_reference = QtWidgets.QTextEdit(self.tab4)
        self.textbox_iTarget4_reference.setGeometry(QtCore.QRect(320, 455, 100, 30))
        # BALANCE
        self.label_ibalance = QLabel("Balance:",self.tab4)
        self.label_ibalance.setGeometry(QtCore.QRect(30, 485, 75, 30))

        self.textbox_ibalance_before = QtWidgets.QLineEdit(self.tab4)
        self.textbox_ibalance_before.setGeometry(QtCore.QRect(120, 485, 100, 30))
        #
        self.textbox_ibalance_after = QtWidgets.QLineEdit(self.tab4)
        self.textbox_ibalance_after.setGeometry(QtCore.QRect(220, 485, 100, 30))
        #
        self.textbox_ibalance_reference = QtWidgets.QTextEdit(self.tab4)
        self.textbox_ibalance_reference.setGeometry(QtCore.QRect(320, 485, 100, 30))
        #

        self.plot_calibrations = Canvas(width=7, height=20, dpi=100, parent=self.tab4) 
        self.plot_calibrations.setGeometry(QtCore.QRect(460, 10, 730, 600))

        # 
        self.plot_trending_source = Canvas_tab2(width=7, height=7, dpi=100, parent=self.tab5) 
        self.plot_trending_source.setGeometry(QtCore.QRect(50, 10, 930, 600))
        self.toolbar_tab5 = NavigationToolbar(self.plot_trending_source, self.tab5)
        self.toolbar_tab5.setGeometry(QtCore.QRect(50, 600, 930, 100))
        #self.plot_trending_gas_flow = Canvas_tab2(width=7, height=20, dpi=100, parent=self.tab5) 
        #self.plot_trending_gas_flow.setGeometry(QtCore.QRect(50, 370, 830, 350))


        self.plot_trending_rf_height = Canvas_tab2(width=7, height=5, dpi=100, parent=self.tab6) 
        self.plot_trending_rf_height.setGeometry(QtCore.QRect(50, 10, 930, 600))

        self.plot_trending_rf_thicknees = Canvas_tab2(width=7, height=5, dpi=100, parent=self.tab7) 
        self.plot_trending_rf_thicknees.setGeometry(QtCore.QRect(50, 10, 930, 600))

        self.toolbar_tab6 = NavigationToolbar(self.plot_trending_rf_height, self.tab6)
        self.toolbar_tab6.setGeometry(QtCore.QRect(50, 600, 830, 100))
        self.toolbar_tab7 = NavigationToolbar(self.plot_trending_rf_thicknees, self.tab7)
        self.toolbar_tab7.setGeometry(QtCore.QRect(50, 600, 830, 100))
        #self.plot_trending_voltage_magnet = Canvas_tab2(width=7, height=20, dpi=100, parent=self.tab5) 
        #self.plot_trending_voltage_magnet.setGeometry(QtCore.QRect(50, 250, 830, 200))
    
        #self.setLayout(self.layout)


    def file_open_collimator_1(self,values):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName_collimator, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        pixmap = QPixmap(self.fileName_collimator)
        pixmap = pixmap.scaled(350, 350, QtCore.Qt.KeepAspectRatio)
        self.label_collimator_1.setPixmap(pixmap)
        self.resize(pixmap_rf.width(), pixmap_rf.height())
        self.show()


    def file_open_collimator_2(self,values):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName_collimator, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        pixmap_rf = QPixmap(self.fileName_collimator)
        pixmap_rf = pixmap_rf.scaled(350, 350, QtCore.Qt.KeepAspectRatio)
        self.label_collimator_2.setPixmap(pixmap_rf)
        self.resize(pixmap_rf.width(), pixmap_rf.height())
        self.show()
        #self.label_rf_position.setPixmap(pixmap_rf)
       
    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)



    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()


    def on_click_load_central(self):
        self.value_position_cyclotron = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.question_midplane =  QMessageBox()
        self.question_midplane.setText("Select an output folder to import central values")
        self.question_midplane.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_midplane.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_source = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_source_file = os.path.join(self.input_path_source,"central_region_values.out")
        self.df_central_region_selected = tfs.read(self.input_path_source_file)
        self.df_central_region_selected = self.df_central_region_selected[(self.df_central_region_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_central_region_selected["DATE"] == self.value_date)]
        print ("HEREEEE")
        print (self.df_central_region_selected)
        try:
           self.textbox_centralregion_a_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(A)_AFTER"].loc[0])
           self.textbox_centralregion_b_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(B)_AFTER"].loc[0])
           self.textbox_centralregion_c_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(C)_AFTER"].loc[0])
           self.textbox_centralregion_d_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(D)_AFTER"].loc[0])
        except:
            try:
               self.textbox_centralregion_a_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(A)_AFTER"].iloc[0] + "/" + self.df_central_region_selected["CENTRAL_REGION_(A)_AFTER"].iloc[0])
               self.textbox_centralregion_b_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(B)_AFTER"].iloc[0] + "/" + self.df_central_region_selected["CENTRAL_REGION_(B)_AFTER"].iloc[0]) 
               self.textbox_centralregion_c_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(C)_AFTER"].iloc[0] + "/" + self.df_central_region_selected["CENTRAL_REGION_(C)_AFTER"].iloc[0])
               self.textbox_centralregion_d_reference.setPlainText(self.df_central_region_selected["CENTRAL_REGION_(D)_AFTER"].iloc[0] + "/" + self.df_central_region_selected["CENTRAL_REGION_(D)_AFTER"].iloc[0])
            except:
               self.textbox_centralregion_a_reference.setPlainText("0")
               self.textbox_centralregion_b_reference.setPlainText("0")
               self.textbox_centralregion_c_reference.setPlainText("0")
               self.textbox_centralregion_d_reference.setPlainText("0")

    def on_click_load_source_performance(self):
        self.value_position_cyclotron = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.question_midplane =  QMessageBox()
        self.question_midplane.setText("Select an output folder to import beam performance value")
        self.question_midplane.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_midplane.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_source = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_source_file = os.path.join(self.input_path_source,"source_performance_values.out")
        print ("HEREEE")
        print (self.input_path_source_file)
        print ("DATE")
        print (self.value_date)
        print (self.value_position_cyclotron)
        self.df_source_performance_selected = tfs.read(self.input_path_source_file)
        print (self.df_source_performance_selected)
        self.df_source_performance_selected = self.df_source_performance_selected[(self.df_source_performance_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_source_performance_selected["DATE"] == self.value_date)]
        print (self.df_source_performance_selected)
        #print ("HEREEEE")
        #measurements_beam_performance = ["CYCLOTRON","DATE","DEE_VOLTAGE","MAGNET_I","GAS_FLOW","VACUUM","I_ION_SOURCE","I_PROBE","I_FOIL","I_TARGET","I_COLL_LOW","I_COLL_UP"]
        try:
             self.textbox_current_0_reference.setPlainText(self.df_source_performance_selected["CURRENT_0"].loc[0])
             self.textbox_current_50_reference.setPlainText(self.df_source_performance_selected["CURRENT_50"].loc[0])
             self.textbox_current_100_reference.setPlainText(self.df_source_performance_selected["CURRENT_100"].loc[0])
             self.textbox_current_150_reference.setPlainText(self.df_source_performance_selected["CURRENT_150"].loc[0])
             self.textbox_current_200_reference.setPlainText(self.df_source_performance_selected["CURRENT_200"].loc[0])
             self.textbox_current_250_reference.setPlainText(self.df_source_performance_selected["CURRENT_250"].loc[0])
             self.textbox_current_300_reference.setPlainText(self.df_source_performance_selected["CURRENT_300"].loc[0])
             self.textbox_current_350_reference.setPlainText(self.df_source_performance_selected["CURRENT_350"].loc[0])
             self.textbox_current_400_reference.setPlainText(self.df_source_performance_selected["CURRENT_400"].loc[0])
             self.textbox_current_450_reference.setPlainText(self.df_source_performance_selected["CURRENT_450"].loc[0])
             self.textbox_current_500_reference.setPlainText(self.df_source_performance_selected["CURRENT_500"].loc[0])
             self.textbox_current_550_reference.setPlainText(self.df_source_performance_selected["CURRENT_550"].loc[0])
             self.textbox_current_600_reference.setPlainText(self.df_source_performance_selected["CURRENT_600"].loc[0])
             print ("first")
        except:
            try:
               self.textbox_current_0_reference.setPlainText(self.df_source_performance_selected["CURRENT_0"].iloc[0] + "/" + self.df_source_performance_selected["CURREN_0"].iloc[0])
               self.textbox_current_50_reference.setPlainText(self.df_source_performance_selected["CURRENT_50"].iloc[0] + "/" + self.df_source_performance_selected["CURRENT_50"].iloc[0])
               self.textbox_current_100_reference.setPlainText(self.df_source_performance_selected["CURRENT_100"].iloc[0]  + "/" + self.df_source_performance_selected["CURRENT_100"].iloc[0])
               self.textbox_current_150_reference.setPlainText(self.df_source_performance_selected["CURRENT_150"].iloc[0] + "/" + self.df_source_performance_selected["CURRENT_150"].iloc[0])
               self.textbox_current_200_reference.setPlainText(self.df_source_performance_selected["CURRENT_200"].iloc[0] + "/" + self.df_source_performance_selected["CURRENT_200"].iloc[0])
               self.textbox_current_250_reference.setPlainText(self.df_source_performance_selected["CURRENT_250"].iloc[0] + "/" + self.df_source_performance_selected["CURRENT_250"].iloc[0])
               self.textbox_current_300_reference.setPlainText(self.df_source_performance_selected["CURRENT_300"].iloc[0] + "/" + self.df_source_performance_selected["CURRENT_300"].iloc[0])
               self.textbox_current_350_reference.setPlainText(self.df_source_performance_selected["CURRENT_350"].iloc[0] + "/" + self.df_source_performance_selected["CURRENT_350"].iloc[0])
               self.textbox_current_400_reference.setPlainText(self.df_source_performance_selected["CURRENT_400"].iloc[0] + "/" + self.df_source_performance_selected["CURRENT_400"].iloc[0])
               self.textbox_current_450_reference.setPlainText(self.df_source_performance_selected["CURRENT_450"].iloc[0] + "/" + self.df_source_performance_selected["CURRENT_450"].iloc[0])
               self.textbox_current_500_reference.setPlainText(self.df_source_performance_selected["CURRENT_500"].iloc[0] + "/" + self.df_source_performance_selected["CURRENT_500"].iloc[0])
               self.textbox_current_550_reference.setPlainText(self.df_source_performance_selected["CURRENT_550"].iloc[0] + "/" + self.df_source_performance_selected["CURRENT_550"].iloc[0])
               self.textbox_current_600_reference.setPlainText(self.df_source_performance_selected["CURRENT_600"].iloc[0] + "/" + self.df_source_performance_selected["CURRENT_600"].iloc[0])
               print ("second")
            except:
               self.textbox_current_0_reference.setPlainText("0")
               self.textbox_current_50_reference.setPlainText("0")
               self.textbox_current_100_reference.setPlainText("0")
               self.textbox_current_150_reference.setPlainText("0")
               self.textbox_current_200_reference.setPlainText("0")
               self.textbox_current_250_reference.setPlainText("0")
               self.textbox_current_300_reference.setPlainText("0")
               self.textbox_current_350_reference.setPlainText("0")
               self.textbox_current_400_reference.setPlainText("0")
               self.textbox_current_450_reference.setPlainText("0")
               self.textbox_current_500_reference.setPlainText("0")
               self.textbox_current_550_reference.setPlainText("0")
               self.textbox_current_600_reference.setPlainText("0")
               print ("three")

    def file_plot(self):
        x_values = [1,2]
        print (self.df_mid_plane_dee1)
        print (self.df_mid_plane_dee2)
        print (self.df_mid_plane.ACTUAL_A)
        print (type(self.df_mid_plane.ACTUAL_A))
        dif_ad = [float(self.variance_a),float(self.variance_d)]
        dif_eh = [float(self.variance_e),float(self.variance_h)]
        dif_fg = [float(self.variance_f),float(self.variance_g)]
        dif_bc = [float(self.variance_b),float(self.variance_c)]
        self.plot_rf.axes[0].clear()
        self.plot_rf.axes[1].clear()
        self.plot_rf.axes[0].errorbar(x_values,dif_ad,label="AD",picker=5,fmt="o",linestyle="-")
        self.plot_rf.axes[0].errorbar(x_values,dif_bc,label="BC",picker=5,fmt="o",linestyle="-")
        self.plot_rf.axes[1].errorbar(x_values,dif_eh,label="EH",picker=5,fmt="o",linestyle="-")
        self.plot_rf.axes[1].errorbar(x_values,dif_fg,label="FG",picker=5,fmt="o",linestyle="-")
        self.plot_rf.axes[0].legend(loc='best',ncol=5,fontsize=10)
        self.plot_rf.axes[1].legend(loc='best',ncol=5,fontsize=10)
        self.plot_rf.axes[0].set_xlabel(str("A,B left to C,D right"),fontsize=10)
        self.plot_rf.axes[0].set_ylabel(str("Distance from midplane [mm]"),fontsize=10)
        self.plot_rf.axes[1].set_xlabel(str("E,F left to G,H right"),fontsize=10)
        self.plot_rf.axes[1].set_ylabel(str("Distance from midplane [mm]"),fontsize=10)
        self.plot_rf.draw()
        self.plot_rf.show()
   
    def file_plot_dr(self):
        x_values = [1,2]
        print (self.df_mid_plane_dee1)
        print (self.df_mid_plane_dee2)
        print (self.df_mid_plane.ACTUAL_A)
        print (type(self.df_mid_plane.ACTUAL_A))
        dif_ad = [float(self.variance_a_reference),float(self.variance_d_reference)]
        dif_eh = [float(self.variance_e_reference),float(self.variance_h_reference)]
        dif_fg = [float(self.variance_f_reference),float(self.variance_g_reference)]
        dif_bc = [float(self.variance_b_reference),float(self.variance_c_reference)]
        #self.plot_rf.axes[0].clear()
        #self.plot_rf.axes[1].clear()
        self.plot_rf.axes[0].errorbar(x_values,dif_ad,label="AD (R)",picker=5,fmt="o",linestyle="-")
        self.plot_rf.axes[0].errorbar(x_values,dif_bc,label="BC (R)",picker=5,fmt="o",linestyle="-")
        self.plot_rf.axes[1].errorbar(x_values,dif_eh,label="EH (R)",picker=5,fmt="o",linestyle="-")
        self.plot_rf.axes[1].errorbar(x_values,dif_fg,label="FG (R)",picker=5,fmt="o",linestyle="-")
        self.plot_rf.axes[0].legend(loc='best',ncol=5,fontsize=10)
        self.plot_rf.axes[1].legend(loc='best',ncol=5,fontsize=10)
        self.plot_rf.axes[0].set_xlabel(str("A,B left to C,D right"),fontsize=10)
        self.plot_rf.axes[0].set_ylabel(str("Distance from midplane [mm]"),fontsize=10)
        self.plot_rf.axes[1].set_xlabel(str("E,F left to G,H right"),fontsize=10)
        self.plot_rf.axes[1].set_ylabel(str("Distance from midplane [mm]"),fontsize=10)
        self.plot_rf.draw()
        self.plot_rf.show()

    def file_plot_source(self):
        self.value_position_cyclotron = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.value_position_current_0 = float(str(self.textbox_current_0.text()))
        self.value_position_current_50 = float(str(self.textbox_current_50.text()))
        self.value_position_current_100 = float(str(self.textbox_current_100.text()))
        self.value_position_current_150 = float(str(self.textbox_current_150.text()))
        self.value_position_current_200 = float(str(self.textbox_current_200.text()))
        self.value_position_current_250 = float(str(self.textbox_current_250.text()))
        self.value_position_current_300 = float(str(self.textbox_current_300.text()))
        self.value_position_current_350 = float(str(self.textbox_current_350.text()))
        self.value_position_current_400 = float(str(self.textbox_current_400.text()))
        self.value_position_current_450 = float(str(self.textbox_current_450.text()))
        self.value_position_current_500 = float(str(self.textbox_current_500.text()))
        self.value_position_current_550 = float(str(self.textbox_current_550.text()))
        self.value_position_current_600 = float(str(self.textbox_current_600.text()))
        probe_values = [self.value_position_current_0,self.value_position_current_50,self.value_position_current_100,self.value_position_current_150,self.value_position_current_200,
        self.value_position_current_250,self.value_position_current_300,self.value_position_current_350,self.value_position_current_400,self.value_position_current_450,self.value_position_current_500,self.value_position_current_550,self.value_position_current_600]     
        source_values = np.linspace(0,600,13)
        print ("PROBE VALUES")
        print (source_values)
        print (probe_values)
        #self.plot_central.axes.clear()
        self.plot_central.axes.errorbar(source_values,probe_values,label="Current Source Performance",picker=5,fmt="o")
        self.plot_central.axes.legend(loc='best',ncol=1,fontsize=10)
        self.plot_central.axes.set_xlabel(str("Ion Source Current [mA]"),fontsize=10)
        self.plot_central.axes.set_ylabel(str("Probe Current [mA]"),fontsize=10)
        self.plot_central.draw()
        self.plot_central.show()

    def file_plot_source_reference(self):
        self.value_position_cyclotron = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.value_position_current_0 = float(str(self.textbox_current_0_reference.toPlainText()))
        self.value_position_current_50 = float(str(self.textbox_current_50_reference.toPlainText()))
        self.value_position_current_100 = float(str(self.textbox_current_100_reference.toPlainText()))
        self.value_position_current_150 = float(str(self.textbox_current_150_reference.toPlainText()))
        self.value_position_current_200 = float(str(self.textbox_current_200_reference.toPlainText()))
        self.value_position_current_250 = float(str(self.textbox_current_250_reference.toPlainText()))
        self.value_position_current_300 = float(str(self.textbox_current_300_reference.toPlainText()))
        self.value_position_current_350 = float(str(self.textbox_current_350_reference.toPlainText()))
        self.value_position_current_400 = float(str(self.textbox_current_400_reference.toPlainText()))
        self.value_position_current_450 = float(str(self.textbox_current_450_reference.toPlainText()))
        self.value_position_current_500 = float(str(self.textbox_current_500_reference.toPlainText()))
        self.value_position_current_550 = float(str(self.textbox_current_550_reference.toPlainText()))
        self.value_position_current_600 = float(str(self.textbox_current_600_reference.toPlainText()))
        probe_values = [self.value_position_current_0,self.value_position_current_50,self.value_position_current_100,self.value_position_current_150,self.value_position_current_200,
        self.value_position_current_250,self.value_position_current_300,self.value_position_current_350,self.value_position_current_400,self.value_position_current_450,self.value_position_current_500,self.value_position_current_550,self.value_position_current_600]     
        source_values = np.linspace(0,600,13)
        print ("PROBE VALUES")
        print (source_values)
        print (probe_values)
        #self.plot_central.axes.clear()
        self.plot_central.axes.errorbar(source_values,probe_values,label="Current Source Performance (Reference)",picker=5,fmt="o")
        self.plot_central.axes.legend(loc='best',ncol=1,fontsize=10)
        self.plot_central.axes.set_xlabel(str("Ion Source Current [mA]"),fontsize=10)
        self.plot_central.axes.set_ylabel(str("Probe Current [mA]"),fontsize=10)
        self.plot_central.draw()
        self.plot_central.show()

    def on_click_load_beam_performance(self):
        self.value_position_cyclotron = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.question_midplane =  QMessageBox()
        self.question_midplane.setText("Select an output folder to import beam performance value")
        self.question_midplane.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_midplane.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_beam_performance = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_beam_performance_file = os.path.join(self.input_path_beam_performance,"beam_performance_values.out")
        print ("HEREEE")
        self.df_beam_performance_selected = tfs.read(self.input_path_beam_performance_file)
        self.df_beam_performance_selected = self.df_beam_performance_selected[(self.df_beam_performance_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_beam_performance_selected["DATE"] == self.value_date)]
        print (self.df_beam_performance_selected)
        #print ("HEREEEE")
        #measurements_beam_performance = ["CYCLOTRON","DATE","DEE_VOLTAGE","MAGNET_I","GAS_FLOW","VACUUM","I_ION_SOURCE","I_PROBE","I_FOIL","I_TARGET","I_COLL_LOW","I_COLL_UP"]
        try:
             self.textbox_beam_dee_voltage_reference.setPlainText(self.df_beam_performance_selected["DEE_VOLTAGE"].loc[0])
             self.textbox_magnet_i_reference.setPlainText(self.df_beam_performance_selected["MAGNET_I"].loc[0])
             self.textbox_gas_flow_reference.setPlainText(self.df_beam_performance_selected["GAS_FLOW"].loc[0])
             self.textbox_vacuum_reference.setPlainText(self.df_beam_performance_selected["VACUUM"].loc[0])
             self.textbox_i_ion_source_reference.setPlainText(self.df_beam_performance_selected["I_ION_SOURCE"].loc[0])
             self.textbox_i_probe_reference.setPlainText(self.df_beam_performance_selected["I_PROBE"].loc[0])
             self.textbox_i_foil_reference.setPlainText(self.df_beam_performance_selected["I_FOIL"].loc[0])
             self.textbox_i_target_reference.setPlainText(self.df_beam_performance_selected["I_TARGET"].loc[0])
             self.textbox_i_coll_low_reference.setPlainText(self.df_beam_performance_selected["I_COLL_LOW"].loc[0])
             self.textbox_i_coll_up_reference.setPlainText(self.df_beam_performance_selected["I_COLL_UP"].loc[0])
             print ("first")
        except:
            try:
               self.textbox_beam_dee_voltage_reference.setPlainText(self.df_beam_performance_selected["DEE_VOLTAGE"].iloc[0] + "/" + self.df_beam_performance_selected["DEE_VOLTAGE"].iloc[0])
               self.textbox_magnet_i_reference.setPlainText(self.df_beam_performance_selected["MAGNET_I"].iloc[0] + "/" + self.df_beam_performance_selected["MAGNET_I"].iloc[0])
               self.textbox_gas_flow_reference.setPlainText(self.df_beam_performance_selected["GAS_FLOW"].iloc[0]  + "/" + self.df_beam_performance_selected["GAS_FLOW"].iloc[0])
               self.textbox_vacuum_reference.setPlainText(self.df_beam_performance_selected["VACUUM"].iloc[0] + "/" + self.df_beam_performance_selected["VACUUM"].iloc[0])
               self.textbox_i_ion_source_reference.setPlainText(self.df_beam_performance_selected["I_ION_SOURCE"].iloc[0] + "/" + self.df_beam_performance_selected["I_ION_SOURCE"].iloc[0])
               self.textbox_i_probe_reference.setPlainText(self.df_beam_performance_selected["I_PROBE"].iloc[0] + "/" + self.df_beam_performance_selected["I_PROBE"].iloc[0])
               self.textbox_i_foil_reference.setPlainText(self.df_beam_performance_selected["I_FOIL"].iloc[0] + "/" + self.df_beam_performance_selected["I_FOIL"].iloc[0])
               self.textbox_i_target_reference.setPlainText(self.df_beam_performance_selected["I_TARGET"].iloc[0] + "/" + self.df_beam_performance_selected["I_TARGET"].iloc[0])
               self.textbox_i_coll_low_reference.setPlainText(self.df_beam_performance_selected["I_COLL_LOW"].iloc[0] + "/" + self.df_beam_performance_selected["I_COLL_LOW"].iloc[0])
               self.textbox_i_coll_up_reference.setPlainText(self.df_beam_performance_selected["I_COLL_UP"].iloc[0] + "/" + self.df_beam_performance_selected["I_COLL_UP"].iloc[0])
               print ("second")
            except:
               self.textbox_beam_dee_voltage_reference.setPlainText("0")
               self.textbox_magnet_i_reference.setPlainText("0")
               self.textbox_gas_flow_reference.setPlainText("0")
               self.textbox_vacuum_reference.setPlainText("0")
               self.textbox_i_ion_source_reference.setPlainText("0")
               self.textbox_i_probe_reference.setPlainText("0")
               self.textbox_i_foil_reference.setPlainText("0")
               self.textbox_i_target_reference.setPlainText("0")
               self.textbox_i_coll_low_reference.setPlainText("0")
               self.textbox_i_coll_up_reference.setPlainText("0")
               print ("three")

    def on_click_load_collimators(self):
        self.value_position_cyclotron = self.textbox_cyclotron_collimators.text()
        self.value_date = self.textbox_date_collimators.text()
        self.question_collimators =  QMessageBox()
        self.question_collimators.setText("Select an import folder to import Collimator values")
        self.question_collimators.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_collimators.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_collimators = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_collimators_file = os.path.join(self.input_path_collimators,"collimators_values.out")
        print (self.input_path_collimators_file)
        self.df_collimators_selected = tfs.read(self.input_path_collimators_file)
        print ("HEREEEEEEE")
        print (self.df_collimators_selected)
        self.df_collimators_selected_cyclotron = self.df_collimators_selected[(self.df_collimators_selected["CYCLOTRON"] == self.value_position_cyclotron)]
        self.df_collimators_selected = self.df_collimators_selected[(self.df_collimators_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_collimators_selected["DATE"] == self.value_date)]      
        print ("HEREEEEEEEEE")
        print (self.df_collimators_selected)
        if len(np.array(self.df_collimators_selected["COLL_1_APERTURE_AFTER"].values)) == 1:
               print ("first step")
               self.textbox_coll1_aperture_reference.setPlainText(np.array(self.df_collimators_selected["COLL_1_APERTURE_AFTER"].values)[0])
               self.textbox_coll2_aperture_reference.setPlainText(np.array(self.df_collimators_selected["COLL_2_APERTURE_AFTER"].values)[0])
               self.textbox_coll1_separation_reference.setPlainText(np.array(self.df_collimators_selected["COLL_1_SEPARATION_AFTER"].values)[0])
               self.textbox_coll2_separation_reference.setPlainText(np.array(self.df_collimators_selected["COLL_2_SEPARATION_AFTER"].values)[0])
               self.textbox_icollimator1_l_reference.setPlainText(np.array(self.df_collimators_selected["COLL_1_L_IMPEDANCE_AFTER"].values)[0])
               self.textbox_icollimator2_l_reference.setPlainText(np.array(self.df_collimators_selected["COLL_2_L_IMPEDANCE_AFTER"].values)[0])
               self.textbox_icollimator1_u_reference.setPlainText(np.array(self.df_collimators_selected["COLL_1_U_IMPEDANCE_AFTER"].values)[0])
               self.textbox_icollimator2_u_reference.setPlainText(np.array(self.df_collimators_selected["COLL_2_U_IMPEDANCE_AFTER"].values)[0])
        elif len(np.array(self.df_collimators_selected["COLL_1_APERTURE_AFTER"].values)) > 1:
               self.textbox_coll1_aperture_reference.setPlainText(np.array(self.df_collimators_selected["COLL_1_APERTURE_AFTER"].values)[0] + "/" + np.array(self.df_collimators_selected["COLL_1_APERTURE_AFTER"].values)[1])
               self.textbox_coll2_aperture_reference.setPlainText(np.array(self.df_collimators_selected["COLL_2_APERTURE_AFTER"].values)[0] + "/" + np.array(self.df_collimators_selected["COLL_2_APERTURE_AFTER"].values)[1])
               self.textbox_coll1_separation_reference.setPlainText(np.array(self.df_collimators_selected["COLL_1_SEPARATION_AFTER"].values)[0] + "/" + np.array(self.df_collimators_selected["COLL_1_SEPARATION_AFTER"].values)[1])
               self.textbox_coll1_separation_reference.setPlainText(np.array(self.df_collimators_selected["COLL_2_SEPARATION_AFTER"].values)[0] + "/" + np.array(self.df_collimators_selected["COLL_2_SEPARATION_AFTER"].values)[1])
               self.textbox_icollimator1_l_reference.setPlainText(np.array(self.df_collimators_selected["COLL_1_L_IMPEDANCE_AFTER"].values)[0] + "/" + np.array(self.df_collimators_selected["COLL_1_L_IMPEDANCE_AFTER"].values)[1])
               self.textbox_icollimator2_l_reference.setPlainText(np.array(self.df_collimators_selected["COLL_2_L_IMPEDANCE_AFTER"].values)[0] + "/" + np.array(self.df_collimators_selected["COLL_2_L_IMPEDANCE_AFTER"].values)[1])
               self.textbox_icollimator1_u_reference.setPlainText(np.array(self.df_collimators_selected["COLL_1_U_IMPEDANCE_AFTER"].values)[0] + "/" + np.array(self.df_collimators_selected["COLL_1_U_IMPEDANCE_AFTER"].values)[1])
               self.textbox_icollimator2_u_reference.setPlainText(np.array(self.df_collimators_selected["COLL_2_U_IMPEDANCE_AFTER"].values)[0] + "/" + np.array(self.df_collimators_selected["COLL_2_U_IMPEDANCE_AFTER"].values)[1])
        else:
               self.textbox_coll1_aperture_reference.setPlainText("0")
               self.textbox_coll2_aperture_reference.setPlainText("0")
               self.textbox_coll1_separation_reference.setPlainText("0")
               self.textbox_coll2_separation_reference.setPlainText("0")
               self.textbox_icollimator1_l_reference.setPlainText("0")
               self.textbox_icollimator2_l_reference.setPlainText("0")
               self.textbox_icollimator1_u_reference.setPlainText("0")
               self.textbox_icollimator2_u_reference.setPlainText("0")
        self.plot_collimators.axes[0].axes.clear()
        self.plot_collimators.axes[0].set_ylabel(str("Aperture [mm]"),fontsize=12)
        #self.plot_collimators.axes[0].set_xlabel(str("Date"),fontsize=12)
        self.plot_collimators.axes[1].set_ylabel(str("Separation [mm]"),fontsize=12)
        self.plot_collimators.axes[1].set_xlabel(str("Date"),fontsize=12)
        self.plot_collimators.axes[1].set_xticklabels(self.df_collimators_selected_cyclotron.DATE, rotation=45)
        self.plot_collimators.axes[0].errorbar(self.df_collimators_selected_cyclotron.DATE,self.df_collimators_selected_cyclotron.COLL_1_APERTURE_AFTER.astype(float),label="COLLIMATOR 1",picker=5,fmt="o")
        self.plot_collimators.axes[0].errorbar(self.df_collimators_selected_cyclotron.DATE,self.df_collimators_selected_cyclotron.COLL_2_APERTURE_AFTER.astype(float),label="COLLIMATOR 2",picker=5,fmt="o")
        print ("test!!!!!")
        print (self.df_collimators_selected_cyclotron.COLL_1_SEPARATION_AFTER)
        self.plot_collimators.axes[1].errorbar(self.df_collimators_selected_cyclotron.DATE,self.df_collimators_selected_cyclotron.COLL_1_SEPARATION_AFTER.astype(float),label="COLLIMATOR 1",picker=5,fmt="o")
        self.plot_collimators.axes[1].errorbar(self.df_collimators_selected_cyclotron.DATE,self.df_collimators_selected_cyclotron.COLL_2_SEPARATION_AFTER.astype(float),label="COLLIMATOR 2",picker=5,fmt="o")
        self.plot_collimators.axes[0].legend(loc='best',ncol=2,fontsize=12)
        self.plot_collimators.axes[1].legend(loc='best',ncol=2,fontsize=12)
        self.plot_collimators.draw()
        self.plot_collimators.show()

    def on_click_load_flaps(self):
        self.value_position_cyclotron = self.textbox_cyclotron_collimators.text()
        self.value_date = self.textbox_date_collimators.text()
        self.question_collimators =  QMessageBox()
        self.question_collimators.setText("Select an import folder to import Collimator values")
        self.question_collimators.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_collimators.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_collimators = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_collimators_file = os.path.join(self.input_path_collimators,"flap_measurements.out")
        print (self.input_path_collimators_file)
        self.df_collimators_selected = tfs.read(self.input_path_collimators_file)
        print ("HEREEEEEEE")
        print (self.df_collimators_selected)
        self.df_collimators_selected_cyclotron = self.df_collimators_selected[(self.df_collimators_selected["CYCLOTRON"] == self.value_position_cyclotron)]
        self.df_collimators_selected = self.df_collimators_selected[(self.df_collimators_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_collimators_selected["DATE"] == self.value_date)]      
        print ("HEREEEEEEEEE")
        print (self.df_collimators_selected)
        if len(np.array(self.df_collimators_selected["FLAP1_0"].values)) == 1:
               print ("first step")
               self.textbox_flap1_position_0.setPlainText(np.array(self.df_collimators_selected["FLAP1_0"].values)[0])
               self.textbox_flap1_position_50.setPlainText(np.array(self.df_collimators_selected["FLAP1_50"].values)[0])
               self.textbox_flap1_position_100.setPlainText(np.array(self.df_collimators_selected["FLAP1_100"].values)[0])
               self.textbox_flap2_position_0.setPlainText(np.array(self.df_collimators_selected["FLAP1_0"].values)[0])
               self.textbox_flap2_position_50.setPlainText(np.array(self.df_collimators_selected["FLAP1_50"].values)[0])
               self.textbox_flap2_position_100.setPlainText(np.array(self.df_collimators_selected["FLAP1_100"].values)[0])
        elif len(np.array(self.df_collimators_selected["FLAP2_0"].values)) > 1:
               self.textbox_flap1_position_0.setPlainText(np.array(self.df_collimators_selected["FLAP1_0"].values)[0] + "/" + self.textbox_flap1_position_0.setPlainText(np.array(self.df_collimators_selected["FLAP1_0"].values)[1]))
               self.textbox_flap1_position_50.setPlainText(np.array(self.df_collimators_selected["FLAP1_50"].values)[0] + "/" + self.textbox_flap1_position_50.setPlainText(np.array(self.df_collimators_selected["FLAP1_50"].values)[1]))
               self.textbox_flap1_position_100.setPlainText(np.array(self.df_collimators_selected["FLAP1_100"].values)[0] + "/" + self.textbox_flap1_position_100.setPlainText(np.array(self.df_collimators_selected["FLAP1_100"].values)[1]))
               self.textbox_flap2_position_0.setPlainText(np.array(self.df_collimators_selected["FLAP1_0"].values)[0] + "/" + self.textbox_flap2_position_0.setPlainText(np.array(self.df_collimators_selected["FLAP1_0"].values)[1]))
               self.textbox_flap2_position_50.setPlainText(np.array(self.df_collimators_selected["FLAP1_50"].values)[0] + "/" + self.textbox_flap2_position_50.setPlainText(np.array(self.df_collimators_selected["FLAP1_50"].values)[1]))
               self.textbox_flap2_position_100.setPlainText(np.array(self.df_collimators_selected["FLAP1_100"].values)[0] + "/" + self.textbox_flap2_position_100.setPlainText(np.array(self.df_collimators_selected["FLAP1_100"].values)[1]))
        else:
               self.textbox_flap1_position_0.setPlainText("0")
               self.textbox_flap1_position_50.setPlainText("0")
               self.textbox_flap1_position_100.setPlainText("0")
               self.textbox_flap2_position_0.setPlainText("0")
               self.textbox_flap2_position_50.setPlainText("0")
               self.textbox_flap2_position_100.setPlainText("0")
        self.plot_collimators.axes[0].axes.clear()
        self.plot_collimators.axes[0].set_ylabel(str("Position [mm]"),fontsize=12)
        #self.plot_collimators.axes[0].set_xlabel(str("Date"),fontsize=12)
        self.plot_collimators.axes[1].set_ylabel(str("Position [mm]"),fontsize=12)
        self.plot_collimators.axes[1].set_xlabel(str("Date"),fontsize=12)
        self.plot_collimators.axes[1].set_xticklabels(self.df_collimators_selected_cyclotron.DATE, rotation=45)
        self.plot_collimators.axes[0].errorbar(self.df_collimators_selected_cyclotron.DATE,self.df_collimators_selected_cyclotron.FLAP1_0.astype(float),label="FLAP 1 (0%)",picker=5,fmt="o")
        self.plot_collimators.axes[0].errorbar(self.df_collimators_selected_cyclotron.DATE,self.df_collimators_selected_cyclotron.FLAP1_50.astype(float),label="FLAP 1 (50%)",picker=5,fmt="o")
        self.plot_collimators.axes[0].errorbar(self.df_collimators_selected_cyclotron.DATE,self.df_collimators_selected_cyclotron.FLAP1_100.astype(float),label="FLAP 1 (100%)",picker=5,fmt="o")
        print ("test!!!!!")
        print (self.df_collimators_selected_cyclotron.COLL_1_SEPARATION_AFTER)
        self.plot_collimators.axes[0].errorbar(self.df_collimators_selected_cyclotron.DATE,self.df_collimators_selected_cyclotron.FLAP2_0.astype(float),label="FLAP 2 (0%)",picker=5,fmt="o")
        self.plot_collimators.axes[0].errorbar(self.df_collimators_selected_cyclotron.DATE,self.df_collimators_selected_cyclotron.FLAP2_50.astype(float),label="FLAP 2 (50%)",picker=5,fmt="o")
        self.plot_collimators.axes[0].errorbar(self.df_collimators_selected_cyclotron.DATE,self.df_collimators_selected_cyclotron.FLAP2_100.astype(float),label="FLAP 2 (100%)",picker=5,fmt="o")
        self.plot_collimators.axes[0].legend(loc='best',ncol=2,fontsize=12)
        self.plot_collimators.axes[1].legend(loc='best',ncol=2,fontsize=12)
        self.plot_collimators.draw()
        self.plot_collimators.show()


    def on_click_load_motors(self):
        self.value_position_cyclotron = self.textbox_cyclotron_calibration.text()
        self.value_date = self.textbox_date_calibration.text()
        self.question_motors =  QMessageBox()
        self.question_motors.setText("Select an import folder to import Collimator values")
        self.question_motors.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_motors.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_motors = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_motors_file = os.path.join(self.input_path_motors,"motor_values.out")
        self.input_path_impedance_file = os.path.join(self.input_path_motors,"impedance_values.out")
        self.input_path_impedance_file_collimators = os.path.join(self.input_path_motors,"collimators_values.out")
        self.df_motors_selected = tfs.read(self.input_path_motors_file)
        self.df_input_path_impedance = tfs.read(self.input_path_impedance_file)

        self.df_motors_selected_cyclotron = self.df_motors_selected[(self.df_motors_selected["CYCLOTRON"] == self.value_position_cyclotron)]
        print ("HEREEEEEEEE")
        print (self.df_motors_selected)
        self.df_motors_selected = self.df_motors_selected[(self.df_motors_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_motors_selected["DATE"] == self.value_date)]
        if len(np.array(self.df_motors_selected["FLAP_1_AFTER"].values)) == 1:
               print ("first step")
               self.textbox_motor_calibration_flap1_reference.setPlainText(np.array(self.df_motors_selected["FLAP_1_AFTER"].values)[0])
               self.textbox_calibration_flap2_reference.setPlainText(np.array(self.df_motors_selected["FLAP_2_AFTER"].values)[0])
               self.textbox_caroussel1_reference.setPlainText(np.array(self.df_motors_selected["CARROUSSEL_1_AFTER"].values)[0])
               self.textbox_caroussel2_reference.setPlainText(np.array(self.df_motors_selected["CARROUSSEL_2_AFTER"].values)[0])
               self.textbox_balance_reference.setPlainText(np.array(self.df_motors_selected["BALANCE_AFTER"].values)[0])
        elif len(np.array(self.df_motors_selected["FLAP_1_AFTER"].values)) > 1:
               self.textbox_motor_calibration_flap1_reference.setPlainText(np.array(self.df_motors_selected["FLAP_1_AFTER"].values)[0] + "/" + np.array(self.df_motors_selected["FLAP_1_AFTER"].values)[1])
               self.textbox_calibration_flap2_reference.setPlainText(np.array(self.df_motors_selected["FLAP_2_AFTER"].values)[0] + "/" + np.array(self.df_motors_selected["FLAP_2_AFTER"].values)[1])
               self.textbox_caroussel1_reference.setPlainText(np.array(self.df_motors_selected["CARROUSSEL_1_AFTER"].values)[0] + "/" + np.array(self.df_motors_selected["CARROUSSEL_1_AFTER"].values)[1])
               self.textbox_caroussel2_reference.setPlainText(np.array(self.df_motors_selected["CARROUSSEL_2_AFTER"].values)[0] + "/" + np.array(self.df_motors_selected["CARROUSSEL_2_AFTER"].values)[1])
               self.textbox_balance_reference.setPlainText(np.array(self.df_motors_selected["BALANCE_AFTER"].values)[0] + "/" + np.array(self.df_motors_selected["BALANCE_AFTER"].values)[1])
        else:
               self.textbox_motor_calibration_flap1_reference.setPlainText("0")
               self.textbox_calibration_flap2_reference.setPlainText("0")
               self.textbox_caroussel1_reference.setPlainText("0")
               self.textbox_caroussel2_reference.setPlainText("0")
               self.textbox_balance_reference.setPlainText("0")
        self.plot_calibrations.axes[0].set_ylabel(str("Calibration [-]"),fontsize=10)
        self.plot_calibrations.axes[0].set_xlabel(str("Date"),fontsize=10)
        self.plot_calibrations.axes[1].set_ylabel(str(r"Impedance [k$\Omega$]"),fontsize=10)
        self.plot_calibrations.axes[1].set_xlabel(str("Date"),fontsize=10)

        print ("HEREEEE")
        print (self.df_motors_selected_cyclotron.FLAP_1_AFTER)
        print (self.df_motors_selected_cyclotron.FLAP_2_AFTER)

        self.plot_calibrations.axes[0].errorbar(self.df_motors_selected_cyclotron.DATE,self.df_motors_selected_cyclotron.FLAP_1_AFTER.astype(float),label="FLAP 1",picker=5,fmt="o")
        self.plot_calibrations.axes[0].errorbar(self.df_motors_selected_cyclotron.DATE,self.df_motors_selected_cyclotron.FLAP_2_AFTER.astype(float),label="FLAP 2",picker=5,fmt="o")
        self.plot_calibrations.axes[0].errorbar(self.df_motors_selected_cyclotron.DATE,self.df_motors_selected_cyclotron.CARROUSSEL_1_AFTER.astype(float),label="CARROUSEL 1",picker=5,fmt="o")
        self.plot_calibrations.axes[0].errorbar(self.df_motors_selected_cyclotron.DATE,self.df_motors_selected_cyclotron.CARROUSSEL_2_AFTER.astype(float),label="CARROUSEL 2",picker=5,fmt="o")
        self.plot_calibrations.axes[0].errorbar(self.df_motors_selected_cyclotron.DATE,self.df_motors_selected_cyclotron.CARROUSSEL_2_AFTER.astype(float),label="BALANCE",picker=5,fmt="o")

        print ("HEREEEE!!!!!")
        print (self.df_input_path_impedance)
        self.plot_calibrations.axes[1].errorbar(self.df_input_path_impedance.DATE,self.df_input_path_impedance.PROBE_AFTER.astype(float) ,label="PROBE",picker=5,fmt="o")
        self.plot_calibrations.axes[1].errorbar(self.df_input_path_impedance.DATE,self.df_input_path_impedance.TARGET_1_AFTER.astype(float),label="TARGET 1",picker=5,fmt="o")
        self.plot_calibrations.axes[1].errorbar(self.df_input_path_impedance.DATE,self.df_input_path_impedance.TARGET_4_AFTER.astype(float),label="TARGET 4",picker=5,fmt="o")
        self.plot_calibrations.axes[1].errorbar(self.df_input_path_impedance.DATE,self.df_input_path_impedance.CARROUSSEL_1_AFTER.astype(float),label="CARROUSEL 1",picker=5,fmt="o")
        self.plot_calibrations.axes[1].errorbar(self.df_input_path_impedance.DATE,self.df_input_path_impedance.CARROUSSEL_2_AFTER.astype(float),label="CARROUSEL 2",picker=5,fmt="o")
        self.plot_calibrations.axes[1].errorbar(self.df_input_path_impedance.DATE,self.df_input_path_impedance.BALANCE_AFTER.astype(float),label="BALANCE_AFTER",picker=5,fmt="o")
        self.plot_calibrations.draw()
        self.plot_calibrations.show()

                           
               
    def on_click_load_impendance(self):
        self.value_position_cyclotron = self.textbox_cyclotron_calibration.text()
        self.value_date = self.textbox_date_calibration.text()
        self.question_impedance =  QMessageBox()
        self.question_impedance.setText("Select an import folder to import Collimator values")
        self.question_impedance.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_impedance.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_impedance = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_impedance_file = os.path.join(self.input_path_impedance,"impedance_values.out")
        self.df_impedance_selected = tfs.read(self.input_path_impedance_file)
        self.df_impedance_selected_cyclotron = self.df_impedance_selected[(self.df_impedance_selected["CYCLOTRON"] == self.value_position_cyclotron)]
        self.df_impedance_selected = self.df_impedance_selected[(self.df_impedance_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_impedance_selected["DATE"] == self.value_date)]
        print (self.df_impedance_selected)
        if len(np.array(self.df_impedance_selected["PROBE_AFTER"].values)) == 1:
               print ("first step")
               self.textbox_iprobe_reference.setPlainText(np.array(self.df_impedance_selected["PROBE_AFTER"].values)[0])
               self.textbox_icaroussel1_reference.setPlainText(np.array(self.df_impedance_selected["CARROUSSEL_1_AFTER"].values)[0])
               self.textbox_icaroussel2_reference.setPlainText(np.array(self.df_impedance_selected["CARROUSSEL_2_AFTER"].values)[0])
               self.textbox_iTarget1_reference.setPlainText(np.array(self.df_impedance_selected["TARGET_1_AFTER"].values)[0])
               self.textbox_iTarget4_reference.setPlainText(np.array(self.df_impedance_selected["TARGET_4_AFTER"].values)[0])
               self.textbox_ibalance_reference.setPlainText(np.array(self.df_impedance_selected["TARGET_4_AFTER"].values)[0])
        elif len(np.array(self.df_impedance_selected["PROBE_AFTER"].values)) > 1:
               self.textbox_iprobe_reference.setPlainText(np.array(self.df_impedance_selected["PROBE_AFTER"].values)[0] + "/" + np.array(self.df_impedance_selected["PROBE_AFTER"].values)[1])
               self.textbox_icaroussel1_reference.setPlainText(np.array(self.df_impedance_selected["CARROUSSEL_1_AFTER"].values)[0] + "/" + np.array(self.df_impedance_selected["CARROUSSEL_1_AFTER"].values)[1])
               self.textbox_icaroussel2_reference.setPlainText(np.array(self.df_impedance_selected["CARROUSSEL_2_AFTER"].values)[0] + "/" + np.array(self.df_impedance_selected["CARROUSSEL_2_AFTER"].values)[1])
               self.textbox_iTarget1_reference.setPlainText(np.array(self.df_impedance_selected["TARGET_1_AFTER"].values)[0] + "/" + np.array(self.df_impedance_selected["TARGET_1_AFTER"].values)[1])
               self.textbox_iTarget4_reference.setPlainText(np.array(self.df_impedance_selected["TARGET_4_AFTER"].values)[0] + "/" + np.array(self.df_impedance_selected["TARGET_4_AFTER"].values)[1])
               self.textbox_ibalance_reference.setPlainText(np.array(self.df_impedance_selected["TARGET_4_AFTER"].values)[0] + "/" + np.array(self.df_impedance_selected["TARGET_4_AFTER"].values)[1])    
        else:
               self.textbox_iprobe_reference.setPlainText("0")
               self.textbox_icaroussel1_reference.setPlainText("0")
               self.textbox_icaroussel2_reference.setPlainText("0")
               self.textbox_iTarget1_reference.setPlainText("0")
               self.textbox_iTarget4_reference.setPlainText("0")
               self.textbox_ibalance_reference.setPlainText("0")

        self.plot_calibrations.axes[0].set_ylabel(str("Calibration [%]"),fontsize=10)
        self.plot_calibrations.axes[0].set_xlabel(str("Date"),fontsize=10)
        self.plot_calibrations.axes[1].set_ylabel(str(r"Impedance [k$\Omega$]"),fontsize=10)
        self.plot_calibrations.axes[1].set_xlabel(str("Date"),fontsize=10)
        self.plot_calibrations.axes[1].errorbar(self.df_impedance_selected_cyclotron.DATE,self.df_impedance_selected_cyclotron.TARGET_1_AFTER,label="TARGET 1",picker=5,fmt="o")
        self.plot_calibrations.axes[1].errorbar(self.df_impedance_selected_cyclotron.DATE,self.df_impedance_selected_cyclotron.TARGET_4_AFTER,label="TARGET 4",picker=5,fmt="o")
        self.plot_calibrations.axes[1].errorbar(self.df_impedance_selected_cyclotron.DATE,self.df_impedance_selected_cyclotron.PROBE_AFTER,label="PROBE",picker=5,fmt="o")
        self.plot_calibrations.axes[1].errorbar(self.df_impedance_selected_cyclotron.DATE,self.df_impedance_selected_cyclotron.CARROUSSEL_1_AFTER,label="CARROUSEL 1",picker=5,fmt="o")
        self.plot_calibrations.axes[1].errorbar(self.df_impedance_selected_cyclotron.DATE,self.df_impedance_selected_cyclotron.CARROUSSEL_2_AFTER,label="CARROUSEL 2",picker=5,fmt="o")
        self.plot_calibrations.axes[1].errorbar(self.df_impedance_selected_cyclotron.DATE,self.df_impedance_selected_cyclotron.CARROUSSEL_2_AFTER,label="BALANCE",picker=5,fmt="o")
        self.plot_calibrations.draw()
        self.plot_calibrations.show()

    def on_click_load_rf1(self):
        self.value_position_cyclotron = self.textbox_cyclotron_rf.text()
        self.value_date = self.textbox_date_rf.text()
        self.question_midplane =  QMessageBox()
        self.question_midplane.setText("Select an output folder to import RF Dee1 values")
        self.question_midplane.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_midplane.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_rf = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_rf_file = os.path.join(self.input_path_rf,"rf_dee1_values.out")
        print (self.input_path_rf_file)
        self.df_rf_dee1_selected = tfs.read(self.input_path_rf_file)
        print ()
        self.df_rf_dee1_selected = self.df_rf_dee1_selected[(self.df_rf_dee1_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_rf_dee1_selected["DATE"] == self.value_date)]
        if len(np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_A_AFTER"].values)) == 1:
               print ("first step")
               self.textbox_dee1h_a_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_A_AFTER"].values)[0])
               self.textbox_dee1h_b_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_B_AFTER"].values)[0])
               self.textbox_dee1h_c_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_C_AFTER"].values)[0])
               self.textbox_dee1h_d_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_D_AFTER"].values)[0])
               self.textbox_dee1_a_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_THICKNESS_A_AFTER"].values)[0])
               self.textbox_dee1_b_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_THICKNESS_B_AFTER"].values)[0])
               self.textbox_dee1_c_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_THICKNESS_C_AFTER"].values)[0])
               self.textbox_dee1_d_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_THICKNESS_D_AFTER"].values)[0])
        elif len(np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_A_AFTER"].values)) > 1:
               self.textbox_dee1h_a_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_A_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_A_AFTER"].values)[1])
               self.textbox_dee1h_b_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_B_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_B_AFTER"].values)[1])
               self.textbox_dee1h_c_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_C_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_C_AFTER"].values)[1])
               self.textbox_dee1h_d_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_D_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee1_selected["RF_1_HEIGHT_D_AFTER"].values)[1])
               self.textbox_dee1_a_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_THICKNESS_A_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee1_selected["RF_1_THICKNESS_A_AFTER"].values)[1])
               self.textbox_dee1_b_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_THICKNESS_B_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee1_selected["RF_1_THICKNESS_B_AFTER"].values)[1])
               self.textbox_dee1_c_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_THICKNESS_C_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee1_selected["RF_1_THICKNESS_C_AFTER"].values)[1])
               self.textbox_dee1_d_reference.setPlainText(np.array(self.df_rf_dee1_selected["RF_1_THICKNESS_D_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee1_selected["RF_1_THICKNESS_D_AFTER"].values)[1])
        else:
               self.textbox_dee1h_a_reference.setPlainText("0")
               self.textbox_dee1h_b_reference.setPlainText("0")
               self.textbox_dee1h_c_reference.setPlainText("0")
               self.textbox_dee1h_d_reference.setPlainText("0")
               self.textbox_dee1_a_reference.setPlainText("0")
               self.textbox_dee1_b_reference.setPlainText("0")
               self.textbox_dee1_c_reference.setPlainText("0")
               self.textbox_dee1_d_reference.setPlainText("0")
        

    def on_click_load_rf2(self):
        self.value_position_cyclotron = self.textbox_cyclotron_rf.text()
        self.value_date = self.textbox_date_rf.text()
        self.question_midplane =  QMessageBox()
        self.question_midplane.setText("Select an output folder to import RF Dee1 values")
        self.question_midplane.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_midplane.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_rf = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_rf_file = os.path.join(self.input_path_rf,"rf_dee2_values.out")
        self.df_rf_dee2_selected = tfs.read(self.input_path_rf_file)
        self.df_rf_dee2_selected = self.df_rf_dee2_selected[(self.df_rf_dee2_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_rf_dee2_selected["DATE"] == self.value_date)]
        print ("HEREEEE")
        print (self.input_path_rf_file)
        print (self.df_rf_dee2_selected)
        print (self.df_rf_dee2_selected["RF_2_HEIGHT_E_AFTER"])
        print ("VALUES")
        print (np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_E_AFTER"].values))
        print (len(np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_E_AFTER"].values)))
        if len(np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_E_AFTER"].values)) == 1:
               print ("first step")
               self.textbox_dee2h_e_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_E_AFTER"].values)[0])
               self.textbox_dee2h_f_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_F_AFTER"].values)[0])
               self.textbox_dee2h_g_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_G_AFTER"].values)[0])
               self.textbox_dee2h_h_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_H_AFTER"].values)[0])
               self.textbox_dee2_e_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_THICKNESS_E_AFTER"].values)[0])
               self.textbox_dee2_f_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_THICKNESS_F_AFTER"].values)[0])
               self.textbox_dee2_g_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_THICKNESS_G_AFTER"].values)[0])
               self.textbox_dee2_h_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_THICKNESS_H_AFTER"].values)[0])

        elif len(np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_E_AFTER"].values)) > 1:
               self.textbox_dee2h_e_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_E_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_E_AFTER"].values)[1])
               self.textbox_dee2h_f_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_F_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_F_AFTER"].values)[1])
               self.textbox_dee2h_g_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_G_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_G_AFTER"].values)[1])
               self.textbox_dee2h_h_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_H_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee2_selected["RF_2_HEIGHT_H_AFTER"].values)[1])
               self.textbox_dee2_e_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_THICKNESS_E_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee2_selected["RF_2_THICKNESS_E_AFTER"].values)[1])
               self.textbox_dee2_f_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_THICKNESS_F_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee2_selected["RF_2_THICKNESS_F_AFTER"].values)[1])
               self.textbox_dee2_g_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_THICKNESS_G_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee2_selected["RF_2_THICKNESS_G_AFTER"].values)[1])
               self.textbox_dee2_h_reference.setPlainText(np.array(self.df_rf_dee2_selected["RF_2_THICKNESS_H_AFTER"].values)[0] + "/" + np.array(self.df_rf_dee2_selected["RF_2_THICKNESS_H_AFTER"].values)[1])
        else:
               self.textbox_dee2h_e_reference.setPlainText("0")
               self.textbox_dee2h_f_reference.setPlainText("0")
               self.textbox_dee2h_g_reference.setPlainText("0")
               self.textbox_dee2h_h_reference.setPlainText("0")
               self.textbox_dee2_e_reference.setPlainText("0")
               self.textbox_dee2_f_reference.setPlainText("0")
               self.textbox_dee2_g_reference.setPlainText("0")
               self.textbox_dee2_h_reference.setPlainText("0")
        
    


    def on_click_central(self):
        self.value_position_location = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.value_position_source_a_after = self.textbox_centralregion_a_after.text()
        self.value_position_source_a_before = self.textbox_centralregion_a_before.text()
        self.value_position_source_b_before = self.textbox_centralregion_b_before.text()
        self.value_position_source_b_after = self.textbox_centralregion_b_after.text()
        self.value_position_source_c_before  = self.textbox_centralregion_c_before.text()
        self.value_position_source_c_after  = self.textbox_centralregion_c_after.text()
        self.value_position_source_d_before = self.textbox_centralregion_d_before.text()
        self.value_position_source_d_after = self.textbox_centralregion_d_after.text()
        #measurements_maintenance = ["CENTRAL_REGION_(A)_BEFORE ","CENTRAL_REGION_(B)_BEFORE", "CENTRAL_REGION_(C)_BEFORE","CENTRAL_REGION_(D)_BEFORE","CENTRAL_REGION_(A)_AFTER ","CENTRAL_REGION_(B)_AFTER", "CENTRAL_REGION_(C)_AFTER","CENTRAL_REGION_(D)_AFTER","CENTRAL_REGION_(A)_REFERENCE ","CENTRAL_REGION_(B)_REFERENCE", "CENTRAL_REGION_(C)_REFERENCE","CENTRAL_REGION_(D)_REFERENCE"]#,"DEE 1 (A)","DEE 1 (B)", "DEE 1 (C)","DEE 1 (D)","DEE 2 (E)", "DEE 2 (F)","DEE 2 (G)", "DEE 2 (H)","DEE 1 (A)","DEE 1 (B) W", "DEE 1 (C) W","DEE 1 (D) W","DEE 2 (E) W", "DEE 2 (F) W","DEE 2 (G) W", "DEE 2 (H) W"]
        central_values = [[self.value_position_location,self.value_date,self.value_position_source_a_before,self.value_position_source_b_before,self.value_position_source_c_before,self.value_position_source_d_before,self.value_position_source_a_after,self.value_position_source_b_after,self.value_position_source_c_after,self.value_position_source_d_after]]
        df_central_region_i = pd.DataFrame((central_values),columns=measurements_maintenance_central_region)
        print (df_central_region_i)
        print ("HEREEE")
        self.df_central_region = self.df_central_region.append(df_central_region_i,ignore_index=True)
        print (self.df_central_region)
        print ("LOCATION")
        print (self.value_position_location)
        print (self.value_date)
        self.question_central =  QMessageBox()
        self.question_central.setText("Select an output folder to import midplane values")
        self.question_central.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_central.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_central = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_central_file = os.path.join(self.output_path_central,"central_region_values.out")
        try: 
            self.df_central_region_old = tfs.read(self.output_path_central_file) 
            self.df_central_region_old = self.df_central_region_old.append(self.df_central_region,ignore_index=True)
            print (self.df_central_region_old)
            print ("HEREEEEEE ADDING A COLUMN")
            print (self.df_central_region)
            print (self.df_central_region_old)
            tfs.write(self.output_path_central_file, self.df_central_region_old) 
        except:
            tfs.write(self.output_path_central_file, self.df_central_region) 
    

    def on_click_beam_performance(self):
        self.value_position_cyclotron = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.value_dee_voltage = str(self.textbox_beam_dee_voltage.text())
        self.value_magnet_i = str(self.textbox_magnet_i.text())
        self.value_gas_flow = str(self.textbox_gas_flow.text())
        self.value_vacuum = str(self.textbox_vacuum.text())
        self.value_i_ion_source = str(self.textbox_i_ion_source.text())
        self.value_i_probe = str(self.textbox_i_probe.text())
        self.value_i_foil = str(self.textbox_i_foil.text())
        self.value_i_target = str(self.textbox_i_target.text())
        self.value_i_coll_low = str(self.textbox_i_coll_low.text())
        self.value_i_coll_up = str(self.textbox_i_coll_up.text())
        #measurements_beam_performance = ["CYCLOTRON","DATE","DEE_VOLTAGE","MAGNET_I","GAS_FLOW","VACUUM","I_ION_SOURCE","I_PROBE","I_FOIL","I_TARGET","I_COLL_LOW","I_COLL_UP"]
        central_values = [[self.value_position_cyclotron,self.value_date,self.value_dee_voltage,self.value_magnet_i,self.value_gas_flow,self.value_vacuum,
        self.value_i_ion_source,self.value_i_probe,self.value_i_foil,self.value_i_target,self.value_i_coll_low,self.value_i_coll_up]]
        df_beam_performance_i = pd.DataFrame((central_values),columns=measurements_beam_performance)
        print ("DF BEAM")
        print (df_beam_performance_i)
        print ("DATEEEEE")
        print (self.value_date)
        self.df_beam_performance = self.df_beam_performance.append(df_beam_performance_i,ignore_index=True)
        print (self.df_beam_performance)
        self.question_beam_performance =  QMessageBox()
        self.question_beam_performance.setText("Select an output folder to export source performance values")
        self.question_beam_performance.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_beam_performance.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_beam_performance = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_beam_performance_file = os.path.join(self.output_path_beam_performance,"beam_performance_values.out")
        try: 
            print ("FIRST HEREE")
            self.df_beam_performance_old = tfs.read(self.output_path_beam_performance_file) 
            self.df_beam_performance_old = self.df_beam_performance_old.append(self.df_beam_performance,ignore_index=True)
            print (self.df_beam_performance_old)
            print ("HEREEEEEE ADDING A COLUMN")
            print (self.df_beam_performance)
            print (self.df_beam_performance_old)
            tfs.write(self.output_path_beam_performance_file, self.df_beam_performance_old) 
            print ("HEREEEE")
        except:
            tfs.write(self.output_path_beam_performance_file, self.df_beam_performance) 
        #print (df_source_performance)


    def on_click_ratio_computation(self):
        self.value_position_cyclotron = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.value_dee_voltage = str(self.textbox_beam_dee_voltage.text())
        self.value_magnet_i = str(self.textbox_magnet_i.text())
        self.value_gas_flow = str(self.textbox_gas_flow.text())
        self.value_vacuum = str(self.textbox_vacuum.text())
        self.value_i_ion_source = str(self.textbox_i_ion_source.text())
        self.value_i_probe = str(self.textbox_i_probe.text())
        self.value_i_target = str(self.textbox_i_target.text())
        self.value_i_foil = str(self.textbox_i_foil.text())
        self.value_i_coll_low = str(self.textbox_i_coll_low.text())
        self.value_i_coll_up = str(self.textbox_i_coll_up.text())
        print (type(self.value_i_ion_source))
        print (float(self.value_i_ion_source))
        print (float(self.value_i_probe))
        self.textbox_probe_source.setPlainText(str(round(float(self.value_i_probe)/float(self.value_i_ion_source),2)))
        self.textbox_foil_probe.setPlainText(str(round(float(self.value_i_foil)/float(self.value_i_probe),2)))
        self.textbox_target_probe.setPlainText(str(round(float(self.value_i_target)/float(self.value_i_probe),2)))
        #print (df_source_performance)

    def on_click_ratio_computation_reference(self):
        self.value_position_cyclotron = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.value_dee_voltage = str(self.textbox_beam_dee_voltage_reference.toPlainText())
        self.value_magnet_i = str(self.textbox_magnet_i_reference.toPlainText())
        self.value_gas_flow = str(self.textbox_gas_flow_reference.toPlainText())
        self.value_vacuum = str(self.textbox_vacuum_reference.toPlainText())
        self.value_i_ion_source = str(self.textbox_i_ion_source_reference.toPlainText())
        self.value_i_probe = str(self.textbox_i_probe_reference.toPlainText())
        self.value_i_target = str(self.textbox_i_target_reference.toPlainText())
        self.value_i_foil = str(self.textbox_i_foil_reference.toPlainText())
        self.value_i_coll_low = str(self.textbox_i_coll_low_reference.toPlainText())
        self.value_i_coll_up = str(self.textbox_i_coll_up_reference.toPlainText())
        self.textbox_probe_source_reference.setPlainText(str(round(float(self.value_i_probe)/float(self.value_i_ion_source),2)))
        self.textbox_foil_probe_reference.setPlainText(str(round(float(self.value_i_foil)/float(self.value_i_probe),2)))
        self.textbox_target_probe_reference.setPlainText(str(round(float(self.value_i_target)/float(self.value_i_probe),2)))

    def on_click_source_performnance(self):
        self.value_position_cyclotron = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.value_position_current_0 = str(self.textbox_current_0.text())
        print (self.value_position_current_0)
        self.value_position_current_50 = str(self.textbox_current_50.text())
        self.value_position_current_100 = str(self.textbox_current_100.text())
        self.value_position_current_150 = str(self.textbox_current_150.text())
        self.value_position_current_200 = str(self.textbox_current_200.text())
        self.value_position_current_250 = str(self.textbox_current_250.text())
        self.value_position_current_300 = str(self.textbox_current_300.text())
        self.value_position_current_350 = str(self.textbox_current_350.text())
        self.value_position_current_400 = str(self.textbox_current_400.text())
        self.value_position_current_450 = str(self.textbox_current_450.text())
        self.value_position_current_500 = str(self.textbox_current_500.text())
        self.value_position_current_550 = str(self.textbox_current_550.text())
        self.value_position_current_600 = str(self.textbox_current_600.text())
        print (self.value_position_current_0)
        print (self.value_position_current_50)
        print (self.value_position_current_100)
        print (self.value_position_current_150)
        print (self.value_position_current_200)
        print (self.value_position_current_250)
        print ("DATE")
        print (self.value_date)
        #print (self.textbox_date.text())
        central_values = [[self.value_position_cyclotron,self.value_date,self.value_position_current_0,self.value_position_current_50,self.value_position_current_100,self.value_position_current_150,self.value_position_current_200,
        self.value_position_current_250,self.value_position_current_300,self.value_position_current_350,self.value_position_current_400,self.value_position_current_450,self.value_position_current_500,self.value_position_current_550,self.value_position_current_600]]
        print (central_values)
        df_source_performance_i = pd.DataFrame((central_values),columns=measurements_source_performance)
        self.df_source_performance = self.df_source_performance.append(df_source_performance_i,ignore_index=True)
        self.question_source_performance =  QMessageBox()
        self.question_source_performance.setText("Select an output folder to export source performance values")
        self.question_source_performance.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_source_performance.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_source_performance = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_source_performance_file = os.path.join(self.output_path_source_performance,"source_performance_values.out")
        try: 
           self.df_source_performance_old = tfs.read(self.output_path_source_performance_file) 
           self.df_source_performance_old = self.df_source_performance_old.append(self.df_source_performance,ignore_index=True)
           print (self.df_source_performance_old)
           print ("HEREEEEEE ADDING A COLUMN")
           print (self.df_source_performance)
           print (self.df_source_performance_old)
           tfs.write(self.output_path_source_performance_file, self.df_source_performance_old) 
           print ("ALSO HEREEE")
        except:
            tfs.write(self.output_path_source_performance_file, self.df_source_performance) 
        
        #except:
        #    tfs.write(self.output_path_source_performance_file, self.df_source_performance) 
        #print (df_source_performance)

    def on_click_flaps(self):
        self.question_rf_dee1 =  QMessageBox()
        self.question_rf_dee1.setText("Select an output folder to export source performance values")
        self.question_rf_dee1.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_rf_dee1.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_flaps = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_flaps = os.path.join(self.output_path_flaps,"flap_measurements.out")
        #self.output_path_rf_dee1_file_2 = os.path.join(self.output_path_rf_dee1,"rf_dee1_values_2.out")
        #thickness
        self.value_position_cyclotron = self.textbox_cyclotron_rf.text()
        self.value_date = self.textbox_date_rf.text()

        self.value_flap1_position_0 = str(self.textbox_flap1_position_0.text())
        self.value_flap2_position_0 = str(self.textbox_flap2_position_0.text())
        self.value_flap1_position_50 = str(self.textbox_flap1_position_0.text())
        self.value_flap2_position_50 = str(self.textbox_flap2_position_0.text())
        self.value_flap1_position_100  = str(self.textbox_flap1_position_0.text())
        self.value_flap2_position_100  = str(self.textbox_flap2_position_0.text())
        
        flap_positions = [[self.value_position_cyclotron,self.value_date,self.value_flap1_position_0,self.value_flap1_position_50,self.value_flap1_position_100,self.value_flap2_position_0,self.value_flap2_position_50,self.value_flap2_position_100]]
        self.df_flap_positions = pd.DataFrame((flap_positions),columns=measurements_rf_flaps)
        
        #self.df_rf_dee1 = self.df_rf_1.append(df_rf_dee1_i,ignore_index=True)
        try: 
           self.df_flap_positions_old = tfs.read(self.output_path_flaps) 
           self.df_flap_positions = self.df_rf_dee1_old.append(self.output_path_flaps,ignore_index=True)
           print (self.df_flap_positions_old)
           print (self.df_flap_positions)
           print (self.df_flap_positions.columns.values)
           print (len(self.df_flap_positions.columns.values))
           tfs.write(self.output_path_flaps, self.df_flap_positions) 
           print ("ALSO HEREEE")
        except:
            tfs.write(self.output_path_flaps, self.df_flap_positions) 

    def on_click_rf_dee1(self):
        self.question_rf_dee1 =  QMessageBox()
        self.question_rf_dee1.setText("Select an output folder to export source performance values")
        self.question_rf_dee1.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_rf_dee1.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_rf_dee1 = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_rf_dee1_file = os.path.join(self.output_path_rf_dee1,"rf_dee1_values.out")
        self.output_path_rf_dee1_file_2 = os.path.join(self.output_path_rf_dee1,"rf_dee1_values_2.out")
        #thickness
        self.value_position_cyclotron = self.textbox_cyclotron_rf.text()
        self.value_date = self.textbox_date_rf.text()
        self.value_dee1t_a_before = str(self.textbox_dee1_a_before.text())
        self.value_dee1t_a_after = str(self.textbox_dee1_a_after.text())
        self.value_dee1t_b_before = str(self.textbox_dee1_b_before.text())
        self.value_dee1t_b_after = str(self.textbox_dee1_b_after.text())
        self.value_dee1t_c_before  = str(self.textbox_dee1_c_before.text())
        self.value_dee1t_c_after  = str(self.textbox_dee1_c_after.text())
        self.value_dee1t_d_before = str(self.textbox_dee1_d_before.text())
        self.value_dee1t_d_after = str(self.textbox_dee1_d_after.text())
        #height 
        self.value_dee1h_a_before = str(self.textbox_dee1h_a_before.text())
        self.value_dee1h_a_after = str(self.textbox_dee1h_a_after.text())
        self.value_dee1h_b_before = str(self.textbox_dee1h_b_before.text())
        self.value_dee1h_b_after = str(self.textbox_dee1h_b_after.text())
        self.value_dee1h_c_before  = str(self.textbox_dee1h_c_before.text())
        self.value_dee1h_c_after  = str(self.textbox_dee1h_c_after.text())
        self.value_dee1h_d_before = str(self.textbox_dee1h_d_before.text())
        self.value_dee1h_d_after = str(self.textbox_dee1h_d_after.text())
        dee1_values = [[self.value_position_cyclotron,self.value_date,self.value_dee1h_a_before,self.value_dee1h_b_before,self.value_dee1h_c_before,self.value_dee1h_d_before,self.value_dee1h_a_after,self.value_dee1h_b_after,self.value_dee1h_c_after,self.value_dee1h_d_after,
        self.value_dee1t_a_before,self.value_dee1t_b_before,self.value_dee1t_c_before,self.value_dee1t_d_before,self.value_dee1t_a_after,self.value_dee1t_b_after,self.value_dee1t_c_after,self.value_dee1t_d_after]]
        #
        self.df_rf_dee1 = pd.DataFrame((dee1_values),columns=measurements_maintenance_rf_1)
        print (dee1_values)
        #self.df_rf_dee1 = self.df_rf_1.append(df_rf_dee1_i,ignore_index=True)
        try: 
           self.df_rf_dee1_old = tfs.read(self.output_path_rf_dee1_file) 
           self.df_rf_dee1 = self.df_rf_dee1_old.append(self.df_rf_dee1,ignore_index=True)
           print (self.df_rf_dee1_old)
           print (self.df_rf_dee1)
           print (self.df_rf_dee1.columns.values)
           print (len(self.df_rf_dee1.columns.values))
           tfs.write(self.output_path_rf_dee1_file, self.df_rf_dee1) 
           print ("ALSO HEREEE")
        except:
            tfs.write(self.output_path_rf_dee1_file, self.df_rf_dee1) 
        
        

    def on_click_rf_dee2(self):
        self.value_position_cyclotron = self.textbox_cyclotron_rf.text()
        self.value_date = self.textbox_date_rf.text()
        #thickness
        self.value_dee2t_e_before = str(self.textbox_dee2_e_before.text())
        self.value_dee2t_e_after = str(self.textbox_dee2_e_after.text())
        self.value_dee2t_f_before = str(self.textbox_dee2_f_before.text())
        self.value_dee2t_f_after = str(self.textbox_dee2_f_after.text())
        self.value_dee2t_g_before  = str(self.textbox_dee2_g_before.text())
        self.value_dee2t_g_after  = str(self.textbox_dee2_g_after.text())
        self.value_dee2t_h_before = str(self.textbox_dee2_h_before.text())
        self.value_dee2t_h_after = str(self.textbox_dee2_h_after.text())
        #height 
        self.value_dee2h_e_before = str(self.textbox_dee2h_e_before.text())
        self.value_dee2h_e_after = str(self.textbox_dee2h_e_after.text())
        self.value_dee2h_f_before = str(self.textbox_dee2h_f_before.text())
        self.value_dee2h_f_after = str(self.textbox_dee2h_f_after.text())
        self.value_dee2h_g_before  = str(self.textbox_dee2h_g_before.text())
        self.value_dee2h_g_after  = str(self.textbox_dee2h_g_after.text())
        self.value_dee2h_h_before = str(self.textbox_dee2h_h_before.text())
        self.value_dee2h_h_after = str(self.textbox_dee2h_h_after.text())
        dee2_values = [[self.value_position_cyclotron,self.value_date,self.value_dee2h_e_before,self.value_dee2h_f_before,self.value_dee2h_g_before,self.value_dee2h_h_before,self.value_dee2h_e_after,self.value_dee2h_f_after,self.value_dee2h_g_after,self.value_dee2h_h_after,
        self.value_dee2t_e_before,self.value_dee2t_f_before,self.value_dee2t_g_before,self.value_dee2t_h_before,self.value_dee2t_e_after,self.value_dee2t_f_after,self.value_dee2t_g_after,self.value_dee2t_h_after]]
        self.df_rf_dee2 = pd.DataFrame((dee2_values),columns=measurements_maintenance_rf_2)
        self.question_dee2 =  QMessageBox()
        self.question_dee2.setText("Select an output folder to export RF Dee2 values")
        self.question_dee2.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_dee2.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_rf_dee2 = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_rf_dee2_file = os.path.join(self.output_path_rf_dee2,"rf_dee2_values.out")
        try: 
           self.df_rf_dee2_old = tfs.read(self.output_path_rf_dee2_file) 
           self.df_rf_dee2 = self.df_rf_dee2_old.append(self.df_rf_dee2,ignore_index=True)
           tfs.write(self.output_path_rf_dee2_file, self.df_rf_dee2) 
           print ("ALSO HEREEE")
        except:
            tfs.write(self.output_path_rf_dee2_file, self.df_rf_dee2) 


    def on_click_collimator(self):
        self.value_position_cyclotron = self.textbox_cyclotron_collimators.text()
        self.value_date = self.textbox_date_collimators.text()
        #aperture
        self.value_coll1_aperture_before = str(self.textbox_coll1_aperture_before.text())
        self.value_coll2_aperture_before = str(self.textbox_coll2_aperture_before.text())
        self.value_coll1_aperture_after = str(self.textbox_coll1_aperture_after.text())
        self.value_coll2_aperture_after = str(self.textbox_coll2_aperture_after.text())
        #separation
        self.value_coll1_separation_before = str(self.textbox_coll1_separation_before.text())
        self.value_coll2_separation_before = str(self.textbox_coll2_separation_before.text())
        self.value_coll1_separation_after = str(self.textbox_coll1_separation_after.text())
        self.value_coll2_separation_after = str(self.textbox_coll2_separation_after.text())
        #impedance 
        self.value_coll1_l_impedance_before = str(self.textbox_icollimator1_l_before.text())
        self.value_coll1_u_impedance_before = str(self.textbox_icollimator1_u_before.text())
        self.value_coll2_l_impedance_before = str(self.textbox_icollimator2_l_before.text())
        self.value_coll2_u_impedance_before = str(self.textbox_icollimator2_u_before.text())
        self.value_coll1_l_impedance_after = str(self.textbox_icollimator1_l_after.text())
        self.value_coll1_u_impedance_after = str(self.textbox_icollimator1_u_after.text())
        self.value_coll2_l_impedance_after = str(self.textbox_icollimator2_l_after.text())
        self.value_coll2_u_impedance_after = str(self.textbox_icollimator2_u_after.text())

        collimators_values = [[self.value_position_cyclotron,self.value_date,self.value_coll1_aperture_before,self.value_coll2_aperture_before,self.value_coll1_separation_before,self.value_coll2_separation_before,self.value_coll1_l_impedance_before,
        self.value_coll1_u_impedance_before,self.value_coll2_l_impedance_before,self.value_coll2_u_impedance_before,self.value_coll1_aperture_after,self.value_coll2_aperture_after,self.value_coll1_separation_after,self.value_coll2_separation_after,self.value_coll1_l_impedance_after,
        self.value_coll1_u_impedance_after,self.value_coll2_l_impedance_after,self.value_coll2_u_impedance_after]]

        self.df_collimators = pd.DataFrame((collimators_values),columns=measurements_collimators_values)
        self.question_collimators =  QMessageBox()
        self.question_collimators.setText("Select an output folder to export RF Dee2 values")
        self.question_collimators.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_collimators.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_collimators = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_collimators_file = os.path.join(self.output_path_collimators,"collimators_values.out")
        try: 
           self.df_collimators_old = tfs.read(self.output_path_collimators_file) 
           self.df_collimators = self.df_collimators_old.append(self.df_collimators,ignore_index=True)
           tfs.write(self.output_path_collimators_file, self.df_collimators) 
           print ("ALSO HEREEE")
        except:
           tfs.write(self.output_path_collimators_file, self.df_collimators) 

    def on_click_motor(self):
        self.value_position_cyclotron = self.textbox_cyclotron_calibration.text()
        self.value_date = self.textbox_date_calibration.text()
        #flap 1/2
        self.value_calibration_flap1_before = str(self.textbox_motor_calibration_flap1_before.text())
        self.value_calibration_flap2_before = str(self.textbox_calibration_flap2_before.text())
        self.value_calibration_flap1_after = str(self.textbox_motor_calibration_flap1_after.text())
        self.value_calibration_flap2_after = str(self.textbox_calibration_flap2_after.text())
        #caroussel 1/2
        self.value_calibration_caroussel1_before = str(self.textbox_caroussel1_before.text())
        self.value_calibration_caroussel2_before = str(self.textbox_caroussel2_before.text())
        self.value_calibration_caroussel1_after = str(self.textbox_caroussel1_after.text())
        self.value_calibration_caroussel2_after = str(self.textbox_caroussel2_after.text())
        #balance
        self.value_calibration_balance_before = str(self.textbox_balance_before.text())
        self.value_calibration_balance_after = str(self.textbox_balance_after.text())

        motor_values = [[self.value_position_cyclotron,self.value_date,self.value_calibration_flap1_before,self.value_calibration_flap2_before,self.value_calibration_caroussel1_before,self.value_calibration_caroussel2_before,
        self.value_calibration_balance_before,self.value_calibration_flap1_after,self.value_calibration_flap2_after,
        self.value_calibration_caroussel1_after,self.value_calibration_caroussel2_after,self.value_calibration_balance_after]]

        self.df_motor = pd.DataFrame((motor_values),columns=measurements_motor_values)
        self.question_motor =  QMessageBox()
        self.question_motor.setText("Select an output folder to export motor values")
        self.question_motor.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_motor.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_motor = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_motor_file = os.path.join(self.output_path_motor,"motor_values.out")
        try: 
           self.df_motor_old = tfs.read(self.output_path_motor_file) 
           self.df_motor = self.df_motor_old.append(self.df_motor,ignore_index=True)
           tfs.write(self.output_path_motor_file, self.df_motor) 
           print ("ALSO HEREEE")
        except:
            tfs.write(self.output_path_motor_file, self.df_motor) 


    def on_click_coll(self):
        self.value_position_cyclotron = self.textbox_cyclotron_impedances.text()
        self.value_date = self.textbox_date_impedances.text()
        self.value_coll_1_aperture_before = self.textbox_coll1_aperture_before.text()
        self.value_coll_1_aperture_after = self.textbox_coll1_aperture_after.text()
        self.value_coll_1_aperture_reference = self.textbox_coll1_aperture_reference.text()
        self.value_coll_1_separation_before = self.textbox_coll1_separation_before.text()
        self.value_coll_1_separation_after = self.textbox_coll1_separation_after.text()
        self.value_coll_1_separation_reference = self.textbox_coll1_separation_reference.text()
        self.value_coll_2_aperture_before = self.textbox_coll2_aperture_before.text()
        self.value_coll_2_aperture_after = self.textbox_coll2_aperture_after.text()
        self.value_coll_2_aperture_reference = self.textbox_coll2_aperture_reference.text()
        self.value_coll_2_separation_before = self.textbox_coll2_separation_before.text()
        self.value_coll_2_separation_after = self.textbox_coll2_separation_after.text()
        self.value_coll_2_separation_reference = self.textbox_coll2_separation_reference.text()
        coll_values = [[self.value_position_cyclotron,self.value_date,self.value_coll_1_separation_before,self.value_coll_1_aperture_before,self.value_coll_2_separation_before,self.value_coll_2_aperture_before,self.value_coll_1_separation_after,self.value_coll_1_aperture_after,self.value_coll_2_separation_after,self.value_coll_2_aperture_after]]
        df_col_i = pd.DataFrame((coll_values),columns=measurements_maintenance_col)
        print (df_col_i)
        print ("HEREEE")
        self.df_coll = self.df_col.append(df_col_i,ignore_index=True)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_coll = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_coll_file = os.path.join(self.output_path_rf_dee2,"collimators_values.out")
        try: 
            self.df_df_coll_old = tfs.read(self.output_path_coll_file) 
            self.df_df_coll_old = self.df_rf1_old.append(self.df_coll,ignore_index=True)
            print ("HEREEEEEE ADDING A COLUMN")
            print (self.df_coll)
            print (self.df_coll_old)
            tfs.write(self.output_path_coll_file, self.df_coll_old) 
        except:
            tfs.write(self.output_path_coll_file, self.df_coll) 


    def on_click_impedance(self):
        self.value_position_cyclotron = self.textbox_cyclotron_calibration.text()
        self.value_date = self.textbox_date_calibration.text()
        #flap 1/2
        self.value_impedance_probe_before = str(self.textbox_iprobe_before.text())
        self.value_impedance_probe_after = str(self.textbox_iprobe_after.text())
        #caroussel 1/2
        self.value_impedance_caroussel1_before = str(self.textbox_icaroussel1_before.text())
        self.value_impedance_caroussel2_before = str(self.textbox_icaroussel2_before.text())
        self.value_impedance_caroussel1_after = str(self.textbox_icaroussel1_after.text())
        self.value_impedance_caroussel2_after = str(self.textbox_icaroussel2_after.text())
        #balance
        self.value_impedance_balance_before = str(self.textbox_ibalance_before.text())
        self.value_impedance_balance_after = str(self.textbox_ibalance_after.text())
        #target
        self.value_impedance_target1_before = str(self.textbox_iTarget1_before.text())
        self.value_impedance_target4_before = str(self.textbox_iTarget4_before.text())
        self.value_impedance_target1_after = str(self.textbox_iTarget1_after.text())
        self.value_impedance_target4_after = str(self.textbox_iTarget4_after.text())
 
        impedance_values = [[self.value_position_cyclotron,self.value_date,self.value_impedance_probe_before,self.value_impedance_target1_before,self.value_impedance_target4_before,self.value_impedance_caroussel1_before,self.value_impedance_caroussel2_before,
        self.value_impedance_balance_before,self.value_impedance_probe_after,self.value_impedance_target1_after,self.value_impedance_target4_after,self.value_impedance_caroussel1_after,self.value_impedance_caroussel2_after,self.value_impedance_balance_after]]
        self.df_impedance = pd.DataFrame((impedance_values),columns=measurements_impedance_values)
        self.question_impedance =  QMessageBox()
        self.question_impedance.setText("Select an output folder to export motor values")
        self.question_impedance.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_impedance.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_impedance = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_impedance_file = os.path.join(self.output_path_impedance,"impedance_values.out")
        try: 
           self.df_impedance_old = tfs.read(self.output_path_impedance_file) 
           self.df_impedance = self.df_impedance_old.append(self.df_impedance,ignore_index=True)
           tfs.write(self.output_path_impedance_file, self.df_impedance) 
           print ("ALSO HEREEE")
        except:
            tfs.write(self.output_path_impedance_file, self.df_impedance) 

    def on_click_midplane(self):
        self.value_position_cyclotron = self.textbox_cyclotron_rf.text()
        self.value_date = self.textbox_date_rf.text()
        self.value_midplane_actual_a = str(self.textbox_midplane_actual_a.toPlainText())
        self.value_midplane_actual_b = str(self.textbox_midplane_actual_b.toPlainText())
        self.value_midplane_actual_c = str(self.textbox_midplane_actual_c.toPlainText())
        self.value_midplane_actual_d = str(self.textbox_midplane_actual_d.toPlainText())
        self.value_midplane_actual_e = str(self.textbox_midplane_actual_e.toPlainText())
        self.value_midplane_actual_f = str(self.textbox_midplane_actual_f.toPlainText())
        self.value_midplane_actual_g = str(self.textbox_midplane_actual_g.toPlainText())
        self.value_midplane_actual_h = str(self.textbox_midplane_actual_h.toPlainText())
        self.value_midplane_variance_a = str(self.textbox_midplane_variance_a.toPlainText())
        self.value_midplane_variance_b = str(self.textbox_midplane_variance_b.toPlainText())
        self.value_midplane_variance_c = str(self.textbox_midplane_variance_c.toPlainText())
        self.value_midplane_variance_d = str(self.textbox_midplane_variance_d.toPlainText())
        self.value_midplane_variance_e = str(self.textbox_midplane_variance_e.toPlainText())
        self.value_midplane_variance_f = str(self.textbox_midplane_variance_f.toPlainText())
        self.value_midplane_variance_g = str(self.textbox_midplane_variance_g.toPlainText())
        self.value_midplane_variance_h = str(self.textbox_midplane_variance_h.toPlainText())
        midplane_values = [[self.value_position_cyclotron,self.value_date,self.value_midplane_actual_a,self.value_midplane_actual_b,self.value_midplane_actual_c,self.value_midplane_actual_d,self.value_midplane_actual_e,self.value_midplane_actual_f,self.value_midplane_actual_g,self.value_midplane_actual_h,
        self.value_midplane_variance_a,self.value_midplane_variance_b,self.value_midplane_variance_c,self.value_midplane_variance_d,self.value_midplane_variance_e,self.value_midplane_variance_f,self.value_midplane_variance_g,self.value_midplane_variance_h]]
        df_mid_plane_i = pd.DataFrame((midplane_values),columns=measurements_maintenance_midplane)
        print (df_mid_plane_i)
        print ("HEREEE")
        self.question_midplane =  QMessageBox()
        self.question_midplane.setText("Select an output folder to import midplane values")
        self.question_midplane.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_midplane.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path_midplane = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.output_path_midplane_file = os.path.join(self.output_path_midplane,"mid_plane_values.out")
        self.df_mid_plane = self.df_mid_plane.append(df_mid_plane_i,ignore_index=True)
        try: 
            self.df_df_midplane_old = tfs.read(self.output_path_midplane_file) 
            self.df_df_midplane_old = self.df_rf1_old.append(self.df_mid_plane,ignore_index=True)
            print ("HEREEEEEE ADDING A COLUMN")
            print (self.df_midplane)
            print (self.df_midplane_old)
            tfs.write(self.output_path_midplane_file, self.df_midplane_old) 
        except:
            tfs.write(self.output_path_midplane_file, self.df_mid_plane)    

    def compute_mid_plane_dee1(self):
        self.midplane_value_a_after = round(float(self.textbox_dee1h_a_after.text()) - float(self.textbox_dee1_a_after.text())/2,2)
        self.midplane_value_b_after = round(float(self.textbox_dee1h_b_after.text()) - float(self.textbox_dee1_b_after.text())/2,2) 
        self.midplane_value_c_after = round(float(self.textbox_dee1h_c_after.text()) - float(self.textbox_dee1_c_after.text())/2,2)
        self.midplane_value_d_after = round(float(self.textbox_dee1h_d_after.text()) - float(self.textbox_dee1_d_after.text())/2,2)
        self.variance_a = round(-float(self.textbox_midplane_theorical_a.toPlainText()) + float(self.midplane_value_a_after),2)
        self.variance_b = round(-float(self.textbox_midplane_theorical_b.toPlainText()) + float(self.midplane_value_b_after),2)
        self.variance_c = round(-float(self.textbox_midplane_theorical_c.toPlainText()) + float(self.midplane_value_c_after),2)
        self.variance_d = round(-float(self.textbox_midplane_theorical_d.toPlainText()) + float(self.midplane_value_d_after),2)
        midplane_values_dee1 = [[self.midplane_value_a_after,self.midplane_value_b_after,self.midplane_value_c_after,self.midplane_value_d_after]]
        self.df_mid_plane_dee_1_i = pd.DataFrame((midplane_values_dee1),columns=measurements_maintenance_midplane_dee1)
        self.df_mid_plane_dee1 = self.df_mid_plane_dee1.append(self.df_mid_plane_dee_1_i,ignore_index=True)
        self.textbox_midplane_actual_a.setPlainText(str(self.midplane_value_a_after))
        self.textbox_midplane_actual_b.setPlainText(str(self.midplane_value_b_after))
        self.textbox_midplane_actual_c.setPlainText(str(self.midplane_value_c_after))
        self.textbox_midplane_actual_d.setPlainText(str(self.midplane_value_d_after))
        self.textbox_midplane_variance_a.setPlainText(str(self.variance_a))
        self.textbox_midplane_variance_b.setPlainText(str(self.variance_b))
        self.textbox_midplane_variance_c.setPlainText(str(self.variance_c))
        self.textbox_midplane_variance_d.setPlainText(str(self.variance_d))

    def compute_mid_plane_dee2(self):
        self.midplane_value_e_after = round(float(self.textbox_dee2h_e_after.text()) - float(self.textbox_dee2_e_after.text())/2,2)
        self.midplane_value_f_after = round(float(self.textbox_dee2h_f_after.text()) - float(self.textbox_dee2_f_after.text())/2,2)
        self.midplane_value_g_after = round(float(self.textbox_dee2h_g_after.text()) - float(self.textbox_dee2_g_after.text())/2,2)
        self.midplane_value_h_after = round(float(self.textbox_dee2h_h_after.text()) - float(self.textbox_dee2_h_after.text())/2,2)
        self.variance_e = round(-float(self.textbox_midplane_theorical_e.toPlainText()) + float(self.midplane_value_e_after),2)
        self.variance_f = round(-float(self.textbox_midplane_theorical_f.toPlainText()) + float(self.midplane_value_f_after),2)
        self.variance_g = round(-float(self.textbox_midplane_theorical_g.toPlainText()) + float(self.midplane_value_g_after),2)
        self.variance_h = round(-float(self.textbox_midplane_theorical_h.toPlainText()) + float(self.midplane_value_h_after),2)
        midplane_values_dee2 = [[self.midplane_value_e_after,self.midplane_value_f_after,self.midplane_value_g_after,self.midplane_value_h_after]]
        self.df_mid_plane_dee_2_i = pd.DataFrame((midplane_values_dee2),columns=measurements_maintenance_midplane_dee2)
        self.df_mid_plane_dee2 = self.df_mid_plane_dee2.append(self.df_mid_plane_dee_2_i,ignore_index=True)
        self.textbox_midplane_actual_e.setPlainText(str(self.midplane_value_e_after))
        self.textbox_midplane_actual_f.setPlainText(str(self.midplane_value_f_after))
        self.textbox_midplane_actual_g.setPlainText(str(self.midplane_value_g_after))
        self.textbox_midplane_actual_h.setPlainText(str(self.midplane_value_h_after))
        self.textbox_midplane_variance_e.setPlainText(str(self.variance_e))
        self.textbox_midplane_variance_f.setPlainText(str(self.variance_f))
        self.textbox_midplane_variance_g.setPlainText(str(self.variance_g))
        self.textbox_midplane_variance_h.setPlainText(str(self.variance_h))

    def compute_mid_plane_dee1_ref(self):
        try:
            self.midplane_value_a_reference = round(float(self.textbox_dee1h_a_reference.toPlainText()) - float(self.textbox_dee1_a_reference.toPlainText())/2,2)
            self.midplane_value_b_reference = round(float(self.textbox_dee1h_b_reference.toPlainText()) - float(self.textbox_dee1_b_reference.toPlainText())/2,2) 
            self.midplane_value_c_reference = round(float(self.textbox_dee1h_c_reference.toPlainText()) - float(self.textbox_dee1_c_reference.toPlainText())/2,2) 
            self.midplane_value_d_reference = round(float(self.textbox_dee1h_d_reference.toPlainText()) - float(self.textbox_dee1_d_reference.toPlainText())/2,2)
        except:
            self.midplane_value_a_reference = round(float(self.textbox_dee1h_a_reference.toPlainText()[0]) - float(self.textbox_dee1_a_reference.toPlainText()[0])/2,2)
            self.midplane_value_b_reference = round(float(self.textbox_dee1h_b_reference.toPlainText()[0]) - float(self.textbox_dee1_b_reference.toPlainText()[0])/2,2) 
            self.midplane_value_c_reference = round(float(self.textbox_dee1h_c_reference.toPlainText()[0]) - float(self.textbox_dee1_c_reference.toPlainText()[0])/2,2) 
            self.midplane_value_d_reference = round(float(self.textbox_dee1h_d_reference.toPlainText()[0]) - float(self.textbox_dee1_d_reference.toPlainText()[0])/2,2)
        self.variance_a_reference = round(-float(self.textbox_midplane_theorical_a.toPlainText()) + float(self.midplane_value_a_reference),2)
        self.variance_b_reference = round(-float(self.textbox_midplane_theorical_b.toPlainText()) + float(self.midplane_value_b_reference),2)
        self.variance_c_reference = round(-float(self.textbox_midplane_theorical_c.toPlainText()) + float(self.midplane_value_c_reference),2)
        self.variance_d_reference = round(-float(self.textbox_midplane_theorical_d.toPlainText()) + float(self.midplane_value_d_reference),2)
        midplane_values_dee1 = [[self.midplane_value_a_reference,self.midplane_value_b_reference,self.midplane_value_c_reference,self.midplane_value_d_reference]]
        self.df_mid_plane_dee_1_i = pd.DataFrame((midplane_values_dee1),columns=measurements_maintenance_midplane_dee1)
        self.df_mid_plane_dee1_ref = self.df_mid_plane_dee1_ref.append(self.df_mid_plane_dee_1_i,ignore_index=True)
        self.textbox_midplane_reference_a.setPlainText(str(self.midplane_value_a_reference))
        self.textbox_midplane_reference_b.setPlainText(str(self.midplane_value_b_reference))
        self.textbox_midplane_reference_c.setPlainText(str(self.midplane_value_c_reference))
        self.textbox_midplane_reference_d.setPlainText(str(self.midplane_value_d_reference))
        self.textbox_midplane_vreference_a.setPlainText(str(self.variance_a_reference))
        self.textbox_midplane_vreference_b.setPlainText(str(self.variance_b_reference))
        self.textbox_midplane_vreference_c.setPlainText(str(self.variance_c_reference))
        self.textbox_midplane_vreference_d.setPlainText(str(self.variance_d_reference))

    def compute_mid_plane_dee2_ref(self):
        try:
            print ("HEREEEEEE")
            self.midplane_value_e_reference = round(float(self.textbox_dee2h_e_reference.toPlainText()) - float(self.textbox_dee2_e_reference.toPlainText())/2,2)
            self.midplane_value_f_reference = round(float(self.textbox_dee2h_f_reference.toPlainText()) - float(self.textbox_dee2_f_reference.toPlainText())/2,2) 
            self.midplane_value_g_reference = round(float(self.textbox_dee2h_g_reference.toPlainText()) - float(self.textbox_dee2_g_reference.toPlainText())/2,2) 
            self.midplane_value_h_reference = round(float(self.textbox_dee2h_h_reference.toPlainText()) - float(self.textbox_dee2_h_reference.toPlainText())/2,2)
        except:
            self.midplane_value_e_reference = round(float(self.textbox_dee2h_e_reference.toPlainText()[0]) - float(self.textbox_dee2_e_reference.toPlainText()[0])/2,2)
            self.midplane_value_f_reference = round(float(self.textbox_dee2h_f_reference.toPlainText()[0]) - float(self.textbox_dee2_f_reference.toPlainText()[0])/2,2) 
            self.midplane_value_g_reference = round(float(self.textbox_dee2h_g_reference.toPlainText()[0]) - float(self.textbox_dee2_g_reference.toPlainText()[0])/2,2) 
            self.midplane_value_h_reference = round(float(self.textbox_dee2h_h_reference.toPlainText()[0]) - float(self.textbox_dee2_h_reference.toPlainText()[0])/2,2)
        self.variance_e_reference = round(-float(self.textbox_midplane_theorical_e.toPlainText()) + float(self.midplane_value_e_reference),2)
        self.variance_f_reference = round(-float(self.textbox_midplane_theorical_f.toPlainText()) + float(self.midplane_value_f_reference),2)
        self.variance_g_reference = round(-float(self.textbox_midplane_theorical_g.toPlainText()) + float(self.midplane_value_g_reference),2)
        self.variance_h_reference = round(-float(self.textbox_midplane_theorical_h.toPlainText()) + float(self.midplane_value_h_reference),2)
        midplane_values_dee1 = [[self.midplane_value_a_reference,self.midplane_value_b_reference,self.midplane_value_c_reference,self.midplane_value_d_reference]]
        self.df_mid_plane_dee_1_i = pd.DataFrame((midplane_values_dee1),columns=measurements_maintenance_midplane_dee1)
        self.df_mid_plane_dee1_ref = self.df_mid_plane_dee1_ref.append(self.df_mid_plane_dee_1_i,ignore_index=True)
        self.textbox_midplane_reference_e.setPlainText(str(self.midplane_value_e_reference))
        self.textbox_midplane_reference_f.setPlainText(str(self.midplane_value_f_reference))
        self.textbox_midplane_reference_g.setPlainText(str(self.midplane_value_g_reference))
        self.textbox_midplane_reference_h.setPlainText(str(self.midplane_value_h_reference))
        self.textbox_midplane_vreference_e.setPlainText(str(self.variance_e_reference))
        self.textbox_midplane_vreference_f.setPlainText(str(self.variance_f_reference))
        self.textbox_midplane_vreference_g.setPlainText(str(self.variance_g_reference))
        self.textbox_midplane_vreference_h.setPlainText(str(self.variance_h_reference))


    def plot_rf_trendings_height(self):
        self.value_position_cyclotron = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.question_source_trends =  QMessageBox()
        self.question_source_trends.setText("Select an import folder to import RF parameters")
        self.question_source_trends.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_source_trends.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_source_trends = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_rf_dee1_trends_file = os.path.join(self.input_path_source_trends,"rf_dee1_values.out")
        self.input_path_rf_dee2_trends_file = os.path.join(self.input_path_source_trends,"rf_dee2_values.out")
        self.df_rf_dee1_trends_selected = tfs.read(self.input_path_rf_dee1_trends_file)
        self.df_rf_dee1_trends_selected_cyclotron = self.df_rf_dee1_trends_selected[(self.df_rf_dee1_trends_selected["CYCLOTRON"] == self.value_position_cyclotron)]
        self.df_rf_dee1_trends_selected_cyclotron['DATE'] = pd.to_datetime(self.df_rf_dee1_trends_selected_cyclotron.DATE,format="%Y/%m/%d")
        self.df_rf_dee1_trends_selected_cyclotron = self.df_rf_dee1_trends_selected_cyclotron.sort_values(by=['DATE'])
        #self.df_rf_dee1_trends_selected = self.df_rf_dee1_trends_selected[(self.df_rf_dee1_trends_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_source_trends_selected["DATE"] == self.value_date)]      
        #
        self.df_rf_dee2_trends_selected = tfs.read(self.input_path_rf_dee2_trends_file)
        self.df_rf_dee2_trends_selected_cyclotron = self.df_rf_dee2_trends_selected[(self.df_rf_dee2_trends_selected["CYCLOTRON"] == self.value_position_cyclotron)]
        self.df_rf_dee2_trends_selected_cyclotron['DATE'] = pd.to_datetime(self.df_rf_dee2_trends_selected_cyclotron.DATE)
        self.df_rf_dee2_trends_selected_cyclotron = self.df_rf_dee2_trends_selected_cyclotron.sort_values(by=['DATE'])
        #self.df_rf_dee2_trends_selected = self.df_source_performance_trends_selected[(self.df_rf_dee2_trends_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_rf_dee2_trends_selected["DATE"] == self.value_date)]      
        #
        #measurements_maintenance_central_region = ["CENTRAL_REGION_(A)_AFTER","CENTRAL_REGION_(B)_AFTER", "CENTRAL_REGION_(C)_AFTER","CENTRAL_REGION_(D)_AFTER"]#,"DEE 1 (A)","DEE 1 (B)", "DEE 1 (C)","DEE 1 (D)","DEE 2 (E)", "DEE 2 (F)","DEE 2 (G)", "DEE 2 (H)","DEE 1 (A)","DEE 1 (B) W", "DEE 1 (C) W","DEE 1 (D) W","DEE 2 (E) W", "DEE 2 (F) W","DEE 2 (G) W", "DEE 2 (H) W"]
        #measurements_source_performance = ["CYCLOTRON","DATE","CURRENT_0","CURRENT_50","CURRENT_100","CURRENT_150","CURRENT_200","CURRENT_250","CURRENT_300","CURRENT_350","CURRENT_400","CURRENT_450","CURRENT_500","CURRENT_550","CURRENT_600"]
        self.df_rf_dee1_trends_selected = self.df_rf_dee1_trends_selected.sort_values(by='DATE', ascending=False)
        print (self.df_rf_dee1_trends_selected.DATE)
        self.plot_trending_rf_height.axes.clear()
        self.plot_trending_rf_height.axes.set_ylabel(str(r"Variance [mm]"),fontsize=12)
        self.plot_trending_rf_height.axes.set_xlabel(str("Date"),fontsize=12)
        self.plot_trending_rf_height.axes.set_xticks(self.df_rf_dee1_trends_selected_cyclotron.DATE)
        self.plot_trending_rf_height.axes.set_xticklabels(self.df_rf_dee1_trends_selected_cyclotron.DATE, rotation=45)
        self.plot_trending_rf_height.axes.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        self.plot_trending_rf_height.axes.plot_date(self.df_rf_dee1_trends_selected_cyclotron.DATE,self.df_rf_dee1_trends_selected_cyclotron["RF_1_HEIGHT_A_AFTER"].astype(float) - self.df_rf_dee1_trends_selected_cyclotron["RF_1_THICKNESS_A_AFTER"].astype(float)/2 - 30 ,label="A",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_height.axes.plot_date(self.df_rf_dee1_trends_selected_cyclotron.DATE,self.df_rf_dee1_trends_selected_cyclotron["RF_1_HEIGHT_B_AFTER"].astype(float) - self.df_rf_dee1_trends_selected_cyclotron["RF_1_THICKNESS_B_AFTER"].astype(float)/2 - 58,label="B",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_height.axes.plot_date(self.df_rf_dee1_trends_selected_cyclotron.DATE,self.df_rf_dee1_trends_selected_cyclotron["RF_1_HEIGHT_C_AFTER"].astype(float) - self.df_rf_dee1_trends_selected_cyclotron["RF_1_THICKNESS_C_AFTER"].astype(float)/2 - 30,label="C",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_height.axes.plot_date(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee1_trends_selected_cyclotron["RF_1_HEIGHT_D_AFTER"].astype(float) - self.df_rf_dee1_trends_selected_cyclotron["RF_1_THICKNESS_D_AFTER"].astype(float)/2 - 30,label="D",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_height.axes.set_xlabel(str("Date"),fontsize=12)
        #self.plot_trending_rf_height.axes.set_aspect(aspect=120)
        self.plot_trending_rf_height.fig.savefig('rf_height_1.pdf',dpi=self.plot_trending_rf_height.fig.dpi)
        #ax.set_aspect(aspect=0.5)
        #forceAspect(self.plot_trending_rf_height.axes.set_aspect,aspect=2)
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_E_AFTER"].astype(float),label="E",picker=5,fmt="o")
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_F_AFTER"].astype(float),label="F",picker=5,fmt="o")
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_G_AFTER"].astype(float),label="G",picker=5,fmt="o")
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_H_AFTER"].astype(float),label="H",picker=5,fmt="o")
        self.plot_trending_rf_height.draw()
        self.plot_trending_rf_height.show()
        #self.plot_trending_rf_height.ax2.set_ylabel(r'Max I probe [$\mu$A]/I source [mA]',fontsize=10)  # we already handled the x-label with ax1
        max_value_list = []
        self.plot_trending_rf_thicknees.axes.set_ylabel(str(r"Variance [mm]"),fontsize=12)
        print ("HEREEEE DEVIATION")
        print (self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_E_AFTER"].astype(float) + self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_E_AFTER"].astype(float)/2 - 58)
        print (self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_E_AFTER"].astype(float)/2)
        print (self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_E_AFTER"].astype(float))
        self.plot_trending_rf_thicknees.axes.set_xlabel(str("Date"),fontsize=12)
        self.plot_trending_rf_thicknees.axes.clear()
        self.plot_trending_rf_thicknees.axes.set_ylabel(str(r"Variance [mm]"),fontsize=12)
        self.plot_trending_rf_thicknees.axes.set_xlabel(str("Date"),fontsize=12)
        self.plot_trending_rf_thicknees.axes.set_xticks(self.df_rf_dee1_trends_selected_cyclotron.DATE)
        self.plot_trending_rf_thicknees.axes.set_xticklabels(self.df_rf_dee1_trends_selected_cyclotron.DATE, rotation=45)
        self.plot_trending_rf_thicknees.axes.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee1_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_E_AFTER"].astype(float) - self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_E_AFTER"].astype(float)/2 - 58 ,label="E",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_F_AFTER"].astype(float) - self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_F_AFTER"].astype(float)/2 - 30 ,label="F",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_G_AFTER"].astype(float) - self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_G_AFTER"].astype(float)/2 - 58 ,label="G",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_H_AFTER"].astype(float) - self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_H_AFTER"].astype(float)/2 - 58 ,label="H",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_thicknees.axes.set_xlabel(str("Date"),fontsize=12)
        self.plot_trending_rf_thicknees.axes.tick_params(axis='both', which='major', labelsize=12)
        self.plot_trending_rf_thicknees.axes.legend(loc='best',ncol=2,fontsize=12)
        self.plot_trending_rf_thicknees.fig.savefig('rf_height_2.png')
     
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_E_AFTER"].astype(float),label="E",picker=5,fmt="o")
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_F_AFTER"].astype(float),label="F",picker=5,fmt="o")
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_G_AFTER"].astype(float),label="G",picker=5,fmt="o")
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_H_AFTER"].astype(float),label="H",picker=5,fmt="o")

        #self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_E_AFTER"].astype(float),label="E",picker=5,fmt="o")
        #self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_F_AFTER"].astype(float),label="F",picker=5,fmt="o")
        #self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_G_AFTER"].astype(float),label="G",picker=5,fmt="o")
        #self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_H_AFTER"].astype(float),label="H",picker=5,fmt="o")
        #self.plot_trending_rf_thicknees.ax2 = self.plot_trending_source.axes.twinx()  # instantiate a second axes that shares the same x-axis
        #self.plot_trending_rf_thicknees.ax2.tick_params(axis='y', labelcolor=color, labelsize=10)
        self.plot_trending_rf_height.axes.tick_params(axis='both', which='major', labelsize=12)
        self.plot_trending_rf_height.axes.legend(loc='best',ncol=2,fontsize=12)
        self.plot_trending_rf_height.fig.savefig('rf_height_2.png')
        self.plot_trending_rf_thicknees.draw()
        self.plot_trending_rf_thicknees.show()


    def plot_rf_trendings_thickness(self):
        self.value_position_cyclotron = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.question_source_trends =  QMessageBox()
        self.question_source_trends.setText("Select an import folder to import RF parameters")
        self.question_source_trends.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_source_trends.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_source_trends = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_rf_dee1_trends_file = os.path.join(self.input_path_source_trends,"rf_dee1_values.out")
        self.input_path_rf_dee2_trends_file = os.path.join(self.input_path_source_trends,"rf_dee2_values.out")
        self.df_rf_dee1_trends_selected = tfs.read(self.input_path_rf_dee1_trends_file)
        self.df_rf_dee1_trends_selected_cyclotron = self.df_rf_dee1_trends_selected[(self.df_rf_dee1_trends_selected["CYCLOTRON"] == self.value_position_cyclotron)]
        self.df_rf_dee1_trends_selected_cyclotron['DATE'] = pd.to_datetime(self.df_rf_dee1_trends_selected_cyclotron.DATE,format="%Y/%m/%d")
        self.df_rf_dee1_trends_selected_cyclotron = self.df_rf_dee1_trends_selected_cyclotron.sort_values(by=['DATE'])
        #self.df_rf_dee1_trends_selected = self.df_rf_dee1_trends_selected[(self.df_rf_dee1_trends_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_source_trends_selected["DATE"] == self.value_date)]      
        #
        self.df_rf_dee2_trends_selected = tfs.read(self.input_path_rf_dee2_trends_file)
        self.df_rf_dee2_trends_selected_cyclotron = self.df_rf_dee2_trends_selected[(self.df_rf_dee2_trends_selected["CYCLOTRON"] == self.value_position_cyclotron)]
        self.df_rf_dee2_trends_selected_cyclotron['DATE'] = pd.to_datetime(self.df_rf_dee2_trends_selected_cyclotron.DATE)
        self.df_rf_dee2_trends_selected_cyclotron = self.df_rf_dee2_trends_selected_cyclotron.sort_values(by=['DATE'])
        #self.df_rf_dee2_trends_selected = self.df_source_performance_trends_selected[(self.df_rf_dee2_trends_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_rf_dee2_trends_selected["DATE"] == self.value_date)]      
        #
        #measurements_maintenance_central_region = ["CENTRAL_REGION_(A)_AFTER","CENTRAL_REGION_(B)_AFTER", "CENTRAL_REGION_(C)_AFTER","CENTRAL_REGION_(D)_AFTER"]#,"DEE 1 (A)","DEE 1 (B)", "DEE 1 (C)","DEE 1 (D)","DEE 2 (E)", "DEE 2 (F)","DEE 2 (G)", "DEE 2 (H)","DEE 1 (A)","DEE 1 (B) W", "DEE 1 (C) W","DEE 1 (D) W","DEE 2 (E) W", "DEE 2 (F) W","DEE 2 (G) W", "DEE 2 (H) W"]
        #measurements_source_performance = ["CYCLOTRON","DATE","CURRENT_0","CURRENT_50","CURRENT_100","CURRENT_150","CURRENT_200","CURRENT_250","CURRENT_300","CURRENT_350","CURRENT_400","CURRENT_450","CURRENT_500","CURRENT_550","CURRENT_600"]
        self.df_rf_dee1_trends_selected = self.df_rf_dee1_trends_selected.sort_values(by='DATE', ascending=False)
        print (self.df_rf_dee1_trends_selected.DATE)
        self.plot_trending_rf_height.axes.clear()
        self.plot_trending_rf_height.axes.set_ylabel(str(r"Thickness [mm]"),fontsize=12)
        self.plot_trending_rf_height.axes.set_xlabel(str("Date"),fontsize=12)
        self.plot_trending_rf_height.axes.set_xticks(self.df_rf_dee1_trends_selected_cyclotron.DATE)
        self.plot_trending_rf_height.axes.set_xticklabels(self.df_rf_dee1_trends_selected_cyclotron.DATE, rotation=45)
        self.plot_trending_rf_height.axes.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        print (self.df_rf_dee1_trends_selected_cyclotron.columns)
        self.plot_trending_rf_height.axes.plot_date(self.df_rf_dee1_trends_selected_cyclotron.DATE,self.df_rf_dee1_trends_selected_cyclotron["RF_1_THICKNESS_A_AFTER"].astype(float),label="A",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_height.axes.plot_date(self.df_rf_dee1_trends_selected_cyclotron.DATE,self.df_rf_dee1_trends_selected_cyclotron["RF_1_THICKNESS_B_AFTER"].astype(float),label="B",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_height.axes.plot_date(self.df_rf_dee1_trends_selected_cyclotron.DATE,self.df_rf_dee1_trends_selected_cyclotron["RF_1_THICKNESS_C_AFTER"].astype(float),label="C",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_height.axes.plot_date(self.df_rf_dee1_trends_selected_cyclotron.DATE,self.df_rf_dee1_trends_selected_cyclotron["RF_1_THICKNESS_D_AFTER"].astype(float),label="D",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_height.axes.set_xlabel(str("Date"),fontsize=12)
        #self.plot_trending_rf_height.axes.set_aspect(aspect=120)
        self.plot_trending_rf_height.fig.savefig('rf_height_1.pdf',dpi=self.plot_trending_rf_height.fig.dpi)
        #ax.set_aspect(aspect=0.5)
        #forceAspect(self.plot_trending_rf_height.axes.set_aspect,aspect=2)
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_E_AFTER"].astype(float),label="E",picker=5,fmt="o")
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_F_AFTER"].astype(float),label="F",picker=5,fmt="o")
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_G_AFTER"].astype(float),label="G",picker=5,fmt="o")
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_H_AFTER"].astype(float),label="H",picker=5,fmt="o")
        self.plot_trending_rf_height.draw()
        self.plot_trending_rf_height.show()
        #self.plot_trending_rf_height.ax2.set_ylabel(r'Max I probe [$\mu$A]/I source [mA]',fontsize=10)  # we already handled the x-label with ax1
        max_value_list = []
        self.plot_trending_rf_thicknees.axes.set_ylabel(str(r"Height [mm]"),fontsize=12)
        print ("HEREEEE")
        print (self.df_rf_dee1_trends_selected_cyclotron["RF_1_THICKNESS_A_AFTER"])
        self.plot_trending_rf_thicknees.axes.set_xlabel(str("Date"),fontsize=12)
        self.plot_trending_rf_thicknees.axes.clear()
        self.plot_trending_rf_thicknees.axes.set_ylabel(str(r"Height [mm]"),fontsize=12)
        self.plot_trending_rf_thicknees.axes.set_xlabel(str("Date"),fontsize=12)
        self.plot_trending_rf_thicknees.axes.set_xticks(self.df_rf_dee1_trends_selected_cyclotron.DATE)
        self.plot_trending_rf_thicknees.axes.set_xticklabels(self.df_rf_dee1_trends_selected_cyclotron.DATE, rotation=45)
        self.plot_trending_rf_thicknees.axes.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_E_AFTER"].astype(float),label="E",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_F_AFTER"].astype(float),label="F",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_G_AFTER"].astype(float),label="G",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_H_AFTER"].astype(float),label="H",picker=5,fmt="o",linestyle="-")
        self.plot_trending_rf_thicknees.axes.set_xlabel(str("Date"),fontsize=12)
        self.plot_trending_rf_thicknees.axes.tick_params(axis='both', which='major', labelsize=12)
        self.plot_trending_rf_thicknees.axes.legend(loc='best',ncol=2,fontsize=12)
        self.plot_trending_rf_thicknees.fig.savefig('rf_height_2.png')
     
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_E_AFTER"].astype(float),label="E",picker=5,fmt="o")
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_F_AFTER"].astype(float),label="F",picker=5,fmt="o")
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_G_AFTER"].astype(float),label="G",picker=5,fmt="o")
        #self.plot_trending_rf_height.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_HEIGHT_H_AFTER"].astype(float),label="H",picker=5,fmt="o")

        #self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_E_AFTER"].astype(float),label="E",picker=5,fmt="o")
        #self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_F_AFTER"].astype(float),label="F",picker=5,fmt="o")
        #self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_G_AFTER"].astype(float),label="G",picker=5,fmt="o")
        #self.plot_trending_rf_thicknees.axes.errorbar(self.df_rf_dee2_trends_selected_cyclotron.DATE,self.df_rf_dee2_trends_selected_cyclotron["RF_2_THICKNESS_H_AFTER"].astype(float),label="H",picker=5,fmt="o")
        #self.plot_trending_rf_thicknees.ax2 = self.plot_trending_source.axes.twinx()  # instantiate a second axes that shares the same x-axis
        #self.plot_trending_rf_thicknees.ax2.tick_params(axis='y', labelcolor=color, labelsize=10)
        self.plot_trending_rf_height.axes.tick_params(axis='both', which='major', labelsize=12)
        self.plot_trending_rf_height.axes.legend(loc='best',ncol=2,fontsize=12)
        self.plot_trending_rf_height.fig.savefig('rf_height_2.png')
        self.plot_trending_rf_thicknees.draw()
        self.plot_trending_rf_thicknees.show()


    def plot_source_trendings(self):
        self.value_position_cyclotron = self.textbox_cyclotron_location.text()
        self.value_date = self.textbox_date_location.text()
        self.question_source_trends =  QMessageBox()
        self.question_source_trends.setText("Select an import folder to import Source parameters")
        self.question_source_trends.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_source_trends.setStandardButtons(QMessageBox.Save)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.input_path_source_trends = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.input_path_source_trends_file = os.path.join(self.input_path_source_trends,"central_region_values.out")
        self.input_path_source_performance_trends_file = os.path.join(self.input_path_source_trends,"source_performance_values.out")
        self.df_source_trends_selected = tfs.read(self.input_path_source_trends_file)
        print ("FIRST HERE")
        print (self.df_source_trends_selected)
        self.df_source_trends_selected_cyclotron = self.df_source_trends_selected[(self.df_source_trends_selected["CYCLOTRON"] == self.value_position_cyclotron)]
        self.df_source_trends_selected_cyclotron['DATE'] = pd.to_datetime(self.df_source_trends_selected_cyclotron.DATE)
        self.df_source_trends_selected_cyclotron = self.df_source_trends_selected_cyclotron.sort_values(by='DATE')
        print (self.df_source_trends_selected_cyclotron)
        self.df_source_trends_selected = self.df_source_trends_selected[(self.df_source_trends_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_source_trends_selected["DATE"] == self.value_date)]      
        #
        self.df_source_performance_trends_selected = tfs.read(self.input_path_source_performance_trends_file)
        print ("FIRST HEREEE")
        print (self.df_source_performance_trends_selected)
        print ("SECOND HEREEEE")
        print (self.value_position_cyclotron)
        print (self.df_source_performance_trends_selected[self.df_source_performance_trends_selected["CYCLOTRON"] == self.value_position_cyclotron])
        self.df_source_performance_trends_selected_cyclotron = self.df_source_performance_trends_selected[(self.df_source_performance_trends_selected["CYCLOTRON"] == self.value_position_cyclotron)]
        self.df_source_performance_trends_selected_cyclotron['DATE'] = pd.to_datetime(self.df_source_performance_trends_selected_cyclotron.DATE)
        self.df_source_performance_trends_selected = self.df_source_performance_trends_selected[(self.df_source_performance_trends_selected["CYCLOTRON"] == self.value_position_cyclotron) & (self.df_source_performance_trends_selected["DATE"] == self.value_date)]      
        #self.df_source_performance_trends_selected_cyclotron = self.df_source_performance_trends_selected_cyclotron.sort_values(by='DATE')
        #
    
        #measurements_maintenance_central_region = ["CENTRAL_REGION_(A)_AFTER","CENTRAL_REGION_(B)_AFTER", "CENTRAL_REGION_(C)_AFTER","CENTRAL_REGION_(D)_AFTER"]#,"DEE 1 (A)","DEE 1 (B)", "DEE 1 (C)","DEE 1 (D)","DEE 2 (E)", "DEE 2 (F)","DEE 2 (G)", "DEE 2 (H)","DEE 1 (A)","DEE 1 (B) W", "DEE 1 (C) W","DEE 1 (D) W","DEE 2 (E) W", "DEE 2 (F) W","DEE 2 (G) W", "DEE 2 (H) W"]
        #measurements_source_performance = ["CYCLOTRON","DATE","CURRENT_0","CURRENT_50","CURRENT_100","CURRENT_150","CURRENT_200","CURRENT_250","CURRENT_300","CURRENT_350","CURRENT_400","CURRENT_450","CURRENT_500","CURRENT_550","CURRENT_600"]
        self.plot_trending_source.axes.set_ylabel(str(r"Position wrt the puller [mm]"),fontsize=12)
        self.plot_trending_source.axes.set_xlabel(str("Date"),fontsize=12)
        #self.plot_trending_source.axes.axes.set_xticklabels(self.df_source_trends_selected_cyclotron.DATE, rotation=45)
        #self.plot_trending_source.axes.axes.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        print (self.df_source_trends_selected_cyclotron["CENTRAL_REGION_(A)_AFTER"])
        print (self.df_source_trends_selected_cyclotron["CENTRAL_REGION_(B)_AFTER"])
        print (self.df_source_trends_selected_cyclotron["CENTRAL_REGION_(C)_AFTER"])
        print (self.df_source_trends_selected_cyclotron["CENTRAL_REGION_(D)_AFTER"])
        self.plot_trending_source.axes.set_ylim([0.0,1.8])
        self.plot_trending_source.axes.set_xticks(self.df_source_trends_selected_cyclotron.DATE)
        self.plot_trending_source.axes.set_xticklabels(self.df_source_trends_selected_cyclotron.DATE, rotation=45)
        self.plot_trending_source.axes.errorbar(self.df_source_trends_selected_cyclotron.DATE,self.df_source_trends_selected_cyclotron["CENTRAL_REGION_(A)_AFTER"].astype(float),label="A",picker=5,fmt="o",linestyle="-")
        self.plot_trending_source.axes.errorbar(self.df_source_trends_selected_cyclotron.DATE,self.df_source_trends_selected_cyclotron["CENTRAL_REGION_(B)_AFTER"].astype(float),label="B",picker=5,fmt="o",linestyle="-")
        self.plot_trending_source.axes.errorbar(self.df_source_trends_selected_cyclotron.DATE,self.df_source_trends_selected_cyclotron["CENTRAL_REGION_(C)_AFTER"].astype(float),label="C",picker=5,fmt="o",linestyle="-")
        self.plot_trending_source.axes.errorbar(self.df_source_trends_selected_cyclotron.DATE,self.df_source_trends_selected_cyclotron["CENTRAL_REGION_(D)_AFTER"].astype(float),label="D",picker=5,fmt="o",linestyle="-")
        self.plot_trending_source.ax2 = self.plot_trending_source.axes.twinx()  # instantiate a second axes that shares the same x-axis
        color = 'black'
        #self.plot_trending_source.draw()
        self.plot_trending_source.show()
        self.plot_trending_source.ax2.set_ylabel(r'Max I probe [$\mu$A]/I source [mA]',fontsize=12) 
        #self.plot_trending_source.ax2.set_ylim([0.5,1.1]) # we already handled the x-label with ax1
        max_value_list = []
        print ("HEREEEEEEE")
        print (self.df_source_performance_trends_selected_cyclotron.columns.values)
        print (self.df_source_performance_trends_selected_cyclotron.CURRENT_50[0])
        print (self.df_source_performance_trends_selected_cyclotron.CURRENT_150[0])
        print (self.df_source_performance_trends_selected_cyclotron.CURRENT_200[0])
        print (self.df_source_performance_trends_selected_cyclotron.CURRENT_250[0])
        print (self.df_source_performance_trends_selected_cyclotron.CURRENT_300[0])
        print (self.df_source_performance_trends_selected_cyclotron.CURRENT_0[0])
        print (float(self.df_source_performance_trends_selected_cyclotron.CURRENT_600[0]))
        print (self.df_source_performance_trends_selected_cyclotron)
        for i in range(len(self.df_source_performance_trends_selected_cyclotron)):
            list_values = [float(self.df_source_performance_trends_selected_cyclotron.CURRENT_0[i]),float(self.df_source_performance_trends_selected_cyclotron.CURRENT_50[i]),float(self.df_source_performance_trends_selected_cyclotron.CURRENT_100[i])
            ,float(self.df_source_performance_trends_selected_cyclotron.CURRENT_150[i]),float(self.df_source_performance_trends_selected_cyclotron.CURRENT_200[i]),float(self.df_source_performance_trends_selected_cyclotron.CURRENT_250[i])
            ,float(self.df_source_performance_trends_selected_cyclotron.CURRENT_300[i]),float(self.df_source_performance_trends_selected_cyclotron.CURRENT_350[i])
            ,float(self.df_source_performance_trends_selected_cyclotron.CURRENT_400[i]),float(self.df_source_performance_trends_selected_cyclotron.CURRENT_450[i]),float(self.df_source_performance_trends_selected_cyclotron.CURRENT_500[i])
            ,float(self.df_source_performance_trends_selected_cyclotron.CURRENT_550[i]),float(self.df_source_performance_trends_selected_cyclotron.CURRENT_600[i])]
            print ("list values")
            print (list_values)
            max_value = np.max(list_values)
            print (max_value)
            max_value_index = list_values.index(max(list_values))
            print (max_value_index)
            source_current = (max_value_index)*50
            max_value_list.append(max_value/source_current)
        print ("MAXIMUM VALUE LIST")
        print (self.df_source_performance_trends_selected_cyclotron.DATE)
        print (max_value_list)
        self.plot_trending_source.ax2.errorbar((self.df_source_performance_trends_selected_cyclotron.DATE),max_value_list,label=r"I probe [$\mu$A]/I source [mA]",fmt="^",color="blue")
        self.plot_trending_source.ax2.tick_params(axis='y', labelcolor=color, labelsize=12)
        self.plot_trending_source.axes.tick_params(axis='y', labelcolor=color, labelsize=12)
        self.plot_trending_source.ax2.set_xticks(self.df_source_trends_selected_cyclotron.DATE)
        self.plot_trending_source.ax2.set_xticklabels(self.df_source_trends_selected_cyclotron.DATE, rotation=45)
        self.plot_trending_source.ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        self.plot_trending_source.axes.legend(loc=2,ncol=4,fontsize=12)
        self.plot_trending_source.ax2.legend(loc=1,ncol=1,fontsize=12)
        self.plot_trending_source.draw()
        self.plot_trending_source.show()


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




class Canvas_alternative(FigureCanvas):
    def __init__(self, width = 5, height = 5, dpi = 100, parent = None):
        self.fig, self.ax = plt.subplots()
        self.l0, = self.ax.plot(t, s0, visible=False, lw=2, color='k', label='2 Hz')
        self.l1, = self.ax.plot(t, s1, lw=2, color='r', label='4 Hz')
        self.l2, = self.ax.plot(t, s2, lw=2, color='g', label='6 Hz')
        plt.subplots_adjust(left=0.2)
        lines = [self.l0, self.l1, self.l2]
        rax = plt.axes([0.05, 0.4, 0.1, 0.15])
        labels = ["Time","Current"]
        check = CheckButtons(rax, labels, visibility)



class Canvas(FigureCanvas):

    def __init__(self, width = 5, height = 5, dpi = 100, parent = None):
        #fig, (ax1, ax2) = plt.subplots(nrows=2)
        self.fig, self.axes = plt.subplots(nrows=2,ncols=1,figsize=(width,height))
        self.fig.tight_layout(pad=3.0)
        plt.gcf().autofmt_xdate()
        self.axes[0].tick_params(labelsize=10)
        self.axes[1].tick_params(labelsize=10)
        #self.axes[2].tick_params(labelsize=10)
        plt.xticks(fontsize=10,rotation=90)
        plt.yticks(fontsize=10)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)


class Canvas_tab2(FigureCanvas):
    def __init__(self, width = 5, height = 5, dpi = 100, parent = None):
        self.fig, self.axes = plt.subplots(1, sharex=True,figsize=(width,height))
        self.fig.tight_layout(pad=3.0)
        plt.gcf().autofmt_xdate()
        self.axes.tick_params(labelsize=10)
        plt.xticks(fontsize=12,rotation=90)
        plt.yticks(fontsize=12)
        #self.axes[1].tick_params(labelsize=10)
        #self.axes[2].tick_params(labelsize=10)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)



if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()
