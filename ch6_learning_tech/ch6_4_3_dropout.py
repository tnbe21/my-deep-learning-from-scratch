import os
import sys

import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.pardir)

from dataset.mnist import load_mnist
from common.multi_layer_net_extend import MultiLayerNetExtend
from common.trainer import Trainer

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

x_train = x_train[:300]
t_train = t_train[:300]

# Dropout使用有無
# Dropoutを使用すると過学習を抑えられる
# 過学習の抑止=訓練データ認識率について100%から離れ、
# 訓練データ認識率とテストデータ認識率間の隔たりを狭める
use_dropout = True
dropout_ratio = 0.2

network = MultiLayerNetExtend(input_size=784, hidden_size_list=[100, 100, 100, 100, 100, 100],
        output_size=10, use_dropout=use_dropout, dropout_ratio=dropout_ratio)
trainer = Trainer(network, x_train, t_train, x_test, t_test, epochs=301,
        mini_batch_size=100, optimizer='sgd', optimizer_param={'lr': 0.01}, verbose=True)

trainer.train()

train_acc_list, test_acc_list = trainer.train_acc_list, trainer.test_acc_list

markers = {
    'train': 'o',
    'test': 's',
}
x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, marker='o', label='train', markevery=10)
plt.plot(x, test_acc_list, marker='s', label='test', markevery=10)
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()
