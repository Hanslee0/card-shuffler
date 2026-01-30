import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# 카드 목록 생성
suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [f"{rank}_of_{suit}" for suit in suits for rank in ranks]

# 카드 섞기
random.shuffle(deck)

# GUI 설정 
root = tk.Tk()
root.title("Shuffled Cards")

# 카드 이미지를 로드하고 표시
frame = tk.Frame(root)
frame.pack()

cards_folder = os.path.abspath("cards")
def load_card_images():
    images = []
    for card in deck:
        # 카드 이미지 경로 설정
        card_path = os.path.join(cards_folder, f"{card}.png")
        print(f"Looking for: {card_path}")
        if os.path.exists(card_path):
            img = Image.open(card_path)
            img.thumbnail((100, 150))  # 이미지 크기 조정
            images.append(ImageTk.PhotoImage(img))
        else:
            print(f"Image for {card} not found!")
    return images

# 카드 이미지 로드
card_images = load_card_images()

# 이미지 디스플레이
for idx, card_image in enumerate(card_images):
    label = tk.Label(frame, image=card_image)
    label.grid(row=idx // 13, column=idx % 13)

root.mainloop()
