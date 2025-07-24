# Image to PNG Converter

A simple Python script that converts all image files in a folder to PNG format.  
Supports multiple image types (JPG, BMP, WEBP, etc.) and safely skips unsupported files.  
Great for bulk image conversion or automating image format cleanup.

---

## Features

- Converts any supported image format to `.png`
- Skips corrupted or unsupported files without crashing
- Works on Windows, macOS, and Linux
- Lightweight and beginner-friendly

---

## Example Input

This repository includes a folder called `Pokedox/` with sample images you can use for testing.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/image-to-png-converter.git
cd image-to-png-converter
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
```

Activate it:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install Pillow
```

---

## How to Use

```bash
python convert_to_png.py <input_folder> <output_folder>
```

### Example:

```bash
python convert_to_png.py ./Pokedox ./output
```

---

## Notes

- The output folder will be created automatically if it doesn’t exist.
- Only image files supported by Pillow will be converted.
- Files that are not valid images will be skipped without stopping the program.
