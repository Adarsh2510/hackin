import replicate
import requests
def enhanceImage (prompt):
    outputUrl = replicate.run(
    "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
    input={"image": open("images/test_4.jpg", "rb")}
    )
    return outputUrl

def createBadge(prompt):
    # badge code here
    print("here")
    output = replicate.run(
        "adarsh2510/badgevarun:9fe1029bcbf0c87337b9d4ae9685823c4a675c0d0b9a5af90594459637eac55a",
        input={"prompt": prompt}
    )
    print(output)
    return output[0]
