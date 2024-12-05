import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from read_txt import read_emg_data


# 读取文件数据
healthy_time, healthy_value = read_emg_data('./data/emg_healthy.txt')
neuropathy_time, neuropathy_value = read_emg_data('./data/emg_neuropathy.txt')
myopathy_time, myopathy_value = read_emg_data('./data/emg_myopathy.txt')



# 定义一个函数进行FFT变换
def compute_fft(time, values):
    n = len(values)  # 数据点数
    dt = time[1] - time[0]  # 采样间隔
    frequencies = fftfreq(n, dt)[:n // 2]  # 频率
    spectrum = np.abs(fft(values))[:n // 2]  # 频谱
    return frequencies, spectrum

# 对信号进行FFT
freq_healthy, spectrum_healthy = compute_fft(healthy_time, healthy_value)
freq_neuropathy, spectrum_neuropathy = compute_fft(neuropathy_time, neuropathy_value)
freq_myopathy, spectrum_myopathy = compute_fft(myopathy_time, myopathy_value)

# 创建图形并绘制频谱图
fig, axs = plt.subplots(3, 1, sharex=True)

# Healthy 频谱图
axs[0].plot(freq_healthy, spectrum_healthy, label='Healthy', color='green', alpha=0.7)
axs[0].set_title('Healthy Frequency Spectrum')
axs[0].set_ylabel('Amplitude')
axs[0].grid(True)
axs[0].legend()

# Neuropathy 频谱图
axs[1].plot(freq_neuropathy, spectrum_neuropathy, label='Neuropathy', color='blue', alpha=0.7)
axs[1].set_title('Neuropathy Frequency Spectrum')
axs[1].set_ylabel('Amplitude')
axs[1].grid(True)
axs[1].legend()

# Myopathy 频谱图
axs[2].plot(freq_myopathy, spectrum_myopathy, label='Myopathy', color='red', alpha=0.7)
axs[2].set_title('Myopathy Frequency Spectrum')
axs[2].set_xlabel('Frequency (Hz)')
axs[2].set_ylabel('Amplitude')
axs[2].grid(True)
axs[2].legend()

# 添加大标题
# fig.suptitle('Frequency Spectrum of EMG Signals', fontsize=16, fontweight='bold')

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()
