
# 🧬 Python Inheritance – Step-by-Step Walkthrough

## 🎯 Learning Objective

By the end of this walkthrough, students will be able to:

* Understand what inheritance is
* Create a parent (base) class
* Create a child (derived) class
* Reuse and extend behavior
* Override methods
* Use `super()` correctly

---

# 1️⃣ What Is Inheritance?

Inheritance allows one class to **reuse attributes and methods** from another class.

Think of it like:

> A child inherits traits from a parent.

In programming:

* **Parent class (Base class)** → Contains common behavior
* **Child class (Derived class)** → Inherits from parent and adds or modifies behavior

---

# 2️⃣ Real-World Analogy

All cars have:

* make
* model
* start() method

But electric cars also:

* have battery_level
* can charge()

Instead of rewriting everything, we inherit.

---

# 3️⃣ Step 1: Create a Parent Class

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} is starting.")
```

### What This Does:

* Defines common properties
* Defines shared behavior

---

# 4️⃣ Step 2: Create a Child Class

To inherit, we place the parent class name in parentheses.

```python
class Car(Vehicle):
    pass
```

Now `Car` inherits everything from `Vehicle`.

---

# 5️⃣ Step 3: Use the Child Class

```python
my_car = Car("Toyota", "Camry")
my_car.start()
```

Output:

```
Toyota Camry is starting.
```

💡 Even though `Car` has no methods, it inherited `start()`.

---

# 6️⃣ Step 4: Extending the Child Class

Now let's add new behavior specific to `Car`.

```python
class Car(Vehicle):
    def honk(self):
        print("Beep beep!")
```

Usage:

```python
my_car = Car("Honda", "Accord")
my_car.start()
my_car.honk()
```

Now the child has:

* All parent methods
* Plus its own methods

---

# 7️⃣ Step 5: Overriding a Parent Method

Sometimes we want to modify behavior.

```python
class ElectricCar(Vehicle):
    def start(self):
        print(f"{self.make} {self.model} starts silently.")
```

Usage:

```python
tesla = ElectricCar("Tesla", "Model 3")
tesla.start()
```

Output:

```
Tesla Model 3 starts silently.
```

⚠️ This replaces the parent's `start()` method.

---

# 8️⃣ Step 6: Using super()

If we want to reuse the parent logic *and* extend it, use `super()`.

```python
class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_level):
        super().__init__(make, model)
        self.battery_level = battery_level
```

### Why super()?

It calls the parent’s constructor so we don’t rewrite initialization logic.

Usage:

```python
tesla = ElectricCar("Tesla", "Model X", 90)
print(tesla.make)
print(tesla.battery_level)
```

---

# 9️⃣ Full Example Together

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} is starting.")


class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_level):
        super().__init__(make, model)
        self.battery_level = battery_level

    def start(self):
        print(f"{self.make} {self.model} starts silently.")

    def charge(self):
        print("Charging the battery.")


tesla = ElectricCar("Tesla", "Model 3", 80)
tesla.start()
tesla.charge()
```

---

# 🔟 Visual Concept

```
Vehicle
   ↑
ElectricCar
```

ElectricCar:

* Inherits make
* Inherits model
* Inherits start()
* Overrides start()
* Adds charge()

---

# 🔎 Key Concepts Summary

| Concept      | Meaning                  |
| ------------ | ------------------------ |
| Inheritance  | One class reuses another |
| Parent class | Base class               |
| Child class  | Derived class            |
| super()      | Calls parent methods     |
| Overriding   | Replacing parent method  |

---

# 🧠 When Should You Use Inheritance?

Use inheritance when:

* There is a clear "is-a" relationship
* A child is a specialized version of a parent
* You want to reuse common behavior

Example:

* Dog **is a** Animal
* Manager **is an** Employee
* ElectricCar **is a** Vehicle

---

# 🚨 Common Mistakes

* Forgetting `super().__init__()`
* Using inheritance when composition is better
* Overcomplicating class hierarchies

---

# 🏁 Mini Practice Exercise (No Solution)

Create:

1. A `Person` class with name and age.
2. A `Student` class that inherits from Person and adds grade.
3. Override a method called introduce().
4. Use super() in the constructor.

---

