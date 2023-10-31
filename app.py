import torch
import gradio as gr
import requests
from PIL import Image
from torchvision import transforms
model = torch.hub.load('pytorch/vision:v0.6.0','resnet18', pretrained=True).eval()

# Download human-readable labels for ImageNet.
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

def predict(inp):
    # input: image (numpy array or pil)
    # output: -> text (contains) label
    inp = transforms.ToTensor()(inp).unsqueeze(0)
    with torch.no_grad():
        print(model(inp).shape)
        prediction = torch.nn.functional.softmax(model(inp), dim = 0)
        prediction = torch.argmax(prediction, dim=1) # xac suat cao nhat
        print(prediction)
        final_label = labels[prediction] # label tuong ung voi xac suat cao nhat
    return str(final_label)


gr.Interface(fn=predict,
             inputs=gr.Image(type="pil"),
             outputs="text",
             examples=["lion.jpg"]).launch(share=True)