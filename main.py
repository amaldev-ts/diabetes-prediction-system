from predict import predict_diabetes

print("DIABETES PREDICTION SYSTEM")

while True:

    predict_diabetes()

    ch = input("Again? (y/n): ")

    if ch.lower() != "y":
        break