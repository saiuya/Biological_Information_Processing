import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftfreq
from read_txt import read_emg_data


# 读取文件数据
healthy_time, healthy_value = read_emg_data("../data/emg_healthy.txt")
neuropathy_time, neuropathy_value = read_emg_data("../data/emg_neuropathy.txt")
myopathy_time, myopathy_value = read_emg_data("../data/emg_myopathy.txt")


# 定义FFT和IFFT处理函数
def compute_fft(time, values):
    n = len(values)  # 数据点数
    dt = time[1] - time[0]  # 采样间隔
    frequencies = fftfreq(n, dt)  # 频率
    spectrum = fft(values)  # 频谱
    return frequencies, spectrum


def compute_ifft(spectrum):
    return np.real(ifft(spectrum))  # 返回实部，重建信号


# 对信号进行FFT和IFFT
freq_healthy, spectrum_healthy = compute_fft(healthy_time, healthy_value)
reconstructed_healthy = compute_ifft(spectrum_healthy)


freq_neuropathy, spectrum_neuropathy = compute_fft(neuropathy_time, neuropathy_value)
reconstructed_neuropathy = compute_ifft(spectrum_neuropathy)


freq_myopathy, spectrum_myopathy = compute_fft(myopathy_time, myopathy_value)
reconstructed_myopathy = compute_ifft(spectrum_myopathy)

# 创建图形比较原始信号和重建信号的拟合度
fig, axs = plt.subplots(3, 2, sharex=True)


# Healthy 信号
axs[0][0].plot(
    healthy_time, healthy_value, label="Original Healthy", color="green", alpha=0.7
)
axs[0, 0].set_title("Original Healthy Signal")
axs[0, 0].set_ylabel("Amplitude")
axs[0, 0].grid(True)

axs[0, 1].plot(
    healthy_time,
    reconstructed_healthy,
    label="Reconstructed Healthy",
    color="lime",
    alpha=0.7,
)
axs[0, 1].set_title("Reconstructed Healthy Signal")
axs[0, 1].grid(True)


# Neuropathy 信号
axs[1, 0].plot(
    neuropathy_time,
    neuropathy_value,
    label="Original Neuropathy",
    color="blue",
    alpha=0.7,
)
axs[1, 0].set_title("Original Neuropathy Signal")
axs[1, 0].set_ylabel("Amplitude")
axs[1, 0].grid(True)

axs[1, 1].plot(
    neuropathy_time,
    reconstructed_neuropathy,
    label="Reconstructed Neuropathy",
    color="cyan",
    alpha=0.7,
)
axs[1, 1].set_title("Reconstructed Neuropathy Signal")
axs[1, 1].grid(True)


# Myopathy 信号
axs[2, 0].plot(
    myopathy_time, myopathy_value, label="Original Myopathy", color="red", alpha=0.7
)
axs[2, 0].set_title("Original Myopathy Signal")
axs[2, 0].set_xlabel("Time (s)")
axs[2, 0].set_ylabel("Amplitude")
axs[2, 0].grid(True)

axs[2, 1].plot(
    myopathy_time,
    reconstructed_myopathy,
    label="Reconstructed Myopathy",
    color="orange",
    alpha=0.7,
)
axs[2, 1].set_title("Reconstructed Myopathy Signal")
axs[2, 1].set_xlabel("Time (s)")
axs[2, 1].grid(True)

# 添加大标题
# fig.suptitle('Comparison of Original and Reconstructed EMG Signals', fontsize=16, fontweight='bold')

# 调整布局
plt.tight_layout()  # 留出大标题空间

# 显示图形
plt.show()
