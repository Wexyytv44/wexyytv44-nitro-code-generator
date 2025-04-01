import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_nitro_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=24))

def generate_and_display():
    num_codes = int(entry_count.get())
    codes = [f"https://discord.gift/{generate_nitro_code()}" for _ in range(num_codes)]
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, '\n'.join(codes))

def save_to_file():
    codes = text_output.get(1.0, tk.END).strip()
    if not codes:
        messagebox.showwarning("Uyarı", "Önce kod üretmelisiniz!")
        return
    with open("nitro_codes.txt", "w") as file:
        file.write(codes)
    messagebox.showinfo("Başarılı", "Kodlar nitro_codes.txt olarak kaydedildi!")

# Ana pencere
root = tk.Tk()
root.title("WEXY-T0OLS | Nitro Generator")
root.geometry("400x500")
root.configure(bg="#222831")

# Başlık
label_title = tk.Label(root, text="🎁 WEXY-T0OLS 🎁", font=("Arial", 18, "bold"), fg="#76ABAE", bg="#222831")
label_title.pack(pady=10)

# Kod sayısı girişi
label_count = tk.Label(root, text="Kaç kod üretmek istiyorsunuz?", fg="#EEEEEE", bg="#222831")
label_count.pack()
entry_count = tk.Entry(root, width=10)
entry_count.pack()
entry_count.insert(0, "5")

# Kodları üretme butonu
btn_generate = tk.Button(root, text="Kod Üret", command=generate_and_display, bg="#76ABAE", fg="black")
btn_generate.pack(pady=5)

# Kodları gösteren metin kutusu
text_output = tk.Text(root, height=10, width=40)
text_output.pack(pady=10)

# Kaydetme butonu
btn_save = tk.Button(root, text="Kaydet", command=save_to_file, bg="#76ABAE", fg="black")
btn_save.pack()

# Pencereyi çalıştır
root.mainloop()