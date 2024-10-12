# Object Oriented Programming in Python Exercises 

### Practice Exercises for Object-Oriented Programming in Python

#### Exercise 1: Basic Class and Object Creation
1. **Define a Class:**
   - Create a class called `Person` with attributes for `name`, `age`, and `email`.
   - Include a method `introduce` that prints a string introducing the person.

2. **Create Objects:**
   - Create at least three objects of the `Person` class with different attribute values.
   - Call the `introduce` method on each object.

#### Exercise 2: Class Attributes and Methods
1. **Modify the `Person` Class:**
   - Add a class attribute `species` with the value `Homo sapiens`.
   - Add a method `birthday` that increments the person's age by 1.

#### Exercise 3: Inheritance
1. **Create a Subclass:**
   - Create a subclass of `Person` called `Student`.
   - Add an additional attribute `student_id` and override the `introduce` method to include the student ID.

2. **Test Inheritance:**
   - Create at least two `Student` objects.
   - Call the overridden `introduce` method on each.

#### Exercise 4: Polymorphism
1. **Create Multiple Classes:**
   - Create a class `Teacher` with attributes `name`, `age`, `email`, and `subject`.
   - Add a method `introduce` that prints a string introducing the teacher.

2. **Polymorphism in Action:**
   - Create a list of `Person`, `Student`, and `Teacher` objects.
   - Iterate over the list and call the `introduce` method on each object to demonstrate polymorphism.

#### Exercise 5: Encapsulation
1. **Encapsulate Attributes:**
   - Modify the `Person` class to make the `email` attribute private.
   - Add getter and setter methods for the `email` attribute.

2. **Test Encapsulation:**
   - Create a `Person` object and attempt to access the private `email` attribute directly.
   - Use the getter and setter methods to modify and retrieve the `email` attribute.