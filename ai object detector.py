import requests
from PIL import Image, ImageDraw
HFAPIKEY = "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"

model = "facebook/detr-resnet-101"
api = f"https://router.huggingface.co/hf-inference/models/{model}"

path = input("Enter Image path: ")
with open(path, "rb") as file:
    imageBytes = file.read()

headers = {
    "Authorization" : f"Bearer {HFAPIKEY}",
    "Content-Type" : "image/png"
}

response = requests.post(api, headers=headers, data=imageBytes)

if response.status_code != 200:
    print("Error:", response.text)
    exit()

detections = response.json()

image = Image.open(path)
draw = ImageDraw.Draw(image)

for obj in detections:
    if obj["score"] > 0.5:
        box = obj["box"]
        x1 = box["xmin"]
        y1 = box["ymin"]
        x2 = box["xmax"]
        y2 = box ["ymax"]

        draw.rectangle([x1, y1, x2, y2], outline="red",width=3)
        draw.text((x1+10, y1+10), obj["label"], fill="red")

save = input("save output image? (y/n): ").strip().lower()

if save == "y":
    output = "output.png"
    image.save(output)
    print(f"Output saved as '{output}'")

print("\nObjects Found")
for obj in detections:
    if obj["score"] > 0.5:
        print(f"{obj['label']} - {obj['score']:.2f}")

image.show()
