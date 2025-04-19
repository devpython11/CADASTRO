from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
import customtkinter as ctk

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind = db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column("id", Integer, primary_key = True, autoincrement = True)
    email = Column("email", String)
    senha = Column("senha", String)
    
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        
def pegar():
    valor_email = email.get()
    valor_senha = senha.get()
    usuario = Usuario(email = valor_email, senha = valor_senha)
    session.add(usuario)
    session.commit()

def n_janela():
    most_email = ctk.CTkLabel(janela, text = email.get())
    most_email.pack(padx = 10, pady = 10)
    
    most_senha = ctk.CTkLabel(janela, text = senha.get())
    most_senha.pack(padx = 10, pady = 10)

def butao():
    pegar()
    n_janela()
    

Base.metadata.create_all(bind = db)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("500x300")

texto = ctk.CTkLabel(janela, text = "Fazer Login")
texto.pack(padx = 10, pady = 10)

email = ctk.CTkEntry(janela, placeholder_text = "Seu e-mail")
email.pack(padx = 10, pady = 10)

senha = ctk.CTkEntry(janela, placeholder_text = "Sua senha")
senha.pack(padx = 10, pady = 10)

botao = ctk.CTkButton(janela, text = "adicionar ao banco de dados", command = butao)
botao.pack(padx = 10, pady = 10)

janela.mainloop()

