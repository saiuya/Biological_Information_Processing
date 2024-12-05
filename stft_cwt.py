import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft, cwt, morlet
from mixed_signal import combined_neuropathy, combined_healthy, combined_myopathy, neuropathy_time, healthy_time, myopathy_time

# 定义CWT的小波函数
def cwt_transform(signal_cwt, widths):
    return cwt(signal_cwt, morlet, widths)

# 设置CWT参数
wavelet_widths = np.arange(1, 100)

# 设置STFT参数
nperseg = 8  # 每段的点数


if __name__ == '__main__':

    # 图形布局
    fig, axs = plt.subplots(3, 2, figsize=(14, 8))

    # 数据列表
    combined_signals = [combined_healthy, combined_neuropathy, combined_myopathy]
    times = [healthy_time, neuropathy_time, myopathy_time]
    titles = ['Healthy', 'Neuropathy', 'Myopathy']

    # 遍历每个信号进行变换和绘图
    for i, (signal, time, title) in enumerate(zip(combined_signals, times, titles)):
        # STFT
        f, t, Zxx = stft(signal, fs=1/(time[1] - time[0]), nperseg=nperseg)
        axs[i, 0].pcolormesh(t, f, np.abs(Zxx), shading='gouraud')
        axs[i, 0].set_title(f'{title} STFT')
        axs[i, 0].set_ylabel('Frequency (Hz)')
        axs[i, 0].set_xlabel('Time (s)')
        axs[i, 0].grid(True)

        # CWT
        cwt_result = cwt_transform(signal, wavelet_widths)
        axs[i, 1].imshow(
            np.abs(cwt_result),
            extent=[time[0], time[-1], wavelet_widths[-1], wavelet_widths[0]],
            aspect='auto',
            cmap='jet'
        )
        axs[i, 1].set_title(f'{title} CWT')
        axs[i, 1].set_ylabel('Scale')
        axs[i, 1].set_xlabel('Time (s)')
        axs[i, 1].grid(True)

    # 调整布局
    fig.suptitle('STFT and CWT of Mixed Signals', fontsize=16, fontweight='bold')
    plt.tight_layout()  # 留出大标题空间

    # 显示图形
    plt.show()
