
# 🛒 Python OOP Activity: Grocery App

## 📌 Objective

You are responsible for building a **Grocery Management App** using Python.
The app will allow users to create and manage multiple shopping lists and grocery items using object-oriented programming principles.

---

## 🎯 Requirements

Your program must:

* Prompt the user for input.
* Allow the user to create multiple shopping lists.
* Allow the user to add grocery items to a specific shopping list.
* Allow the user to display all shopping lists and their items.

---

## 🏬 Shopping List

A **Shopping List** represents a store or location.

Each shopping list must include:

* **Title** (Store Name)
* **Address**

### Example Shopping Lists:

* Fiesta
* Walmart
* Sams Club
* Costco
* Randalls

A user should be able to create multiple shopping lists.

---

## 🥛 Grocery Item

A **Grocery Item** belongs to a shopping list.

Each grocery item must include:

* **Title**
* **Price**
* **Quantity**

### Example Grocery Items:

* Milk
* Cookies
* Paper
* Napkins
* Soda
* Chips
* Chicken
* Eggs

---

## 🧾 Example Output Structure

```
Fiesta
- Milk
- Soda
- Fish

Walmart
- Paper
- Napkins
- Plates
- Chips

Sams Club
- Chicken
- Beef
- Eggs
- Sugar
- Salt
- Pepper
- Honey
```

---

## 🧱 Required Classes

You must create at least the following classes:

### 1️⃣ GroceryList (or ShoppingList)

Responsible for:

* Storing title
* Storing address
* Holding a collection of grocery items
* Adding grocery items
* Displaying grocery items

---

### 2️⃣ GroceryItem

Responsible for:

* Storing title
* Storing price
* Storing quantity

---

## 🖥️ Program Flow

Your program should allow the user to:

1. Create a shopping list
2. Add a grocery item to a specific shopping list
3. Display all shopping lists
4. Exit the application

You may implement this using a menu system such as:

```
1. Create Shopping List
2. Add Grocery Item
3. Display Lists
4. Exit
```

---

## 💡 Design Expectations

* Use classes and objects properly.
* Keep responsibilities separated.
* Store multiple shopping lists in a collection.
* Each shopping list should manage its own grocery items.

---

## 🚀 Bonus (Optional Enhancements)

* Calculate total cost per shopping list.
* Remove grocery items.
* Remove shopping lists.
* Save/load lists from a file.
* Validate user input.

---

This activity reinforces:

* Classes and objects
* Object relationships (composition)
* Lists and collections
* User input handling
* Program design and structure

