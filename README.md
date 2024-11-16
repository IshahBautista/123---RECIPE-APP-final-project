# 123 - Recipe App Final Project

## **README File**

### **Coding Conventions**

To ensure our code remains **readable** and easy to **modify**, let's follow these guidelines:

---

### **1. File Structure**

- Separate different UI screens into **individual files**.
- Each file can include both the **frontend** and **backend** components for that screen.
- Alternatively, you may choose to **separate the UI files from the backend files** for a cleaner structure.

---

### **2. Variable Naming**

- Use **descriptive variable names**.
- **Avoid** using single-letter variables or ambiguous abbreviations.

#### Examples:

- **DON'T**: `a`, `b`, `c`, `SOP`, `totPri`
- **DO**: `someValue1`, `some_Value2`, `SumOfPrices`, `totalPrice`

---

### **3. Adding Comments**

- If your logic is **complicated**, include comments to make it easier to understand.


---

### **4. Follow the Open/Closed Principle**

- Write code that is **open for extension** but **closed for modification**.
- Create **classes** for every major item with multiple variations (e.g., ingredients, recipes, filters).

---

### **5. Class Design**

- Use **private class variables** to avoid unintentional value changes.
- Provide **getter methods** to access private variables when needed.

#### Example:

```python
class Recipe:
    def __init__(self, something):
        self.__something = something  # Private variable

    def getSomething(self):
        return self.__something  # Getter method
```

---

### **6. Flet Layout**

- Try to format the flet layout code in a readable way by separating the arguments of an element into different lines with indentions

**DONT DO THIS:**
```python
page.add(ft.Column(controls=[
        ft.Row(controls=[ft.Text(value="a", color="green), ft.Text(value="B", color="red")], alignment=ft.MainAxisAlignment.CENTER)], ))
```

**INSTEAD DO:**
```python
page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value="A", color="green"),
                        ft.Text(value="B", color="red")
                    ], 
                    alignment=ft.MainAxisAlignment.CENTER)
            ], )
        )
```

Its the exact same code but the lower one is better and more readable.
