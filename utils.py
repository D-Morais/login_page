import bcrypt
from banco_de_dados import search_user, search_email, adc_user


def encrypt(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(password, password_hash):
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))


def create_user(user, password, email):
    exist_user = search_user(user)
    if exist_user:
        return f"Erro: O nome de usuário já está em uso.", "danger", user, "", email

    exist_email = search_email(email)
    if exist_email:
        return f"Erro: O nome de email já está em uso.", "danger", user, "", email

    adc_user(user, password, email)
    return f"Usuário adicionado com sucesso!", "success", "", "", ""
