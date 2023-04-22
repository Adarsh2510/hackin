import replicate
def enhanceImage (prompt):
    outputUrl = replicate.run(
    "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
    input={"image": open("images/test_4.jpg", "rb")}
    )
    return outputUrl

def createBadge (prompt):
    return "https://replicate.delivery/pbxt/Y2NOATxdmZaDB96at8EK3IPcQ0zEBfXvD75W2g1K6F7meY0QA/out-0.png"