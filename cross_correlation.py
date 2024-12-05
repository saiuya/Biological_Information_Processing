import numpy as np
import matplotlib.pyplot as plt
from origin_fig import healthy_value, neuropathy_value, myopathy_value



# 找到最短信号的长度
min_length = min(len(neuropathy_value), len(healthy_value), len(myopathy_value))

# 对信号进行截断以匹配最短长度
neuropathy_value_trimmed = neuropathy_value[:min_length]
healthy_value_trimmed = healthy_value[:min_length]
myopathy_value_trimmed = myopathy_value[:min_length]

# 定义互相关函数
def compute_cross_correlation(signal1, signal2):
    n = len(signal1)
    result = np.correlate(signal1, signal2, mode='full')  # 互相关计算
    lags = np.arange(-n + 1, n)  # 滞后范围，与结果长度对齐
    return lags, result

# 计算互相关
lags_nh, crosscorr_nh = compute_cross_correlation(neuropathy_value_trimmed, healthy_value_trimmed)  # Neuropathy vs Healthy
lags_nm, crosscorr_nm = compute_cross_correlation(neuropathy_value_trimmed, myopathy_value_trimmed)  # Neuropathy vs Myopathy
lags_hm, crosscorr_hm = compute_cross_correlation(healthy_value_trimmed, myopathy_value_trimmed)  # Healthy vs Myopathy


if __name__ == '__main__':
    
    # 创建图形
    fig, axs = plt.subplots(3, 1, sharex=True)

    # Neuropathy vs Healthy
    axs[0].plot(lags_nh, crosscorr_nh, label='Neuropathy vs Healthy', color='blue')
    axs[0].set_title('Cross-Correlation: Neuropathy vs Healthy')
    axs[0].set_ylabel('Correlation')
    axs[0].grid(True)
    axs[0].legend()

    # Neuropathy vs Myopathy
    axs[1].plot(lags_nm, crosscorr_nm, label='Neuropathy vs Myopathy', color='red')
    axs[1].set_title('Cross-Correlation: Neuropathy vs Myopathy')
    axs[1].set_ylabel('Correlation')
    axs[1].grid(True)
    axs[1].legend()

    # Healthy vs Myopathy
    axs[2].plot(lags_hm, crosscorr_hm, label='Healthy vs Myopathy', color='green')
    axs[2].set_title('Cross-Correlation: Healthy vs Myopathy')
    axs[2].set_xlabel('Lag')
    axs[2].set_ylabel('Correlation')
    axs[2].grid(True)
    axs[2].legend()

    # 调整布局和标题
    # fig.suptitle('Cross-Correlation of EMG Signals', fontsize=16, fontweight='bold')
    plt.tight_layout()  # 留出大标题空间

    # 显示图形
    plt.show()
