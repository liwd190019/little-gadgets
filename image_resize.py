from torchvision import transforms
import os
from PIL import Image

resize_transform = transforms.Resize((512, 512))

# for image in 
van_dir = os.path.expanduser('/home/ubuntu/sky_workdir/vangogh_image_10shots')
resized_van_path = '/home/ubuntu/sky_workdir/vangogh_resized_image_10shots'
for filename in os.listdir(van_dir):
    image_path = os.path.join('/home/ubuntu/sky_workdir/vangogh_image_10shots', filename)
    if os.path.isfile(image_path) and filename.lower().endswith(('.jpg', '.jpeg', 'png')):
        image = Image.open(image_path)
        # image_tensor = transforms.ToTensor()(image)
        # resized_image = resize_transform(image_tensor)
        resized_image = image.resize((256, 256))
        resized_image_path = os.path.join(resized_van_path, filename)
        resized_image.save(resized_image_path)
