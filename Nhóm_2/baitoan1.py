n = 77
gpa = 5.0 + (n % 5) * 0.5
diem_ren_luyen = 60 + (n % 4) * 10
hoc_phi_co_ban = 10000000 + (n * 100000)
print("---Thông tin sinh viên---")
print(f"GPA: {gpa}")
print(f"Điểm rèn luyện: {diem_ren_luyen}")
print(f"Học phí cơ bản: {hoc_phi_co_ban:,} VNĐ")
if gpa >= 6.5 and diem_ren_luyen >= 80:
    xep_loai = "Xuất sắc(Miễn giảm 50% học phí)"
    tong_hoc_phi = hoc_phi_co_ban * 50 // 100
elif gpa >= 5.5 and diem_ren_luyen >= 70:
    xep_loai = "Khá(Miễn giảm 25% học phí)"
    tong_hoc_phi = hoc_phi_co_ban * 75 // 100
elif gpa >= 4.0 and diem_ren_luyen >= 50:
    xep_loai = "Trung bình(Không miễn giảm)"
    tong_hoc_phi = hoc_phi_co_ban
else:
    xep_loai = "Cảnh báo học vụ(Phạt thêm 10%)"
    tong_hoc_phi = hoc_phi_co_ban * 110 // 100
print("Xếp loại học bổng:",xep_loai)
print(f"=> Tổng học phí phải đóng: {tong_hoc_phi:,} VNĐ")