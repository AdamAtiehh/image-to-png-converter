import sys
import os
from PIL import Image, UnidentifiedImageError

def convert_images_to_png(input_folder, output_folder):
    """Converts all supported image files in the input_folder to PNG format and saves them to output_folder."""

    # Validate input path
    if not os.path.isdir(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist or is not a directory.")
        return

    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    converted_count = 0

    # Loop through files in the input directory
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Skip if it's not a file
        if not os.path.isfile(input_path):
            continue

        try:
            # Try opening the image
            with Image.open(input_path) as img:
                # Get the base name without extension
                clean_name = os.path.splitext(filename)[0]

                # Define the output path with PNG extension
                output_path = os.path.join(output_folder, f"{clean_name}.png")

                # Convert and save
                img.save(output_path, "PNG")
                print(f"Converted: {filename} → {clean_name}.png")
                converted_count += 1

        except UnidentifiedImageError:
            print(f"Skipped (not a valid image): {filename}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

    print(f"\nDone. {converted_count} image(s) converted to PNG.")


if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python convert_to_png.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    convert_images_to_png(input_folder, output_folder)
