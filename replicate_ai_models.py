import replicate
import os

def enhanceImage (input_image_path):
    outputUrl = replicate.run(
    os.getenv('ENHANCE_MODEL'),
    input={"image": open(input_image_path, "rb")}
    )
    return outputUrl

def createBadge(prompt):
    # badge code here
    output = replicate.run(
        os.getenv('PRE_TRAINED_EDIT_IMAGE_MODEL'),
        input={"prompt": prompt}
    )
    print(output)
    return output[0]
