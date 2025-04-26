# FITS_Parser

A simple FITS file parser made using Astropy and Numpy.

## Instructions on how to run the Decoder.py

### Step 1. Install Interpreter

Before running, ensure you have a python version 3 or above interpreter.

### Step 2. Clone the Repository

If you have git installed:

```bash
git clone https://github.com/Syntax-Programmer/FITS_Parser.git
```

Otherwise, download the zip file of the code from

```link
https://github.com/Syntax-Programmer/FITS_Parser
```

### Step 3. (Optional) Generate a Virtual Environment

Make a Virtual Environment if you don't want to install the dependencies globally.

#### Unix based systems

To generate the Virtual Environment:

```bash
python3 -m venv location/to/gen/venv/to
```

Activate the Virtual Environment:

```bash
source location/of/your/venv/bin/activate
```

Install the dependencies after the above command.

Exiting the Virtual Environment:

```bash
deactivate
```

#### Windows

To generate the Virtual Environment:

```bash
python3 -m venv location\to\gen\venv\to
```

##### Activate the Virtual Environment

If you are using the command prompt:

```bash
source location\of\your\venv\bin\activate.bat
```

If you are using Powershell:

```bash
source location\of\your\venv\bin\activate.ps1
```

Install the dependencies after the above command.

Exiting the Virtual Environment:

```bash
deactivate
```

### Step 4. Install Dependencies

Locate into the project directory and install the dependencies:

```bash
pip install -r requirements.txt
```

### Step 5. Run the Decoder

Locate to the project directory and run:

```bash
python3 Decoder.py
```

## How to Write the ToParse.csv for Parsing

### Step 1: Create file "ToParse.csv" in the FITS_Parser directory

### Step 2: Writing the File

#### NOTE: Following the formatting guidelines given below is the responsibility of the user. Minimal checks are performed to verify validity.

The format to write a single line to the file:

```txt
absolute_filepath.fits,metadata=true/false
```

- Maintain the delimiter as ",".

- First comes the **file path** to the FITS file to parse, it has to be absolute path, or relative to the **FITS_Parser** directory.

- Second is the **metadata** flag, specifying weather to include metadata in the parsed file. In the above format, the "metadata=true/false" flag is case independent so go crazy.

Example:

```txt
test.fits,metadata=false
impo.fits,metadata=true
```
