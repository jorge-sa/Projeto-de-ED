class Registro:
    def __init__(self, nome, phone, email):
        self.name = nome
        self.phone = phone
        self.email = email

    def show(self):
        print(f"Nome: {self.name}\nTelefone: {self.phone}\nE-Mail: {self.email}")