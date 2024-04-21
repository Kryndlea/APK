# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QCheckBox, QGraphicsItem

from algorithms import *
from draw import Draw
from draw import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1748, 1252)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(parent=self.centralwidget)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1748, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSimplify = QtWidgets.QMenu(parent=self.menubar)
        self.menuSimplify.setObjectName("menuSimplify")
        self.menuView = QtWidgets.QMenu(parent=self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionMinimum_bounding_rectangle = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/maer.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionMinimum_bounding_rectangle.setIcon(icon2)
        self.actionMinimum_bounding_rectangle.setObjectName("actionMinimum_bounding_rectangle")
        self.actionPCA = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icons/pca.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPCA.setIcon(icon3)
        self.actionPCA.setObjectName("actionPCA")
        self.actionLongestedge = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icons/longestedge.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionLongestedge.setIcon(icon4)
        self.actionLongestedge.setObjectName("actionLongestedge")
        self.actionWallAverage = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons/wa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWallAverage.setIcon(icon5)
        self.actionWallAverage.setObjectName("actionWallAverage")
        self.actionWeightedbisector = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/icons/weightedbisector.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWeightedbisector.setIcon(icon6)
        self.actionWeightedbisector.setObjectName("actionWeightedBisector")
        self.actionClear_results = QtGui.QAction(parent=MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/icons/clear_ch.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_results.setIcon(icon7)
        self.actionClear_results.setObjectName("actionClear_results")

        self.actionClear_all = QtGui.QAction(parent=MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/icons/clear_er.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear_all.setIcon(icon8)
        self.actionClear_all.setObjectName("actionClear_all")

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSimplify.addAction(self.actionMinimum_bounding_rectangle)
        self.menuSimplify.addAction(self.actionPCA)
        self.menuSimplify.addAction(self.actionLongestedge)
        self.menuSimplify.addAction(self.actionWallAverage)
        self.menuSimplify.addAction(self.actionWeightedbisector)
        self.menuView.addAction(self.actionClear_results)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionClear_all)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSimplify.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMinimum_bounding_rectangle)
        self.toolBar.addAction(self.actionPCA)
        self.toolBar.addAction(self.actionLongestedge)
        self.toolBar.addAction(self.actionWallAverage)
        self.toolBar.addAction(self.actionWeightedbisector)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear_results)
        self.toolBar.addAction(self.actionClear_all)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.actionOpen.triggered.connect(self.openClick)  # type: ignore
        self.actionMinimum_bounding_rectangle.triggered.connect(self.mbrClick)  # type: ignore
        self.actionPCA.triggered.connect(self.pcaClick)  # type: ignore
        self.actionLongestedge.triggered.connect(self.longest_edgeClick)  # type: ignore
        self.actionWallAverage.triggered.connect(self.wall_averageClick)  # type: ignore
        self.actionWeightedbisector.triggered.connect(self.weighted_bisectorClick)  # type: ignore
        self.actionClear_results.triggered.connect(self.clearResultsClick)  # type: ignore
        self.actionClear_all.triggered.connect(self.clearAllClick)  # type: ignore
        self.actionExit.triggered.connect(MainWindow.close)
        self.checkBox = QCheckBox("Calculate accuracy")
        self.checkBox.setChecked(True)
        self.checkBox.stateChanged.connect(self.changeStatusClick)
        self.toolBar.addWidget(self.checkBox)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openClick(self, filename):
        self.Canvas.loadData()
        self.Canvas.resizeData()

        # function to fit data to the widget

    def show_info_box(self, algorithm_name, accuracy):
        info_box = QMessageBox()
        info_box.setWindowTitle("Simplification accuracy")
        info_box.setInformativeText(f"Algorithm: {algorithm_name}\nAccuracy: {round(accuracy, 3)} %")
        info_box.setIcon(QMessageBox.Icon.Information)
        info_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        timer = QTimer()
        timer.timeout.connect(info_box.close)
        timer.setSingleShot(True)
        timer.start(10000) 
        info_box.exec()

    def changeStatusClick(self, state):
        if state == 0:
            self.Canvas.setVisible(False)
            print(self.Canvas.visible)
        else:
            self.Canvas.setVisible(True)

    def resizeDisplay(self):
        self.Canvas.resizeData()
        self.Canvas.repaint()


    def mbrClick(self):
        buildings = self.Canvas.getBuildings()
        maer_list = []
        a = Algorithms()
        for building in buildings:
            maer = a.createMBR(building)
            if maer is not None:
                maer_list.append(maer)
            else:
                warning_box = QMessageBox()
                warning_box.setText("Acknowledgement")
                warning_box.setIcon(QMessageBox.Icon.Warning)
                warning_box.setInformativeText(
                    f"Found empty geometry in buildings dataset, skipping...")
                warning_box.exec()
        n = len(maer_list)
        if self.Canvas.visible:
            signals = []
            for i in range(n):
                building = buildings[i]
                erp = maer_list[i]
                signal = a.calculate_accuracy(building, erp)
                signals.append(signal)
            accuracy_meth = (mean(signals)*100)
            algorithm_name = 'Minimum bounding rectangle.'
            self.show_info_box(algorithm_name=algorithm_name, accuracy=accuracy_meth)
        
        # update mbr
        self.Canvas.setMBR(maer_list)
        self.Canvas.repaint()

    def pcaClick(self):
        # Get building
        buildings = self.Canvas.getBuildings()
        erp_pca_list = []
        a = Algorithms()
        for building in buildings:
            erp_pca = a.createERPCA(building)
            if erp_pca is not None:
                erp_pca_list.append(erp_pca)
        n = len(erp_pca_list)
        if self.Canvas.visible:
            signals = []
            for i in range(n):
                building = buildings[i]
                erp = erp_pca_list[i]
                signal = a.calculate_accuracy(building, erp)
                signals.append(signal)
            accuracy_meth = (mean(signals)*100)
            algorithm_name = 'Principal Component Analysis'
            self.show_info_box(algorithm_name=algorithm_name, accuracy=accuracy_meth)


        # Update MBR
        self.Canvas.setMBR(erp_pca_list)
        # Repaint screen
        self.Canvas.repaint()

    def longest_edgeClick(self):
        # Get building
        buildings = self.Canvas.getBuildings()
        le_list = []
        a = Algorithms()
        for building in buildings:
            le = a.longestEdge(building)
            if le is not None:
                le_list.append(le)

        n = len(le_list)
        if self.Canvas.visible:
            signals = []
            for i in range(n):
                building = buildings[i]
                erp = le_list[i]
                signal = a.calculate_accuracy(building, erp)
                signals.append(signal)
            accuracy_meth = (mean(signals)*100)
            algorithm_name = 'Longest edge'
            self.show_info_box(algorithm_name=algorithm_name, accuracy=accuracy_meth)

        # Update MBR
        self.Canvas.setMBR(le_list)

        # Repaint screen
        self.Canvas.repaint()

    def wall_averageClick(self):
        # Get building
        buildings = self.Canvas.getBuildings()
        wa_list = []
        a = Algorithms()
        for building in buildings:
            wa = a.wallAverage(building)
            if wa is not None:
                wa_list.append(wa)
        
        n = len(wa_list)
        if self.Canvas.visible:
            signals = []
            for i in range(n):
                building = buildings[i]
                erp = wa_list[i]
                signal = a.calculate_accuracy(building, erp)
                signals.append(signal)
            accuracy_meth = (mean(signals)*100)
            algorithm_name = 'Wall average algortithm'
            self.show_info_box(algorithm_name=algorithm_name, accuracy=accuracy_meth)
        # Update MBR
        self.Canvas.setMBR(wa_list)

        # Repaint screen
        self.Canvas.repaint()

    def weighted_bisectorClick(self):
        # Get building
        buildings = self.Canvas.getBuildings()
        weigh_bisect_list = []
        a = Algorithms()
        for building in buildings:
            weigh_bis = a.weighted_bisector(building)
            if weigh_bis is not None:
                weigh_bisect_list.append(weigh_bis)
        
        n = len(weigh_bisect_list)
        for i in range(n):
            building = buildings[i]
            erp = weigh_bisect_list[i]
            a.calculate_accuracy(building, erp)
        
        n = len(weigh_bisect_list)
        if self.Canvas.visible:
            signals = []
            for i in range(n):
                building = buildings[i]
                erp = weigh_bisect_list[i]
                signal = a.calculate_accuracy(building, erp)
                signals.append(signal)
            accuracy_meth = (mean(signals)*100)
            algorithm_name = 'Weighted bisector algorithm.'
            self.show_info_box(algorithm_name=algorithm_name, accuracy=accuracy_meth)
        # Update MBR
        self.Canvas.setMBR(weigh_bisect_list)

        # Repaint screen
        self.Canvas.repaint()


    def clearResultsClick(self):
        self.Canvas.clearResults()
        self.Canvas.repaint()


    def clearAllClick(self):
        self.Canvas.clearData()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simplify buildings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSimplify.setTitle(_translate("MainWindow", "Simplify"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Close application"))
        self.actionMinimum_bounding_rectangle.setText(_translate("MainWindow", "Minimum bounding rectangle"))
        self.actionLongestedge.setText(_translate("MainWindow", "Longest edge algorithm"))
        self.actionWallAverage.setText(_translate("MainWindow", "Wall Average algorithm"))
        self.actionWeightedbisector.setText(_translate("MainWindow", "Weighted Bisector algorithm"))
        self.actionMinimum_bounding_rectangle.setToolTip(
            _translate("MainWindow", "Simplify using minimum bounding rectangle"))
        self.actionPCA.setText(_translate("MainWindow", "PCA"))
        self.actionPCA.setToolTip(_translate("MainWindow", "Simplify building using PCA"))
        self.actionLongestedge.setToolTip(_translate("MainWindow", "Simplify building using Longest edge algorithm"))
        self.actionWallAverage.setToolTip(_translate("MainWindow", "Simplify building using Wall Average algorithm"))
        self.actionWeightedbisector.setToolTip(_translate("MainWindow", "Simplify building using Weighted Bisector algorithm"))
        self.actionClear_results.setText(_translate("MainWindow", "Clear results"))
        self.actionClear_all.setText(_translate("MainWindow", "Clear all"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())