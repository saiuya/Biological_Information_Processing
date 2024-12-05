import numpy as np
import matplotlib.pyplot as plt
from read_txt import read_emg_data

# 读取文件数据
healthy_time, healthy_value = read_emg_data('./data/emg_healthy.txt')
neuropathy_time, neuropathy_value = read_emg_data('./data/emg_neuropathy.txt')
myopathy_time, myopathy_value = read_emg_data('./data/emg_myopathy.txt')


# 定义自相关函数
def compute_autocorrelation(signal):
    N= len(signal)
    result = np.correlate(signal, signal, mode='full')*(N*np.array(signal).std()*np.array(signal).std())  # 自相关计算
    result = result[result.size // 2:]  # 取后半部分
    result /= np.max(result)  # 归一化
    lags = np.arange(0, N)
    return lags, result


if __name__ == '__main__':

    # 计算自相关, 分析信号的周期性
    lags_healthy, autocorr_healthy = compute_autocorrelation(healthy_value)
    lags_neuropathy, autocorr_neuropathy = compute_autocorrelation(neuropathy_value)
    lags_myopathy, autocorr_myopathy = compute_autocorrelation(myopathy_value)




    # 创建图形并绘制自相关函数
    fig, axs = plt.subplots(3, 1, sharex=True)

    # Healthy 自相关
    axs[0].plot(lags_healthy, autocorr_healthy, label='Healthy', color='green')
    axs[0].set_title('Healthy Autocorrelation')
    axs[0].set_ylabel('Correlation')
    axs[0].grid(True)
    axs[0].legend()


    # Neuropathy 自相关
    axs[1].plot(lags_neuropathy, autocorr_neuropathy, label='Neuropathy', color='blue')
    axs[1].set_title('Neuropathy Autocorrelation')
    axs[1].set_ylabel('Correlation')
    axs[1].grid(True)
    axs[1].legend()


    # Myopathy 自相关
    axs[2].plot(lags_myopathy, autocorr_myopathy, label='Myopathy', color='red')
    axs[2].set_title('Myopathy Autocorrelation')
    axs[2].set_xlabel('Lag')
    axs[2].set_ylabel('Correlation')
    axs[2].grid(True)
    axs[2].legend()

    # 调整布局和标题
    # fig.suptitle('Autocorrelation of EMG Signals', fontsize=16, fontweight='bold')
    plt.tight_layout()  # 留出大标题空间

    # 显示图形
    plt.show()
