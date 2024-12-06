import numpy as np
import matplotlib.pyplot as plt
from read_txt import read_emg_data
from scipy import signal

# 读取文件数据
healthy_time, healthy_value = read_emg_data("../data/emg_healthy.txt")
neuropathy_time, neuropathy_value = read_emg_data("../data/emg_neuropathy.txt")
myopathy_time, myopathy_value = read_emg_data("../data/emg_myopathy.txt")


# 定义高斯脉冲信号
# def create_gaussian_pulse(time_axs, amplitude=1.0, center=0.5, width=0.1):
def create_gaussian_pulse(n):
    # return amplitude * np.exp(-((time_axs - center) ** 2) / (2 * width ** 2))
    return signal.gausspulse(n - 2, fc=2) + signal.gausspulse(n - 6, fc=1)


# 定义噪声信号
# def create_noise_signal(size, amplitude=0.1):
def create_noise_signal(n):
    # return amplitude * np.random.normal(0, 1, size)
    return np.random.normal(-0.1, 0.1, np.size(n))


# 创建时间轴
neuropathy_time = np.array(neuropathy_time)
healthy_time = np.array(healthy_time)
myopathy_time = np.array(myopathy_time)

# 创建高斯脉冲和噪声
# gaussian_healthy = create_gaussian_pulse(healthy_time, amplitude=0.5, center=0.05, width=0.01)
gaussian_healthy = create_gaussian_pulse(healthy_time)
# noise_healthy = create_noise_signal(len(healthy_time), amplitude=0.05)
noise_healthy = create_noise_signal(healthy_time)

# gaussian_neuropathy = create_gaussian_pulse(neuropathy_time, amplitude=0.5, center=0.05, width=0.01)
gaussian_neuropathy = create_gaussian_pulse(neuropathy_time)
# noise_neuropathy = create_noise_signal(len(neuropathy_time), amplitude=0.05)
noise_neuropathy = create_noise_signal(neuropathy_time)

# gaussian_myopathy = create_gaussian_pulse(myopathy_time, amplitude=0.5, center=0.05, width=0.01)
gaussian_myopathy = create_gaussian_pulse(myopathy_time)
# noise_myopathy = create_noise_signal(len(myopathy_time), amplitude=0.05)
noise_myopathy = create_noise_signal(myopathy_time)

# 叠加信号
combined_neuropathy = (
    np.array(neuropathy_value) + gaussian_neuropathy + noise_neuropathy
)
combined_healthy = np.array(healthy_value) + gaussian_healthy + noise_healthy
combined_myopathy = np.array(myopathy_value) + gaussian_myopathy + noise_myopathy


if __name__ == "__main__":
    # 创建图形
    fig, axs = plt.subplots(4, 3, figsize=(14, 8), sharex=True)

    # 信号名称和颜色
    titles = ["Healthy", "Neuropathy", "Myopathy"]
    colors = ["green", "blue", "red"]

    # 数据列表
    original_signals = [healthy_value, neuropathy_value, myopathy_value]
    times = [healthy_time, neuropathy_time, myopathy_time]
    gaussian_signals = [gaussian_healthy, gaussian_neuropathy, gaussian_myopathy]
    noise_signals = [noise_healthy, noise_neuropathy, noise_myopathy]
    combined_signals = [combined_healthy, combined_neuropathy, combined_myopathy]

    # 绘图
    for col, (time, original, gaussian, noise, combined, title, color) in enumerate(
        zip(
            times,
            original_signals,
            gaussian_signals,
            noise_signals,
            combined_signals,
            titles,
            colors,
        )
    ):
        # 混合信号
        axs[0, col].plot(time, combined, label="Mixed", color="cyan", alpha=0.7)
        axs[0, col].set_title(f"{title}: Mixed Signal")
        axs[0, col].set_ylabel("Amplitude")
        axs[0, col].grid(True)
        axs[0, col].legend()

        # 原始信号
        axs[1, col].plot(time, original, label="Original", color=color, alpha=0.7)
        axs[1, col].set_title(f"{title}: Original Signal")
        axs[1, col].set_ylabel("Amplitude")
        axs[1, col].grid(True)
        axs[1, col].legend()

        # 高斯脉冲信号
        axs[2, col].plot(
            time, gaussian, label="Gaussian Pulse", color="orange", alpha=0.7
        )
        axs[2, col].set_title(f"{title}: Gaussian Pulse Signal")
        axs[2, col].set_ylabel("Amplitude")
        axs[2, col].grid(True)
        axs[2, col].legend()

        # 噪声信号
        axs[3, col].plot(time, noise, label="Noise", color="purple", alpha=0.7)
        axs[3, col].set_title(f"{title}: Noise Signal")
        axs[3, col].set_xlabel("Time (s)")
        axs[3, col].set_ylabel("Amplitude")
        axs[3, col].grid(True)
        axs[3, col].legend()

    # 调整布局
    fig.suptitle(
        "EMG Signal Analysis: Mixed, Original, Gaussian Pulse, and Noise",
        fontsize=16,
        fontweight="bold",
    )
    plt.tight_layout()  # 留出大标题空间

    # 显示图形
    plt.show()
