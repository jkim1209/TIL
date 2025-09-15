import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

def linear_single_theta_gdm(x, y, theta=1, rate=0.1, epochs=100, graph_on=True):
    """
    Returns theta that explains linear relationship y = theta * x
    after updating epochs times using gadient descent method.
    
    Args:
        x (list)        :   list of x values
        y (list)        :   list of y values
        theta (float)   :   initial theta, default is 1
        rate (float)    :   initial learning rate, default is 0.1
        epochs (int)    :   number of iteration, default is 100
        graph_on (bool) :   visualize theta and loss for each epoch, default is True

    Returns:
        theta_list: list of updated learning rates
        loss_lost: list of updated squared errors
    """
    theta_list = []
    loss_list = []
    data = list(zip(x,y))

    for epoch in range(epochs):
        for x,y in data:
            pred = theta * x
            loss = (y-pred) ** 2

            theta_list.append(theta)
            loss_list.append(loss)

            theta = theta + 2*rate*x*(y-pred)

    if graph_on:
        fig, ax = plt.subplots(2, 1, figsize = (20,10))
        ax[0].plot(theta_list)
        ax[1].plot(loss_list)
        ax[0].set_title(r'$\theta$', fontsize = 30)
        ax[1].set_title(r'$\mathcal{L}$', fontsize = 30)
        for ax_idx in range(2):
            ax[ax_idx].tick_params(axis = 'both', labelsize = 20)
        plt.tight_layout()
        plt.show()

    return theta_list, loss_list


if __name__ == '__main__':
    x = np.array([1, 0.5, 3])
    y = 3*x
    theta = 0.1
    rate = 0.01
    epochs = 50
    theta_list, loss_list = linear_single_theta_gdm(x, y, theta, rate, epochs, graph_on=True)
    print(theta_list)
    print(loss_list)
    