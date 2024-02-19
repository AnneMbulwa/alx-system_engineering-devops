0x15. API

    What to cover
What Bash scripting should not be used for
What is an API
What is a REST API
What are microservices
What is the CSV format
What is the JSON format
Pythonic Package and module name style
Pythonic Class name style
Pythonic Variable name style
Pythonic Function name style
Pythonic Constant name style
Significance of CapWords or CamelCase in Python

Bash scripting should not be used for tasks that require complex data manipulation, heavy computational tasks, or high-level programming constructs. While Bash is a powerful scripting language for automating command-line tasks and simple scripting tasks, it is not well-suited for more complex programming scenarios. In such cases, using a more robust programming language like Python or Java would be more appropriate.

An API, or Application Programming Interface, is a set of rules and protocols that allows different software applications to communicate and interact with each other. It defines the methods, data formats, and conventions that developers can use to interact with a software component or service.

A REST API, or Representational State Transfer API, is a type of API that follows the principles of the REST architectural style. It is designed to be stateless, scalable, and provide a uniform interface for accessing and manipulating resources over the web. REST APIs typically use HTTP methods like GET, POST, PUT, and DELETE to perform CRUD (Create, Read, Update, Delete) operations on resources.

Microservices are a software architecture pattern where applications are built as a collection of small, loosely coupled, and independently deployable services. Each microservice is responsible for a specific business capability and can be developed, deployed, and scaled independently. Microservices promote modularity, scalability, and maintainability in large-scale applications.

CSV stands for Comma-Separated Values. It is a simple file format used for storing tabular data, such as spreadsheets or databases. In a CSV file, each line represents a row, and the values within each row are separated by commas or other delimiters. CSV files are commonly used for data interchange between different applications.

JSON stands for JavaScript Object Notation. It is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. JSON is often used to transmit data between a server and a web application as an alternative to XML. It is based on a subset of the JavaScript programming language and uses key-value pairs to represent data objects.

In Python, there are conventions for naming packages, modules, classes, variables, functions, and constants. Following these conventions is often referred to as "Pythonic" style. Here are the general guidelines:

- Package and module names should be in lowercase, with words separated by underscores. For example: `my_package`, `my_module`.

- Class names should follow the CapWords convention, also known as CamelCase, where each word starts with an uppercase letter and there are no underscores. For example: `MyClass`, `MyOtherClass`.

- Variable names should be in lowercase, with words separated by underscores. For example: `my_variable`, `my_other_variable`.

- Function names should be in lowercase, with words separated by underscores. For example: `my_function`, `my_other_function`.

- Constants, which are typically defined using uppercase letters, should use underscores to separate words. For example: `MY_CONSTANT`, `MY_OTHER_CONSTANT`.

The use of CapWords or CamelCase in Python is significant because it helps improve readability and consistency in the codebase. It makes it easier for developers to distinguish between different elements and aligns with the conventions followed by the Python community.
