import matplotlib.pyplot as plt
from scipy.signal import butter, sosfiltfilt

from origin_fig import healthy_value, neuropathy_value, myopathy_value, neuropathy_time, healthy_time, myopathy_time


# 定义低通滤波器
def low_pass_filter(data, cutoff, fs, order=4):
    nyquist = 0.5 * fs  # 奈奎斯特频率
    normal_cutoff = cutoff / nyquist  # 归一化截止频率
    sos = butter(order, normal_cutoff, btype='low', analog=False, output='sos')  # 使用sos形式
    filtered_data = sosfiltfilt(sos, data)  # 应用滤波
    return filtered_data


# 采样频率和截止频率
sampling_rate = 1 / (neuropathy_time[1] - neuropathy_time[0])  # 假设所有信号采样率相同
cutoff_frequency = 50  # 截止频率 50 Hz

# 应用低通滤波
neuropathy_filtered = low_pass_filter(neuropathy_value, cutoff_frequency, sampling_rate)
healthy_filtered = low_pass_filter(healthy_value, cutoff_frequency, sampling_rate)
myopathy_filtered = low_pass_filter(myopathy_value, cutoff_frequency, sampling_rate)

if __name__ == '__main__':
    # 创建图形
    fig, axs = plt.subplots(3, 1, sharex=True)

    # Healthy
    axs[0].plot(healthy_time, healthy_value, label='Original Healthy', color='green', alpha=0.7)
    axs[0].plot(healthy_time, healthy_filtered, label='Filtered Healthy', color='lime', alpha=0.7)
    axs[0].set_title('Healthy Signal (Original vs Filtered)')
    axs[0].set_ylabel('Amplitude')
    axs[0].grid(True)
    axs[0].legend()
    
    # Neuropathy
    axs[1].plot(neuropathy_time, neuropathy_value, label='Original Neuropathy', color='blue', alpha=0.7)
    axs[1].plot(neuropathy_time, neuropathy_filtered, label='Filtered Neuropathy', color='cyan', alpha=0.7)
    axs[1].set_title('Neuropathy Signal (Original vs Filtered)')
    axs[1].set_ylabel('Amplitude')
    axs[1].grid(True)
    axs[1].legend()


    # Myopathy
    axs[2].plot(myopathy_time, myopathy_value, label='Original Myopathy', color='red', alpha=0.7)
    axs[2].plot(myopathy_time, myopathy_filtered, label='Filtered Myopathy', color='orange', alpha=0.7)
    axs[2].set_title('Myopathy Signal (Original vs Filtered)')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('Amplitude')
    axs[2].grid(True)
    axs[2].legend()

    # 调整布局和标题
    fig.suptitle('Low-Pass Filtered EMG Signals', fontsize=16, fontweight='bold')
    plt.tight_layout()  # 留出大标题空间

    # 显示图形
    plt.show()
