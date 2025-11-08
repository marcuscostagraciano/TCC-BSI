# Comparative Analysis: NumPy vs C/Cython Implementations

*Read this in other languages: [Portuguese](README.md)*

This project aims to comparethe performance of basic statistical operations between the NumPy library and custom implementations in C and Cython.

## 🎯 Objective

Analyze and compare the execution time of different statistical operations (maximum, minimum, mean, and range) implemented in pure C, Cython, and NumPy, using large datasets.

## 🛠️ Cython Module Compilation

To compile Cython modules, use the setup script with CLI interface:

```bash
python setup.py build_ext --inplace
```

To clean generated files:

```bash
python setup.py clean --all
```

To see detailed setup help:

```bash
python setup.py --help-setup
```

### CLI Interface

The setup script has a command-line interface that facilitates module compilation and cleanup:

- `build_ext`: Compiles all Cython modules found in `src/pureCython/`
  - `--inplace`: Compiles extensions in their original location
- `clean`: Removes compilation files
  - `--all`: Removes all build artifacts
- `--help-setup`: Shows detailed help about available commands

## 🏗️ Project Architecture

### Class Structure

#### CLI Classes

- **CLIHandler**: Class responsible for command-line interface
  - Manages CLI arguments and options
  - Implements custom argument parser
  - Provides detailed help messages
  - Build, clean, and help options
  - User-friendly interface with English messages

#### Setup Classes

- **SetupConfig**: Configuration class for build process
  - Defines project paths and build settings
  - Manages file filters
  - Uses dataclass for simplified configuration
  - Controls which files should be ignored
  - Project path validation

- **CythonSetup**: Class for compilation management
  - Automatically discovers Cython modules
  - Manages extension creation and compilation
  - Uses class methods for static operations
  - Incremental compilation support
  - Automatic dependency management

#### Graph Classes

- **GraphConfig**: Configuration class for graph generation
  - Stores settings like title, legends, grid, and data
  - Uses `@dataclass` decorator for data management

- **BaseGraph**: Base graph class
  - Defines common interface for all graph types
  - Implements basic configuration and generation
  - Automatic graph download support
  - Silent mode option (download only)

- **Specific Graph Classes**:
  - `BoxPlot`: Generates box plots with multi-series support
  - `ViolinPlot`: Generates violin plots with configurable visualization options
  - `LinePlot`: Generates line plots with custom colors

Common features across all graphs:

- Automatic PNG download
- Silent mode (download only)
- Custom colors and styles
- Granular display control
- Legend and positioning configuration
- Raw data export to CSV

#### Test Classes

- **BaseTests**: Base class for performance tests
  - Manages graph download settings
  - Implements generic graph generation method
  - Configurable automatic result saving
  - Controls display vs. download behavior

- **Tests**: Main test class inheriting from BaseTests
  - Maintains NumPy results cache for reuse
  - Implements specific tests for each operation:
    - Maximum value (C and Cython)
    - Minimum value (C and Cython)
    - Arithmetic mean (Cython)
    - Range (C and Cython)
  - Offers execution methods:
    - Individual: by operation type
    - Complete: all operations sequentially
  - Supports method chaining
  - Silent execution support (download only)

### Performance Tests

The tests compare the following operations:

- Maximum Value (C and Cython vs NumPy)
- Minimum Value (C and Cython vs NumPy)
- Arithmetic Mean (Cython vs NumPy)
- Range (C and Cython vs NumPy)

## ⚡ Running Tests

### Prerequisites

- Python 3.10+
- NumPy
- Matplotlib
- Pandas
- Cython

### Installation

```bash
pip install -r requirements.txt
```

### Execution

1. Via Python Script:
   ```bash
   python main.py
   ```

1. Via Jupyter Notebook:
   - Open the `main.ipynb` file
   - Run cells sequentially

### Test Configuration

- `NUM_REPETICOES`: Number of times each test is executed
- `NUM_REGISTROS`: Test array size
- Settings can be adjusted in the `src/utils/consts.py` file

### Result Visualization

Tests automatically generate:

- Violin plots
- Line plots
- Raw data in CSV format
- Option to save results without display

## 📊 Project Structure

```markdown
TCC-BSI/
├── src/
│   ├── pureCython/      # Cython implementations
│   ├── classes/         # Graph and setup classes
│   ├── tests/           # Performance tests
│   └── utils/           # Utilities
├── main.py              # Main script
├── main.ipynb          # Jupyter Notebook
└── setup.py            # Setup script with CLI
```

[<img align="right" alt="Back to top" src="https://img.shields.io/badge/%E2%86%91-Back%20to%20top-lightgrey" />](#comparative-analysis-numpy-vs-ccython-implementations)
