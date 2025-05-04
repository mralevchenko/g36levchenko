import json

class Contact:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def to_json(self):
        '''Серіалізація об'єкта Contact у JSON-рядок'''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

# Створення екземплярів
c1 = Contact("Lucy Smile", '7777', '1, Smile st.') 
c2 = Contact("Thomas Cook", '1123', '2, Cook avn.')

# Список контактів
contacts = [c1, c2]

# Серіалізація кожного об'єкта в JSON-рядок
contacts_serialized = [contact.to_json() for contact in contacts]

# Запис у файл
filename = "contact.json"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(contacts_serialized, f, indent=4)

print("Серіалізовано у файл:", contacts_serialized)

# Десеріалізація з файлу
with open(filename, 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)  # Це список рядків у JSON-форматі

# Перетворення кожного рядка назад у словник
result = [json.loads(item) for item in loaded_data]

print("Десеріалізовано з файлу:", result)

