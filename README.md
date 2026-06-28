# Python Object-Oriented Programming (OOP)

## 📖 Overview

This project demonstrates the core concepts of **Object-Oriented Programming (OOP)** in Python. It includes examples of classes, objects, inheritance, polymorphism, encapsulation, and abstraction to help understand how OOP is used to build clean, reusable, and maintainable applications.

## 🚀 Features

* Class and Object creation
* Constructors (`__init__`)
* Instance and Class Variables
* Instance, Class, and Static Methods
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction using Abstract Base Classes (ABC)
* Method Overriding
* Real-world examples

## 📂 Project Structure

```text
python-oop/
│── main.py
│── person.py
│── student.py
│── employee.py
│── examples/
│── README.md
```

## 🛠️ Requirements

* Python 3.8 or higher

## ▶️ Running the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/python-oop.git
```

2. Navigate to the project directory:

```bash
cd python-oop
```

3. Run the program:

```bash
python main.py
```

## 📚 OOP Concepts Covered

### 1. Class

A blueprint for creating objects.

### 2. Object

An instance of a class with its own attributes and methods.

### 3. Constructor

The `__init__()` method initializes object attributes when an object is created.

### 4. Encapsulation

Restricts direct access to object data by using methods or properties.

### 5. Inheritance

Allows a child class to inherit attributes and methods from a parent class.

### 6. Polymorphism

Allows different classes to implement the same method in different ways.

### 7. Abstraction

Hides implementation details using abstract classes from the `abc` module.

## 📌 Example

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()
```

**Output**

```text
Dog barks
```

## 🎯 Learning Objectives

* Understand Python classes and objects.
* Learn the four pillars of OOP:

  * Encapsulation
  * Abstraction
  * Inheritance
  * Polymorphism
* Build reusable and modular Python programs.
* Practice designing object-oriented applications.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, improve the examples, and submit a pull request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Inam Ullah**
