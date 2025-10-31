# Simple Calculator

This project contains two calculator implementations:
1. A GUI-based calculator (`calc_gui_safe.py`)
2. A CLI-based calculator (`calc_cli_safe.py`)

Both calculators implement basic arithmetic operations with input validation for safe calculations.

## Features

- Basic arithmetic operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
- Input validation and error handling
- Safe numeric calculations
- User-friendly interfaces (GUI and CLI options)

## Requirements

- Python 3.x
- tkinter (for GUI version)

## Installation

1. Clone or download this repository
2. Ensure Python 3.x is installed on your system
3. No additional packages need to be installed for CLI version
4. For GUI version, tkinter should be included in standard Python installation

## Usage

### GUI Calculator

Run the GUI calculator with:
```bash
python calc_gui_safe.py
```

The GUI calculator provides:
- Numeric buttons (0-9)
- Operation buttons (+, -, *, /)
- Clear button (C)
- Equals button (=)
- Display screen for input/output

### CLI Calculator

Run the CLI calculator with:
```bash
python calc_cli_safe.py
```

Follow the prompts to:
1. Enter the first number
2. Choose an operation
3. Enter the second number
4. View the result
5. Choose to continue or exit

## Error Handling

Both calculators include:
- Protection against division by zero
- Input validation for numbers
- Safe arithmetic operations

## Contributing

Feel free to submit issues and enhancement requests.

## License

[MIT License](LICENSE)
