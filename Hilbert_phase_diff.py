import numpy as np
import matplotlib.pyplot as plt
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

# 计算两两之间的相位差
phase_diff_nh = phase_neuropathy - phase_healthy  # Neuropathy vs Healthy
phase_diff_nm = phase_neuropathy - phase_myopathy  # Neuropathy vs Myopathy
phase_diff_hm = phase_healthy - phase_myopathy  # Healthy vs Myopathy


if __name__ == '__main__':

    # 创建图形并绘制相位差
    fig, axs = plt.subplots(3, 1, sharex=True)

    # Neuropathy vs Healthy
    axs[0].plot(neuropathy_time_trimmed, phase_diff_nh, label='Phase Difference: Neuropathy vs Healthy', color='blue')
    axs[0].set_title('Phase Difference: Neuropathy vs Healthy')
    axs[0].set_ylabel('Phase Difference (radians)')
    axs[0].grid(True)
    axs[0].legend()

    # Neuropathy vs Myopathy
    axs[1].plot(neuropathy_time_trimmed, phase_diff_nm, label='Phase Difference: Neuropathy vs Myopathy', color='red')
    axs[1].set_title('Phase Difference: Neuropathy vs Myopathy')
    axs[1].set_ylabel('Phase Difference (radians)')
    axs[1].grid(True)
    axs[1].legend()

    # Healthy vs Myopathy
    axs[2].plot(neuropathy_time_trimmed, phase_diff_hm, label='Phase Difference: Healthy vs Myopathy', color='green')
    axs[2].set_title('Phase Difference: Healthy vs Myopathy')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('Phase Difference (radians)')
    axs[2].grid(True)
    axs[2].legend()

    # 调整布局和标题
    # fig.suptitle('Phase Differences Between EMG Signals', fontsize=16, fontweight='bold')
    plt.tight_layout()  # 留出大标题空间

    # 显示图形
    plt.show()
