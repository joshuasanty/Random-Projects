from PIL import Image

def combine_2x2(imgA_path, imgB_path, imgC_path, imgD_path, output_path):
    # Open images
    imgA = Image.open(imgA_path)
    imgB = Image.open(imgB_path)
    imgC = Image.open(imgC_path)
    imgD = Image.open(imgD_path)

    # Assume all images same size; if not, resize to match A
    w, h = imgA.size
    imgB = imgB.resize((w, h))
    imgC = imgC.resize((w, h))
    imgD = imgD.resize((w, h))

    # Create output canvas
    combined = Image.new("RGB", (w * 2, h * 2))

    # Paste images
    combined.paste(imgA, (0, 0))
    combined.paste(imgB, (w, 0))
    combined.paste(imgC, (0, h))
    combined.paste(imgD, (w, h))

    # Save result
    combined.save(output_path)
    print(f"Saved combined image as: {output_path}")


# Example usage:
combine_2x2("noiseLevel_chamferDistance_boxplot.png", "noiseLevel_F0.1_boxplot.png", "noiseLevel_F0.2_boxplot.png", "noiseLevel_F0.5_boxplot.png", "output/boxplotnoise.jpg")
