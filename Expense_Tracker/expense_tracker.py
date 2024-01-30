class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.categories = {}

    def add_expense(self, date, amount, category):
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append((date, amount))

    def add_category(self, category):
        if category not in self.categories:
            self.categories[category] = 0

    def view_expenses(self):
        for category, items in self.expenses.items():
            total_amount = sum(amount for _, amount in items)
            print(f"{category}: ${total_amount}")

    def view_categories(self):
        print("Categories:")
        for category in self.expenses.keys():
            print(category)

# Sample usage
tracker = ExpenseTracker()

while True:
    print("\nGider Takip Menüsü :")
    print("1. Gider Ekle")
    print("2. Kategori Ekle")
    print("3. Giderleri Gör")
    print("4. Kategorileri Gör")
    print("5. Çık")

    choice = input("Seçimini Gir: ")

    if choice == "1":
        date = input("Tarih Gir (YYYY-MM-DD): ")
        amount = float(input("Tutar Gir: $"))
        category = input("Kategori Gir: ")
        tracker.add_expense(date, amount, category)
    elif choice == "2":
        category = input("Kategori Gir: ")
        tracker.add_category(category)
    elif choice == "3":
        tracker.view_expenses()
    elif choice == "4":
        tracker.view_categories()
    elif choice == "5":
        print("Gider Takibinden Çıkılıyor")
        break
    else:
        print("Geçersiz Seçim Tekrar Girin.")
