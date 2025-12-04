from pathlib import Path
from PIL import Image

def loadSingleImage():
    root = Path("img_to_Torch")
    imgDir = Path("img")
    print("Available images:")
    for image_path in root.iterdir():
        if image_path.suffix == ".pt":
            print(image_path.stem)

    selected_image = input("Enter the filename of the image to load (without extension): ").strip()

    selected_image = selected_image.replace(".pt","").replace(".jpg", "") 

    pt_name = selected_image + ".pt"
    jpg_name = selected_image + ".jpg"


    # Automatisch richtigen Ordner finden 
    found_path = None
    for folder in imgDir.iterdir():
        if folder.is_dir():
            candidate = folder / jpg_name
            if candidate.exists():
                found_path = candidate
                break

    if not found_path:
        print(f"ERROR: Could not find {selected_image} in any folder inside {imgDir}")
        return

    img = Image.open(found_path)
    img.show()

    print(f"Loaded image from: {found_path}")

    # continue with loading the .pt file to send it to the model afterwards