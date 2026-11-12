n = 77
pin_dung = 1000 + n
max_attempts = 3 + (n % 3)
luot_con_lai = max_attempts

while luot_con_lai > 0:
    nhap_ma_pin = input("Nhập mã PIN: ")
    if nhap_ma_pin == str(pin_dung):
        print("Đăng nhập thành công!")
        otp = []
        for i in range(1, 6):
            ket_qua = n * i
            if ket_qua % 2 != 0:
                continue
            otp.append(str(ket_qua))
        print("--- MÃ OTP CỦA BẠN ---")
        print("OTP: " + "-".join(otp))

        break
    luot_con_lai -= 1
    if luot_con_lai > 0:
        print(f"Sai! Bạn còn {luot_con_lai} lần thử.")
    else:
        print("Tài khoản đã bị khóa!")