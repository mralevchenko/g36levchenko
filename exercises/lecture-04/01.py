class ContactManager:
    def __init__(self):
        self.contacts = []

    def is_valid_phone(self, phone):
        return phone.isdigit() and len(phone) == 12

    def is_unique_phone(self, phone):
        return all(contact["phone"] != phone for contact in self.contacts)

    def is_unique_name(self, full_name):
        return all(contact["full_name"] != full_name for contact in self.contacts)

    def add_contact(self, full_name, phone, email):
        # Перевірка заповнення всіх полів
        if not full_name or not phone or not email:
            print("Усі поля обов'язкові для заповнення.")
            return

        # Перевірка телефону
        if not self.is_valid_phone(phone):
            print("Номер телефону має бути числом довжиною 12.")
            return

        if not self.is_unique_phone(phone):
            print("Такий номер телефону вже існує.")
            return

        # Перевірка унікальності імені
        if not self.is_unique_name(full_name):
            print("Контакт з таким ім'ям вже існує.")
            return

        # Додавання контакту
        contact = {
            "full_name": full_name,
            "phone": phone,
            "email": email
        }
        self.contacts.append(contact)
        print("Контакт успішно додано.")

    def clear_contacts(self):
        self.contacts.clear()
        print("Список контактів очищено.")

    def list_contacts(self):
        for contact in self.contacts:
            print(contact)
