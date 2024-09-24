
import sqlite3

def atualizar_contato():
    print("  ")
    visualizar_contato()
    print("  ")
    contato_id= input("Digite o ID do contato que deseja editar: ")

    conn= sqlite3.connect('teste.db')
    cursor= conn.cursor()

    cursor.execute('SELECT * FROM contatos WHERE id = ?', (contato_id,))
    contato= cursor.fetchone()

    if contato:
        print("  ")
        print(f"Editando contato; ID: {contato[0]}, Nome: {contato[1]}, Email: {contato[2]}, Telefone: {contato[3]}")
        novo_nome= input("Digite o novo nome (Ou deixe em branco para manter o atual): ")
        novo_email= input("Digite o novo email (Ou deixe em branco para manter o atual): ")
        novo_telefone=input("Digite o novo telefone (Ou deixe em branco para manter o atual): ")

        if novo_nome:
            cursor.execute('UPDATE contatos SET nome = ? WHERE id = ?', (novo_nome, contato_id))
        if novo_email:
            cursor.execute('UPDATE contatos SET email = ? WHERE id = ?', (novo_email, contato_id))
        if novo_telefone:
            cursor.execute('UPDATE contatos SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))

        conn.commit()
        conn.close()
        print("Contato editado com sucesso!")
    else:
        print("Contato não encontrado")
        conn.close()

def criar_tabela():
    conn = sqlite3.connect('teste.db')
    cursor= conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS contatos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT, telefone TEXT)''')

    conn.close()

def addcontato():
    nome= input("Digite o nome do contato: ")
    email= input("Digite o email do contato: ")
    telefone= input("Digite o telefone do contato: ")

    con= sqlite3.connect('teste.db')
    cursor= con.cursor()

    cursor.execute('''INSERT INTO contatos (nome, email, telefone) VALUES (?, ?, ?)''', (nome, email, telefone))

    con.commit()
    con.close()

    print("  ")
    print("Contato adicionado com sucesso!!")

def visualizar_contato():
    conn= sqlite3.connect('teste.db')
    cursor= conn.cursor()

    cursor.execute('SELECT * FROM contatos')
    print("  ")
    print("Contatos:")
    for row in cursor.fetchall():
        print(f"-ID: {row[0]}, Nome: {row[1]}, Email: {row[2]}, Telefone: {row[3]}")

    conn.close()

def excluir_contato():
    visualizar_contato()
    print("  ")
    contato_id = input("Digite a o ID do contato que deseja excluir: ")

    conn= sqlite3.connect('teste.db')
    cursor= conn.cursor()

    cursor.execute('DELETE FROM contatos WHERE id = ?', (contato_id,))

    conn.commit()
    conn.close()
    print("  ")
    print("Contato excluido com sucesso!")

criar_tabela()

while True:
    print("\nMenu:")
    print("1- Adiconar contato")
    print("2- Excluir contato")
    print("3- Editar contato")
    print("4- Visualizar contatos")
    print("5- Sair")
    print("  ")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        addcontato()
    elif opcao == "2":
        excluir_contato()
    elif opcao == "3":
        atualizar_contato()
    elif opcao == "4":
        visualizar_contato()
    elif opcao == "5":
        break
    else:
        print("Opção invalida.")