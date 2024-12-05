import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import hilbert

from origin_fig import healthy_value, neuropathy_value, myopathy_value, neuropathy_time

# 找到最短信号的长度
min_length = min(len(neuropathy_value), len(healthy_value), len(myopathy_value))

# 对信号进行截断
neuropathy_value_trimmed = np.array(neuropathy_value[:min_length])
healthy_value_trimmed = np.array(healthy_value[:min_length])
myopathy_value_trimmed = np.array(myopathy_value[:min_length])
neuropathy_time_trimmed = np.array(neuropathy_time[:min_length])

# 定义Hilbert变换函数
def hilbert_transform(signal):
    analytic_signal = hilbert(signal)  # 计算解析信号
    instantaneous_phase = np.unwrap(np.angle(analytic_signal))  # 瞬时相位，并解相位包裹
    return instantaneous_phase

# 对三个信号进行Hilbert变换
phase_neuropathy = hilbert_transform(neuropathy_value_trimmed)
phase_healthy = hilbert_transform(healthy_value_trimmed)
phase_myopathy = hilbert_transform(myopathy_value_trimmed)


if __name__ == '__main__':
    # 创建图形并绘制相位图
    fig, axs = plt.subplots(3, 1, sharex=True)

    # Healthy 信号相位
    axs[0].plot(neuropathy_time_trimmed, phase_healthy, label='Healthy Phase', color='green')
    axs[0].set_title('Healthy Phase')
    axs[0].set_ylabel('Phase (radians)')
    axs[0].grid(True)
    axs[0].legend()


    # Neuropathy 信号相位
    axs[1].plot(neuropathy_time_trimmed, phase_neuropathy, label='Neuropathy Phase', color='blue')
    axs[1].set_title('Neuropathy Phase')
    axs[1].set_ylabel('Phase (radians)')
    axs[1].grid(True)
    axs[1].legend()


    # Myopathy 信号相位
    axs[2].plot(neuropathy_time_trimmed, phase_myopathy, label='Myopathy Phase', color='red')
    axs[2].set_title('Myopathy Phase')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('Phase (radians)')
    axs[2].grid(True)
    axs[2].legend()

    # 调整布局和标题
    # fig.suptitle('Phase of EMG Signals (Hilbert Transform)', fontsize=16, fontweight='bold')
    plt.tight_layout()  # 留出大标题空间

    # 显示图形
    plt.show()
