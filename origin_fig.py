import matplotlib.pyplot as plt
from read_txt import read_emg_data

# number of samples
healthy_N = 50860
neuropathy_N = 147858
myopathy_N = 110337

dt_sec = 0.00025
Hz = 1/dt_sec



# 读取文件数据
healthy_time, healthy_value = read_emg_data('./data/emg_healthy.txt')
neuropathy_time, neuropathy_value = read_emg_data('./data/emg_neuropathy.txt')
myopathy_time, myopathy_value = read_emg_data('./data/emg_myopathy.txt')



if __name__ == '__main__':

    # 创建图形并绘制数据
    fig, axs = plt.subplots(3, 1, sharex=True)


    # 添加大标题
    # fig.suptitle('Comparison of EMG Signals')


    # Healthy 数据
    axs[0].plot(healthy_time, healthy_value, label='Healthy', color='green', alpha=0.7)
    axs[0].set_title('Healthy')
    axs[0].set_ylabel('Amplitude')
    axs[0].grid(True)
    axs[0].legend()


    # Neuropathy 数据
    axs[1].plot(neuropathy_time, neuropathy_value, label='Neuropathy', color='blue', alpha=0.7)
    axs[1].set_title('Neuropathy')
    axs[1].set_ylabel('Amplitude')
    axs[1].grid(True)
    axs[1].legend()



    # Myopathy 数据
    axs[2].plot(myopathy_time, myopathy_value, label='Myopathy', color='red', alpha=0.7)
    axs[2].set_title('Myopathy')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('Amplitude')
    axs[2].grid(True)
    axs[2].legend()

    # 调整布局
    plt.tight_layout()

    # 显示图形
    plt.show()
