import sqlite3 as sql


def connect():
    return sql.connect("banco.db")


def init_db():
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE, 
        );
        """
    )
    conexao.commit()
    conexao.close()


def adc_user(name, password_user, email_user):
    conexao = connect()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """INSERT INTO users (username, password, email) VALUES (?, ?, ?)""", (name, password_user, email_user)
        )
        conexao.commit()
        return f"Usuário criado com sucesso."

    except sql.IntegrityError as er:
        conexao.rollback()
        return f"Erro: O nome de usuário ou email já está em uso. {er}"

    finally:
        conexao.close()


def update_user(name, new_password):
    conexao = connect()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """UPDATE users SET password = ? WHERE username = ?""", (new_password, name)
        )

        if cursor.rowcount == 0:
            conexao.rollback()
            return f"Erro: Usuário {name} não encontrado."
        else:
            conexao.commit()
            return f"Senha alterada com sucesso."

    except sql.Error as er:
        conexao.rollback()
        return f"Erro ao atualizar a senha {er}"

    finally:
        conexao.close()


def delete_user(name):
    conexao = connect()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """DELETE FROM users WHERE username = ?;""", (name, )
        )

        if cursor.rowcount == 0:
            conexao.rollback()
            return f"Erro: Usuário {name} não encontrado."
        else:
            conexao.commit()
            return f"Usuário removido com sucesso."

    except sql.Error as er:
        conexao.rollback()
        return f"Erro ao remover o usuário: {er}"

    finally:
        conexao.close()


def search_user(name):
    conexao = connect()
    cursor = conexao.cursor()

    cursor.execute(
        """SELECT username, password FROM users WHERE username = ?;""", (name, )
    )

    user = cursor.fetchone()
    conexao.close()

    return user


def list_users():
    conexao = connect()
    cursor = conexao.cursor()

    cursor.execute(
        """SELECT username, password, email FROM users;"""
    )

    users = cursor.fetchall()
    conexao.close()

    return users


if __name__ == '__main__':
    init_db()
