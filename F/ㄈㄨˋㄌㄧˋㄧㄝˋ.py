import numpy as np
import matplotlib.pyplot as plt

# 1. 設定參數
t = np.linspace(0, 2, 1000)  # 2秒的時間
f = 1  # 基頻 1Hz

# 定義一個函數：用前 N 個奇數諧波來合成方波
def synthesize_square_wave(n_harmonics):
    signal = np.zeros_like(t)
    # 方波公式： sin(w) + 1/3 sin(3w) + 1/5 sin(5w) + ...
    for k in range(1, n_harmonics * 2, 2):  # 只取奇數項 (1, 3, 5...)
        coefficient = 4 / (np.pi * k)
        signal += coefficient * np.sin(2 * np.pi * k * f * t)
    return signal

# 2. 畫圖比較
plt.figure(figsize=(10, 8))

# 第一張：只有基頻 (Fundamental)
plt.subplot(3, 1, 1)
plt.plot(t, synthesize_square_wave(1), color='#D90429', linewidth=2)
plt.title('1st Harmonic (Just a Sine Wave)', fontsize=12)
plt.grid(True, alpha=0.3)

# 第二張：前 5 個波疊加
plt.subplot(3, 1, 2)
plt.plot(t, synthesize_square_wave(5), color='#D90429', linewidth=2)
plt.title('Sum of First 5 Harmonics (Getting Closer)', fontsize=12)
plt.grid(True, alpha=0.3)

# 第三張：前 50 個波疊加
plt.subplot(3, 1, 3)
plt.plot(t, synthesize_square_wave(50), color='#D90429', linewidth=2)
plt.plot(t, np.sign(np.sin(2*np.pi*f*t)), 'k--', alpha=0.3, label='Ideal Square Wave') # 理想方波
plt.title('Sum of First 50 Harmonics (Almost a Square Wave!)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()