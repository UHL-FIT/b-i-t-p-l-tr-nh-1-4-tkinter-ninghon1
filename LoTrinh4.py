import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def xu_ly_thong_tin():
    # Tương tác Terminal: In thời gian hiện tại lúc sinh viên nhấn nút
    thoi_gian_hien_tai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{thoi_gian_hien_tai}] Đã nhấn nút xử lý")

    mssv = o_nhap_ma_sv.get()
    ho_ten = o_nhap_ho_ten.get()

    # Ràng buộc dữ liệu: Kiểm tra MSSV có phải là số không
    if not mssv.isdigit():
        # Thông báo Popup: Dùng messagebox.showerror() thay vì hiện lên Label
        messagebox.showerror("Lỗi nhập liệu", "MSSV phải là số!")
        return
    
    # In kết quả thành công ra terminal
    print(f"Thông tin sinh viên - MSSV: {mssv}, Họ tên: {ho_ten}")
    
    # Hiển thị kết quả thành công lên nhãn kết quả
    nhan_ket_qua.config(text=f"Đã lưu: {ho_ten} ({mssv})", fg="green")

    # Xóa trắng 2 ô nhập liệu sau khi thành công
    o_nhap_ma_sv.delete(0, tk.END)
    o_nhap_ho_ten.delete(0, tk.END)

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL (LoTrinh 4)")
root.geometry("400x250")

root.columnconfigure(1, weight=1)

# Tạo các thành phần
nhan_ma_sv = tk.Label(root, text="Mã sinh viên:")
o_nhap_ma_sv = tk.Entry(root)

nhan_ho_ten = tk.Label(root, text="Họ và tên:")
o_nhap_ho_ten = tk.Entry(root)

nut_xu_ly = tk.Button(root, text="Xử lý thông tin", command=xu_ly_thong_tin)

nhan_ket_qua = tk.Label(root, text="Kết quả sẽ hiển thị ở đây")

# Bố cục giao diện
nhan_ma_sv.grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

nhan_ho_ten.grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

nut_xu_ly.grid(row=2, column=0, columnspan=2, pady=10)

nhan_ket_qua.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
