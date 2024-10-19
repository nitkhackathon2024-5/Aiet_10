Design Pattern Detector Web Application
This project is a web-based tool that allows users to detect design patterns in Python code. The current version can detect Singleton, Factory, and Observer patterns in the given code.


Installation-
1.Clone the repository
Step-by-Step Setup-
git clone https://github.com/your-username/design-pattern-detector.git
cd design-pattern-detector

2.Set up a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.Set environment variables (for Flask): On Linux or macOS:
export FLASK_APP=app.py
export FLASK_ENV=development

or On Windows:

set FLASK_APP=app.py
set FLASK_ENV=development

How to Run
1.Run the Flask application:
flask run

2.Access the application: Open your browser and go to http://localhost:5000.

3.You should see a simple UI where you can input Python code for pattern detection.

How to Use
Instructions
1.Open the web app: After running the Flask server, open the app in your browser at http://localhost:5000.

2.Input Python Code: Paste your Python code in the text area provided.

3.Detect Design Patterns: Press the "Detect Patterns" button.

4.View Results: Detected patterns will be displayed below the text area, including their names and descriptions.


Contributing
1.Fork the project.
2.Create your feature branch:

git checkout -b feature/your-feature-name

3.Commit your changes:

git commit -m 'Add some feature'

4.Push to the branch:

git push origin feature/your-feature-name

5.Create a pull request.


these are some examples for test case in the program:

class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class ConcreteObserver(Observer):
    def update(self, subject):
        print("Observer notified!")

Factory Pattern:
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        return None


Singleton Pattern:

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
