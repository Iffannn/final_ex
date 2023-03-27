#ชานมแก้วละ 25 บาท 
# ข่มุก 5 บาท 
# เฉาก๊วย 10 บาท 
# ถั่วแดง 15 บาท 
# วิปครีม 15 บาท 
# เลือกท๊อปปิ้งได้ไม่เกิน 2 อย่าง 

def calculate_price_tea(price):
    if price == 30:
        return "bubble"
    elif price == 35:
        return "grass jelly"
    elif price == 40:
        return "red bean,whipped cream,bubble and grass jelly"
    elif price == 45:
        return "bubble and red bean,bubble and whipped cream"
    elif price == 50:
        return "grass jelly and red bean,grass jelly and whipped cream"
    elif price == 60:
        return "red bean and whipped cream"
    elif price == 25:
        return "Only tea,not have topping"