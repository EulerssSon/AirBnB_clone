# Airbnb Clone Console

This is a command-line interface (CLI) for an Airbnb clone application. The CLI allows you to interact with various models such as User, State, City, Place, Amenity, and Review. You can create, show, update, and delete instances of these models using simple commands.

## How to Start

To run the Airbnb Clone Console, follow these steps:

1. Ensure that you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the `console.py` file.
4. Run the command: `python console.py` or `python3 console.py`.

The console will start, and you will see the prompt `(hbnb)`. Now you can enter commands to interact with the Airbnb clone application.

## How to Use

The Airbnb Clone Console supports the following commands:

- `quit` or `EOF`: Exit the program.
- `create <class_name>`: Create a new instance of the specified model.
- `show <class_name> <id>`: Display the string representation of an instance based on the class name and ID.
- `destroy <class_name> <id>`: Delete an instance based on the class name and ID.
- `all [<class_name>]`: Display the string representation of all instances or of a specific class.
- `update <class_name> <id> <attribute> <value>`: Update the attribute of an instance.

Additionally, you can use the following custom commands:

- `<class_name>.count()`: Count the number of instances of a specific class.
- `<class_name>.all()`: Display the string representation of all instances of a specific class.
- `<class_name>.show(<id>)`: Display the string representation of an instance based on the class name and ID.
- `<class_name>.destroy(<id>)`: Delete an instance based on the class name and ID.

## Examples

```python
(hbnb) create User
e1c275ab-c0ea-4f42-a9e8-96a7b42e16b2

(hbnb) show User e1c275ab-c0ea-4f42-a9e8-96a7b42e16b2
[User] (e1c275ab-c0ea-4f42-a9e8-96a7b42e16b2) {'id': 'e1c275ab-c0ea-4f42-a9e8-96a7b42e16b2', 'created_at': datetime.datetime(2024, 3, 11, 12, 0, 0), 'updated_at': datetime.datetime(2024, 3, 11, 12, 0, 0)}

(hbnb) update User e1c275ab-c0ea-4f42-a9e8-96a7b42e16b2 name "John Doe"

(hbnb) show User e1c275ab-c0ea-4f42-a9e8-96a7b42e16b2
[User] (e1c275ab-c0ea-4f42-a9e8-96a7b42e16b2) {'id': 'e1c275ab-c0ea-4f42-a9e8-96a7b42e16b2', 'created_at': datetime.datetime(2024, 3, 11, 12, 0, 0), 'updated_at': datetime.datetime(2024, 3, 11, 12, 1, 0), 'name': 'John Doe'}

(hbnb) User.count()
1

(hbnb) all User
[[User] (e1c275ab-c0ea-4f42-a9e8-96a7b42e16b2) {'id': 'e1c275ab-c0ea-4f42-a9e8-96a7b42e16b2', 'created_at': datetime.datetime(2024, 3, 11, 12, 0, 0), 'updated_at': datetime.datetime(2024, 3, 11, 12, 1, 0), 'name': 'John Doe'}]
