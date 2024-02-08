from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79123456789"),
    Smartphone("Samsung", "Galaxy S21", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79345678901"),
    Smartphone("OnePlus", "9 Pro", "+79456789012"),
    Smartphone("Google", "Pixel 8", "+79567890123")
]

for phones in catalog:
    print(f"{phones.brand} - {phones.model}. {phones.number}")