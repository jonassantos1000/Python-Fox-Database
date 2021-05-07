from tkinter import *
from tkinter import messagebox
import os
import os.path
from manuBase import manuBase



class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 60
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 0
        self.quintoContainer.pack()
        
        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Fox Database")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.baseLabel = Label(self.segundoContainer,text="Diretorio Base", font=self.fontePadrao)
        self.baseLabel.pack(side=LEFT)

        self.base = Entry(self.segundoContainer)
        self.base["width"] = 30
        self.base["font"] = self.fontePadrao
        self.base.pack(side=LEFT)
        
        self.firebird30 = Button(self.quartoContainer)
        self.firebird30["text"] = "Restore Base"
        self.firebird30["font"] = ("Arial", "8")
        self.firebird30["width"] = 20
        self.firebird30["command"] = self.restore
        self.firebird30.pack(side=LEFT)

        self.manu = Button(self.quintoContainer)
        self.manu["text"] = "Manutencao Base"
        self.manu["font"] = ("Arial", "8")
        self.manu["width"] = 20
        self.manu["command"] = self.manutencao
        self.manu.pack()        

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def manutencao(self):
        base = self.base.get()
        #pega o diretorio puro sem nome da base
        nomeBase='\ '+os.path.basename(base)
        nomeBase=nomeBase.replace(" ", "")
        diretorio=base.replace(nomeBase, "")
        if (os.path.exists(base)):
            
            res=messagebox.askyesno(title="Versão do Firebird", message="A base esta na versão 3.0 ?")
            if (res==True):
                manuBase.manutencao30(self)               
           
                if(os.path.exists(diretorio+"\Manutencao.FDB")):
                    messagebox.showinfo(title="Fox Database",message="Fim da manutenção, verifique o diretorio:\n\n"+ diretorio+ "\Manutencao.FDB")
                else:
                    erroManutencao=messagebox.askyesno(title="Fox Database",message="Não foi possivel realizar a manutenção utilizando o firebird 3.0.\n Gostaria de efetuar esse processo utilizando a versão 2.5 ?")
                    if(erroManutencao==True):
                        manuBase.manutencao25(self)
                        if(os.path.exists(diretorio+"\Manutencao.FDB")):
                            messagebox.showinfo(title="Fox Database",message="Manutenção efetuada utilizando a versão 2.5.\n Verifique o diretorio:\n\n"+ diretorio+ "\Manutencao.FDB")
                        else:
                            messagebox.showinfo(title="Fox Database",message="Também não foi possivel efetuar a manutenção utilizando a versão 2.5\n Verifique se a base informada não esta como backup.")
            else:
                manuBase.manutencao25(self)
                if(os.path.exists(diretorio+"\Manutencao.FDB")):
                    messagebox.showinfo(title="Fox Database",message="Fim da manutenção, verifique o diretorio:\n\n"+ diretorio+ "\Manutencao.FDB")
                else:
                    erroManutencao=messagebox.askyesno(title="Fox Database",message="Não foi possivel realizar a manutenção utilizando o firebird 2.5.\n Gostaria de efetuar esse processo utilizando a versão 3.0 ?")
                    if(erroManutencao==True):
                        manuBase.manutencao30(self)
                        if(os.path.exists(diretorio+"\Manutencao.FDB")):
                            messagebox.showinfo(title="Fox Database",message="Manutenção efetuada utilizando a versão 3.0.\n Verifique o diretorio:\n\n"+ diretorio+ "\Manutencao.FDB")
                        else:
                            messagebox.showinfo(title="Fox Database",message="Também não foi possivel efetuar a manutenção utilizando a versão 3.0\n Verifique se a base informada não esta como backup.")
        else:
            messagebox.showwarning(title="Fox Database",message="Diretorio de base invalido !!!")
           
    def restore(self):
        try:
            base = self.base.get()
            #pega o diretorio puro sem nome da base
            nomeBase='\ '+os.path.basename(base)
            nomeBase=nomeBase.replace(" ", "")
            diretorio=base.replace(nomeBase, "")    
            #comando para executar o gbak
            if (os.path.exists(base)):
                os.system('echo Processo Iniciado & "./Resources/30/gbak.exe" ' + '"'+ base +'"' + ' ' + diretorio + '\MILLENNIUMNOVA.FDB ' + ' ' +  '-user sysdba -pass masterkey -r -v -p 16384 -se service_mgr >  LogRestore.txt & echo Processo finalizado & @pause')
                if (os.path.exists(diretorio+'\MILLENNIUMNOVA.FDB')):
                    messagebox.showinfo(title="Fox Database",message="Comando executado!!!\n\nDiretorio: " + diretorio + "\n\nDiretorio: "+ diretorio+ "\MILLENNIUMNOVA.FDB")
                else:
                    os.system('echo Processo Iniciado & "./Resources/25/gbak.exe" ' + 'gbak ' + '"'+ base +'"' + ' ' + diretorio + '\MILLENNIUMNOVA.FDB ' + ' ' +  '-user sysdba -pass masterkey -r -v -p 16384 -se service_mgr  > LogRestore.txt& echo Processo finalizado @pause')
                    if(os.path.exists(diretorio+'\MILLENNIUMNOVA.FDB')):
                        messagebox.showinfo(title="Fox Database",message="Comando executado!!!\n\nDiretorio: " + diretorio + "\n\nDiretorio: "+ diretorio+ "\MILLENNIUMNOVA.FDB")
                    else:
                        messagebox.showwarning(title="Fox Database",message="Base de dados informada não esta no formato de Backup. \nPor favor, informe outro diretorio e tente novamente.")
            else:
                messagebox.showwarning(title="Fox Database",message="Diretorio de base invalido !!!")
        except:
            self.mensagem["text"] = "Erro na execução do programa"
                
root = Tk()
root.title("Fox Database - Desenvolvido por Jonas Santos")
Application(root)
root.mainloop()
