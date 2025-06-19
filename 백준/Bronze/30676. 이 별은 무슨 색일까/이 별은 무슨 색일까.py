lambda_nm = int(input())

if 380 <= lambda_nm < 425:
    print("Violet")
elif 425 <= lambda_nm < 450:
    print("Indigo")
elif 450 <= lambda_nm < 495:
    print("Blue")
elif 495 <= lambda_nm < 570:
    print("Green")
elif 570 <= lambda_nm < 590:
    print("Yellow")
elif 590 <= lambda_nm < 620:
    print("Orange")
else: 
    print("Red")
