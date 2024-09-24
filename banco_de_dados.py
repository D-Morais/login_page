import sqlite3 as sql


def connect():
    return sql.connect("banco.db")


def init_db():
    conexao = connect()
    cursor = conexao.cursor()
    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS users (
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            created_at TEXT DEFAULT (DATE('now')),
            updated_at TEXT DEFAULT (DATE('now'))
        );
        """
    )

    cursor.execute(
        """
        CREATE TRIGGER IF NOT EXISTS update_date
        AFTER UPDATE ON users
        FOR EACH ROW
        BEGIN
            UPDATE users
            SET updated_at = DATE('now')
            WHERE id = OLD.id;
        END;
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


def update_password(name, new_password):
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
        """SELECT username FROM users WHERE username = ?;""", (name, )
    )

    user = cursor.fetchone()
    conexao.close()

    return user


def search_email(name_email):
    conexao = connect()
    cursor = conexao.cursor()

    cursor.execute(
        """SELECT email FROM users WHERE email = ?;""", (name_email, )
    )

    email = cursor.fetchone()
    conexao.close()

    return email


def verify_user(name):
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
