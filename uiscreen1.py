# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\uiscreen1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_header(object):
    def setupUi(self, main_header):
        main_header.setObjectName("main_header")
        main_header.resize(666, 638)
        main_header.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(main_header)
        self.centralwidget.setObjectName("centralwidget")
        self.download_audiobooks = QtWidgets.QPushButton(self.centralwidget)
        self.download_audiobooks.setGeometry(QtCore.QRect(290, 210, 151, 31))
        self.download_audiobooks.setObjectName("download_audiobooks")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 611, 121))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, -40, 131, 171))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(310, 390, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(300, 420, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(150, 530, 431, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 500, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.download_audiobooks_2 = QtWidgets.QPushButton(self.centralwidget)
        self.download_audiobooks_2.setGeometry(QtCore.QRect(290, 250, 151, 31))
        self.download_audiobooks_2.setObjectName("download_audiobooks_2")
        self.download_audiobooks_3 = QtWidgets.QPushButton(self.centralwidget)
        self.download_audiobooks_3.setGeometry(QtCore.QRect(290, 310, 151, 31))
        self.download_audiobooks_3.setObjectName("download_audiobooks_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(310, 300, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(170, 150, 351, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 410, 61, 41))
        self.label_5.setObjectName("label_5")
        self.download_audiobooks_4 = QtWidgets.QPushButton(self.centralwidget)
        self.download_audiobooks_4.setGeometry(QtCore.QRect(30, 390, 121, 31))
        self.download_audiobooks_4.setObjectName("download_audiobooks_4")
        self.download_audiobooks_5 = QtWidgets.QPushButton(self.centralwidget)
        self.download_audiobooks_5.setGeometry(QtCore.QRect(30, 430, 121, 31))
        self.download_audiobooks_5.setObjectName("download_audiobooks_5")
        main_header.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_header)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 21))
        self.menubar.setObjectName("menubar")
        main_header.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_header)
        self.statusbar.setObjectName("statusbar")
        main_header.setStatusBar(self.statusbar)

        self.retranslateUi(main_header)
        QtCore.QMetaObject.connectSlotsByName(main_header)

    def retranslateUi(self, main_header):
        _translate = QtCore.QCoreApplication.translate
        main_header.setWindowTitle(_translate("main_header", "MainWindow"))
        self.download_audiobooks.setText(
            _translate("main_header", "Download AudioBooks"))
        self.label.setText(_translate(
            "main_header", "Export and Transcribe your Audible Bookmarks!"))
        self.label_2.setText(_translate(
            "main_header", "<html><head/><body><p><img src='sound.png'/></p></body></html>"))
        self.textBrowser.setHtml(_translate("main_header", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Note</span> that this project does NOT \'crack\' any DRM. It simplys allows the user to use their own encryption key (fetched from Audible servers) to decrypt the audiobook in the same manner that the official audiobook playing software does. Please only use this application for gaining full access to your own audiobooks for archiving/conversion/convenience. DeDRMed audiobooks should not be uploaded to open servers, torrents, or other methods of mass distribution. No help will be given to people doing such things. Authors, retailers, and publishers all need to make a living, so that they can continue to produce audiobooks for us to hear, and enjoy. Don\'t be a parasite. This message is borrowed from the https://apprenticealf.wordpress.com/ page. </p></body></html>"))
        self.label_3.setText(_translate("main_header", "Legal Disclaimer"))
        self.download_audiobooks_2.setText(
            _translate("main_header", "Transcribe Bookmarks"))
        self.download_audiobooks_3.setText(
            _translate("main_header", "Perform All Operations"))
        self.textBrowser_2.setHtml(_translate("main_header", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Downloading Audiobooks may take longer, so it is recommended to download them before transcribing bookmarks</p></body></html>"))
        self.label_5.setText(_translate("main_header", "TextLabel"))
        self.download_audiobooks_4.setText(
            _translate("main_header", "Export to Excel (.csv)"))
        self.download_audiobooks_5.setText(
            _translate("main_header", "Export to Notion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_header = QtWidgets.QMainWindow()
    ui = Ui_main_header()
    ui.setupUi(main_header)
    main_header.show()
    sys.exit(app.exec_())
