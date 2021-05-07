from tkinter import *
from tkinter import messagebox
import os
import os.path
class manuBase():

    def manutencao30(self):
        if(os.path.exists("Controller.bat")):
            os.system("del Controller.bat")
        elif(os.path.exists("Controller.dll")):
            os.system("del Controller.dll")

                    
        base = self.base.get()
        #pega o diretorio puro sem nome da base
        nomeBase='\ '+os.path.basename(base)
        nomeBase=nomeBase.replace(" ", "")
        diretorio=base.replace(nomeBase, "")
        if (os.path.exists(base)):
            arquivo = open("Controller.bat", "w")
            arquivo.write('''
        @echo OFF
        del *.log /q 
        set ISC_USER=owner
        echo %time%
        if exist %2  del %2 /q
        "./Resources/30/gbak.exe" -z -b -user sysdba -pass masterkey -nod -g -l -v -st t -y Manutencao1.log %1 stdout | "./Resources/30/gbak.exe" -z -user sysdba -pass masterkey -c -v -st t -y Manutencao2.log stdin %2
        echo %time%''')
            arquivo.close()
            os.system('Controller.bat "'+base+'" ' + '"'+ diretorio + '\Manutencao.FDB"')
                     
            os.rename("Controller.bat", "Controller.dll")
            if(os.path.exists("Controller.bat")):
                os.system("del Controller.bat")
            elif(os.path.exists("Controller.dll")):
                os.system("del Controller.dll")        
        else:
            messagebox.showwarning(title="Fox Database",message="Diretorio de base invalido !!!")

    def manutencao25(self):
        if(os.path.exists("Controller.bat")):
            os.system("del Controller.bat")
        elif(os.path.exists("Controller.dll")):
            os.system("del Controller.dll")
                     
        base = self.base.get()
        #pega o diretorio puro sem nome da base
        nomeBase='\ '+os.path.basename(base)
        nomeBase=nomeBase.replace(" ", "")
        diretorio=base.replace(nomeBase, "")
        if (os.path.exists(base)):
                
            arquivo = open("Controller.bat", "w")
            arquivo.write('''
        @echo OFF
        del *.log /q 
        set ISC_USER=owner
        echo %time%
        if exist %2  del %2 /q
        "./Resources/25/gbak.exe" -z -b -user sysdba -pass masterkey -nod -g -l -v -st t -y Manutencao1.log %1 stdout | "./Resources/25/gbak.exe" -z -user sysdba -pass masterkey -c -v -st t -y Manutencao2.log stdin %2
        echo %time%''')
            arquivo.close()
            os.system('Controller.bat "'+base+'" ' + '"'+ diretorio + '\Manutencao.FDB"')
                     
            os.rename("Controller.bat", "Controller.dll")
            if(os.path.exists("Controller.bat")):
                os.system("del Controller.bat")
            elif(os.path.exists("Controller.dll")):
                os.system("del Controller.dll")  
        else:
             messagebox.showwarning(title="Fox Database",message="Diretorio de base invalido !!!")

