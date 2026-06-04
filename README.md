# Simple Calculator

This project is a simple calculator implemented in Python. It provides a command-line interface for evaluating mathematical expressions safely using an expression evaluator. The calculator supports basic arithmetic operations, unary operations, and common mathematical functions.

## Features

- Evaluate mathematical expressions with addition, subtraction, multiplication, division, and more.
- Support for unary operations such as negation.
- Built-in functions for square root, trigonometric functions, logarithms, and constants like π and e.
- Safe evaluation of expressions to prevent code injection.

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd simple-calculator
pip install -r requirements.txt
```

## Usage

To run the calculator, execute the following command:

```bash
python src/caculs.py
```

You will be presented with a prompt where you can enter mathematical expressions. Type `exit` or `quit` to exit the calculator.

## Testing

Unit tests for the calculator functionality are located in the `tests` directory. To run the tests, use the following command:

```bash
pytest tests/test_caculs.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
