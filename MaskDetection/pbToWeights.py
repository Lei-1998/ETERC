import torch

# Instantiate your model. This is just a regular PyTorch model that will be exported in the following steps.
model =  torch.load('model_data/yolov4_maskdetect_weights1.pth')
# Evaluate the model to switch some operations from training mode to inference.
model.eval()
# Create dummy input for the model. It will be used to run the model inside export function.
dummy_input = torch.randn(1, 3, 224, 224)
# Call the export function
torch.onnx.export(model, (dummy_input, ), 'model.onnx')