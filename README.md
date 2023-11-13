
# Project Title: AirBnB Clone

## Description of the Project

This project is part of the AirBnB clone series - a larger project to eventually deploy a simple copy of the AirBnB website. The current phase of the project involves creating a command-line interpreter using Python, which lays the groundwork for the future web application. This interpreter allows for the management of the application's data, with functionalities to create, retrieve, update, and delete objects (CRUD operations).

## Description of the Command Interpreter

The command interpreter in this project is a console-based tool that allows interaction with the backend of the AirBnB clone. It is used for data management tasks such as creating new users or places, retrieving object information, updating attributes, and deleting objects.

### How to Start the Interpreter

To start the command interpreter, navigate to the project directory in your terminal and run the console file:

```bash
$ ./console.py
```

This will start the console, and you should see a prompt waiting for input:

```
(hbnb)
```

### How to Use the Command Interpreter

You can use the command interpreter by typing commands followed by their parameters. The interpreter supports various commands like `create`, `show`, `destroy`, `update`, and `all`.

#### Basic Commands and Usage:

- **Create**: Creates a new instance of a class.
  ```
  (hbnb) create User
  ```

- **Show**: Displays the information of an object of a given class and id.
  ```
  (hbnb) show User user_id
  ```

- **Destroy**: Deletes an instance based on the class name and id.
  ```
  (hbnb) destroy User user_id
  ```

- **Update**: Updates an instance based on the class name and id by adding or updating an attribute.
  ```
  (hbnb) update User user_id email "user@example.com"
  ```

- **All**: Displays all instances of a class or, if no class is specified, all instances of every class.
  ```
  (hbnb) all User
  ```

### Examples

Here are some examples of using the command interpreter:

1. **Creating a new user**:
   ```
   (hbnb) create User
   ```

2. **Retrieving a user's information**:
   ```
   (hbnb) show User user_id
   ```

3. **Deleting a user**:
   ```
   (hbnb) destroy User user_id
   ```

4. **Updating a user's email address**:
   ```
   (hbnb) update User user_id email "new_email@example.com"
   ```

