__author__ = 'Rolando.Morales'
# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from rv7 import *
import sys
from PyQt4.phonon import Phonon
import random
import time
import os
class vistarv(QMainWindow,Ui_MainWindow):
    def __init__(self,arg):
      super(vistarv,self).__init__()
      self.setupUi(self)
      icon = QtGui.QIcon()
      icon.addPixmap(QtGui.QPixmap(":/newPrefix/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
      self.setWindowIcon(icon)
      self.setStyleSheet("background: rgb(30,30, 30)")
      self.seekSlider.setMediaObject(self.videoPlayer.mediaObject())
      self.volumeSlider.setAudioOutput(self.videoPlayer.audioOutput())
      self.open.clicked.connect(self.Open)
      self.p2.clicked.connect(self.play_clicked)
      self.signal=SIGNAL('play')
      self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
      self.listWidget.connect(self.listWidget,QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.listItemRightClicked)
      self.setStyle(QStyleFactory.create('windowsvista'))
      self.connect(self,self.signal,self.FinishedVideo)
      self.p3.clicked.connect(self.stop_clicked)
      self.p6.clicked.connect(self.CambiarModo)
      self.listWidget.setHidden(True)
      self.listWidget.activated.connect(self.cambiarVactual)
      self.videoPlayer.finished.connect(self.FinishedVideo)
      self.videoPlayer.videoWidget().installEventFilter(self)
      self.videoPlayer.mediaObject().stateChanged.connect(self.state_changed)
      self.p5.clicked.connect(self.repNext)
      self.p4.clicked.connect(self.repPrev)
      self.p7.clicked.connect(self.clista)
      self.agregar.clicked.connect(self.agregarList)
      self.s1=QShortcut(self)
      self.s1.setKey(QKeySequence("Space"))
      self.s2=QShortcut(self)
      self.s2.setKey(QKeySequence("Enter"))
      self.s1.activated.connect(self.play_clicked)
      self.s2.activated.connect(self.fs)
      self.control=False
      self.listaReproduccion=QStringList()
      self.vactual=None
      self.modo=0
      self.formatosDisponibles=["mpg", "avi","mp4","mov","flv","wmv","3gp","mkv","rm","DivX","RealVideo","ogg","WebM","Xvid","vob","mp3","wav","rmv"]
      self.controlLista=0

      self.open.setToolTip("Nueva lista de reproduccion")
      self.agregar.setToolTip("Adicionar videos a la lista de reproduccion")
      self.p3.setToolTip("Parar")
      self.p4.setToolTip("Anterior")
      self.p5.setToolTip("Siguiente")
      self.p2.setToolTip("Reproducir")
      self.p6.setToolTip("Aleatorio apagado")
      self.arg=arg
      self.setAcceptDrops(True)
      self.cargarArgumentosOS()
      self.listWidget.setHidden(True)




    def clista(self):
       if self.controlLista==0:
        self.listWidget.setHidden(False)
        self.controlLista=1
       else:
        self.controlLista=0
        self.listWidget.setHidden(True)


    def dragEnterEvent(self, event):
       if event.mimeData().hasUrls:
             event.accept()
       else:
             event.ignore()
    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
         if event.mimeData().hasUrls:
           event.setDropAction(Qt.CopyAction)
           event.accept()
           urls=event.mimeData().urls()
           if len(urls)>1 and self.vactual!=None:
              for url in urls:
               formato=QString(url.toLocalFile()).split(".",-1)[-1]
               if self.formatosDisponibles.__contains__(formato):
                self.listaReproduccion.append(QString(url.toLocalFile()))
                self.addItems([QString(url.toLocalFile())])
           elif len(urls)>1 and self.vactual==None:
                for url in urls:
                    formato=QString(url.toLocalFile()).split(".",-1)[-1]
                    if self.formatosDisponibles.__contains__(formato):
                      self.listaReproduccion.append(QString(url.toLocalFile()))
                      self.addItems([QString(url.toLocalFile())])
                if len(self.listaReproduccion)>0:
                    self.vactual=0
                    self.listWidget.setItemSelected(self.listWidget.item(self.vactual),True)
                    self.videoPlayer.play(Phonon.MediaSource(self.listaReproduccion[self.vactual]))
           else:
                aux=len(self.listaReproduccion)
                for url in urls:
                  formato=QString(url.toLocalFile()).split(".",-1)[-1]
                  if self.formatosDisponibles.__contains__(formato):
                    self.listaReproduccion.append(QString(url.toLocalFile()))
                    self.addItems([QString(url.toLocalFile())])
                if len(self.listaReproduccion)>aux and self.vactual!=-1:
                  self.vactual=len(self.listaReproduccion)-1
                  self.listWidget.setItemSelected(self.listWidget.item(self.vactual),True)
                  self.videoPlayer.play(Phonon.MediaSource(QString(url.toLocalFile())))
            #self.emit(SIGNAL("dropped"), l)
         else:
            event.ignore()



    def cargarArgumentosOS(self):
        if len(self.arg)>1:
            filename=self.arg[len(self.arg)-1]
            formato=QString(filename).split(".",-1)[-1]

            if self.formatosDisponibles.__contains__(formato):
                self.listaReproduccion.append(QString(filename))
                self.addItems([QString(filename)])
                self.vactual=0
                self.videoPlayer.play(Phonon.MediaSource(self.listaReproduccion[self.vactual]))


    def CambiarModo(self):
        if self.modo==0:
         icon = QtGui.QIcon()
         icon.addPixmap(QtGui.QPixmap(":/newPrefix/aleatorio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
         self.p6.setIcon(icon)
         self.p6.setToolTip("Aleatorio encendido")

         self.modo=1
        elif self.modo==1:
         icon = QtGui.QIcon()
         icon.addPixmap(QtGui.QPixmap(":/newPrefix/repetir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
         self.p6.setIcon(icon)
         self.p6.setToolTip("Repetir")

         self.modo=2
        else:
         icon = QtGui.QIcon()
         icon.addPixmap(QtGui.QPixmap(":/newPrefix/notAleatorio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
         self.p6.setIcon(icon)
         self.modo=0
         self.p6.setToolTip("Aleatorio apagado")


    def FinishedVideo(self):
      if self.vactual==None:
          self.vactual=0

      if self.modo==0:
       if self.vactual+1<len(self.listaReproduccion):
         self.vactual=self.vactual+1
         self.videoPlayer.play(Phonon.MediaSource(self.listaReproduccion[self.vactual]))
         self.listWidget.setItemSelected(self.listWidget.item(self.vactual),True)
      elif self.modo==1:
          self.vactual = random.randint(0,len(self.listaReproduccion)-1)
          self.videoPlayer.play(Phonon.MediaSource(self.listaReproduccion[self.vactual]))
          self.listWidget.setItemSelected(self.listWidget.item(self.vactual),True)
      else:
          self.videoPlayer.play(Phonon.MediaSource(self.listaReproduccion[self.vactual]))
          self.listWidget.setItemSelected(self.listWidget.item(self.vactual),True)



    def cambiarVactual(self,item):
         self.vactual=item.row()
         self.videoPlayer.play(Phonon.MediaSource(self.listaReproduccion[item.row()]))

    def checkList(self):
        if self.checkBox.isChecked():
            self.listWidget.setHidden(False)
        else:
            self.listWidget.setHidden(True)

    def  repNext(self):
     if self.vactual!=None:
       if self.modo!=1:
        if self.vactual+1<len(self.listaReproduccion):
         self.vactual=self.vactual+1
         self.videoPlayer.play(Phonon.MediaSource(self.listaReproduccion[self.vactual]))
         self.listWidget.setItemSelected(self.listWidget.item(self.vactual),True)
       else:
         self.vactual = random.randint (0,len(self.listaReproduccion)-1)
         self.videoPlayer.play(Phonon.MediaSource(self.listaReproduccion[self.vactual]))
         self.listWidget.setItemSelected(self.listWidget.item(self.vactual),True)

    def  repPrev(self):
      if self.vactual!=None:
        if self.modo!=1:
         if self.vactual>0:
          self.vactual=self.vactual-1
          self.videoPlayer.play(Phonon.MediaSource(self.listaReproduccion[self.vactual]))
          self.listWidget.setItemSelected(self.listWidget.item(self.vactual),True)
        else:
          self.vactual = random.randint (0,len(self.listaReproduccion)-1)
          self.videoPlayer.play(Phonon.MediaSource(self.listaReproduccion[self.vactual]))
          self.listWidget.setItemSelected(self.listWidget.item(self.vactual),True)

    def play_clicked(self):
            if (self.videoPlayer.mediaObject().state() in
                (Phonon.PausedState, Phonon.StoppedState)):
                self.videoPlayer.play()
            else:
                self.videoPlayer.pause()

    def stop_clicked(self):
            self.videoPlayer.stop()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/newPrefix/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.p2.setIcon(icon)


    def state_changed(self, newstate, oldstate):
            states = {
                Phonon.PausedState: "Resumir",
                Phonon.PlayingState: "Pausa",
                Phonon.StoppedState: "Reproducir"

            }

            if newstate!=0 and newstate !=5:
             if states[newstate]=="Pausa":
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/newPrefix/st.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.p2.setIcon(icon)
                self.p2.setToolTip("Pausa")

             elif states[newstate]=="Resumir":
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/newPrefix/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.p2.setIcon(icon)
                self.p2.setToolTip("Resumir")
            else:
              self.p3.setEnabled(newstate != Phonon.StoppedState)

    def eventFilter(self, obj, event):
            if event.type() == QEvent.MouseButtonDblClick:
                obj.setFullScreen(not obj.isFullScreen())
            return False

    def fs(self):
     if self.control==False:
        self.showFullScreen()
        self.control=True
     else:
         self.showNormal()
         self.control=False



    def Open(self):
             self.vactual=None
             filename=""
             filenames = QFileDialog.getOpenFileNames(self, 'Abrir Videos', '', 'Videos (*.mpg *.avi *.mp4 *.mov *.flv *.wmv *.3gp *.mkv *.rm *.DivX *.RealVideo *.ogg *.WebM *.Xvid *.vob *.mp3 *.wav *.rmv)')
             if filenames!="":
                  self.vactual=0
                  self.listWidget.clear()
                  self.listaReproduccion=filenames
                  self.addItems(filenames)
                  self.listWidget.setItemSelected(self.listWidget.item(0),True)
                  self.videoPlayer.play(Phonon.MediaSource(self.listaReproduccion[self.vactual]))

    def agregarList(self):
         filenames = QFileDialog.getOpenFileNames(self, 'Adicionar Videos', '', 'Videos (*.mpg *.avi *.mp4 *.mov *.flv *.wmv *.3gp *.mkv *.rm *.DivX *.RealVideo *.ogg *.WebM *.Xvid *.vob *.mp3 *.wav *.rmv)')
         if filenames!="":
            for file in filenames:
                        self.listaReproduccion.append(file)
            self.addItems(filenames)
            if len(self.listaReproduccion)==len(filenames):
             self.vactual=0
             self.listWidget.setItemSelected(self.listWidget.item(0),True)
             self.videoPlayer.play(Phonon.MediaSource(self.listaReproduccion[self.vactual]))



    def listItemRightClicked(self, QPos):
     self.listMenu= QtGui.QMenu()
     menu_item = self.listMenu.addAction("Remover")
     icon5 = QtGui.QIcon()
     icon5.addPixmap(QPixmap(":/newPrefix/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
     menu_item.setIcon(icon5)
     self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.menuItemClicked)
     parentPosition = self.listWidget.mapToGlobal(QtCore.QPoint(0, 0))
     self.listMenu.move(parentPosition + QPos)
     self.listMenu.show()

    def menuItemClicked(self):
      model = self.listWidget.model()
      for i in range(0,len(self.listaReproduccion)):
         if i==self.listWidget.row(self.listWidget.currentItem()):
            if i>self.vactual:
             print(type(self.listaReproduccion))
             self.listaReproduccion.removeAt(i)
             model.removeRow(self.listWidget.indexFromItem(self.listWidget.currentItem()).row())
            elif i<self.vactual:
                self.vactual=self.vactual-1
                self.listaReproduccion.removeAt(i)
                model.removeRow(self.listWidget.indexFromItem(self.listWidget.currentItem()).row())


    def addItems(self,lista):
        icon = QtGui.QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/video2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        for elemento in lista:
            arr=elemento.split("\\",-1)
            if len(arr)==1:
                arr=elemento.split("/",-1)
            item=QListWidgetItem(arr[-1])
            item.setIcon(icon)
            self.listWidget.addItem(item)







if __name__ == "__main__":
        app = QApplication(sys.argv)
        arg=sys.argv
        windowa = vistarv(arg)
        windowa.show()
        sys.exit(app.exec_())