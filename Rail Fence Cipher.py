import tkinter as tk
from tkinter import scrolledtext

# ---------------- ENCODING ----------------
def encoding(plain_text, rails):
    if rails == 1:
        return plain_text

    rail = [["" for _ in range(len(plain_text))] for _ in range(rails)]
    row, direction = 0, 1

    for col in range(len(plain_text)):
        rail[row][col] = plain_text[col]
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    encrypted_text = ""
    for r in range(rails):
        for c in range(len(plain_text)):
            if rail[r][c] != "":
                encrypted_text += rail[r][c]

    return encrypted_text

# ---------------- DECODING ----------------
def decoding(cipher_text, rails):
    if rails == 1:
        return cipher_text

    rail = [["" for _ in range(len(cipher_text))] for _ in range(rails)]
    row, direction = 0, 1

    # Mark zigzag positions
    for col in range(len(cipher_text)):
        rail[row][col] = "*"
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    # Fill marked positions
    index = 0
    for r in range(rails):
        for c in range(len(cipher_text)):
            if rail[r][c] == "*" and index < len(cipher_text):
                rail[r][c] = cipher_text[index]
                index += 1

    # Read zigzag
    result = ""
    row, direction = 0, 1
    for col in range(len(cipher_text)):
        result += rail[row][col]
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    return result

# ---------------- GUI FUNCTIONS ----------------
def encode_text():
    global encrypted_text
    plain_text = input_text.get("1.0", tk.END).strip().replace(" ", "")
    rails = int(rail_input.get("1.0", tk.END).strip())

    if not plain_text or rails <= 0:
        return

    encrypted_text = encoding(plain_text, rails)
    encrypted_box.delete("1.0", tk.END)
    encrypted_box.insert(tk.END, encrypted_text)

def decode_text():
    rails = int(rail_input.get("1.0", tk.END).strip())
    if not encrypted_text or rails <= 0:
        return

    decoded_text = decoding(encrypted_text, rails)
    decoded_box.delete("1.0", tk.END)
    decoded_box.insert(tk.END, decoded_text)

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Rail Fence Cipher")

tk.Label(root, text="Enter Text:").pack()
input_text = scrolledtext.ScrolledText(root, height=8, width=100)
input_text.pack()

tk.Label(root, text="Number of Rails:").pack()
rail_input = scrolledtext.ScrolledText(root, height=2, width=10)
rail_input.pack()

encode_btn = tk.Button(root, text="Encode", command=encode_text)
encode_btn.pack()

tk.Label(root, text="Encrypted Text:").pack()
encrypted_box = scrolledtext.ScrolledText(root, height=8, width=100)
encrypted_box.pack()

decode_btn = tk.Button(root, text="Decode", command=decode_text)
decode_btn.pack()

tk.Label(root, text="Decoded Text:").pack()
decoded_box = scrolledtext.ScrolledText(root, height=8, width=100)
decoded_box.pack()

root.mainloop()