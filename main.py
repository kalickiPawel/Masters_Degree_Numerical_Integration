#!/usr/bin/env python
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

from modules import ObjLoader


def draw_plot(function, a, b, i):
    np.random.seed(19680801)
    data = np.random.randn(2, 100)
    x = np.arange(a, b, 0.01)
    f = eval(function)

    fig, axs = plt.subplots(2, 2, figsize=(5, 5))
    axs[0, 0].hist(data[0])
    axs[1, 0].scatter(data[0], data[1])
    axs[0, 1].plot(x, f)
    axs[1, 1].hist2d(data[0], data[1])

    plt.show()


def integrate(function, a, b, i):
    dx = (b - a) / i
    integrator = 0
    for x in range(i):
        x = x * dx + a
        integrator += dx * eval(function)
    # draw_plot(function, a, b, i)
    return integrator


def main(args):
    # function = input("Funkcja: ")
    # a = float(input("Początek przedziału: "))
    # b = float(input("Koniec przedziału: "))
    # i = int(input("Liczba podprzedziałów: "))
    # print("Całka z funkcji {function} po przedziale od {a} do {b} = {integrate}".format(
    #     function=function,
    #     a=a,
    #     b=b,
    #     integrate=integrate(function, a, b, i))
    # )
    obj = ObjLoader()
    obj.load_model("models/example.obj")
    print(obj.model.shape)

    x = []
    y = []
    z = []
    for i in range(len(obj.model)):
        if i % 3 == 0:
            x.append(obj.model[i])
        if i % 3 == 1:
            y.append(obj.model[i])
        if i % 3 == 2:
            z.append(obj.model[i])

    x, y, z = np.array(obj.v)[:,:3].T
    I, J, K = np.array(obj.f).T

    mesh = go.Mesh3d(x=-x, y=z, z=y, i=I, j=J, k=K, color='lightpink', opacity=0.50)
    layout = go.Layout(title='Mesh3d from a Wavefront obj file')
    fig = go.Figure(data=[mesh], layout=layout)
    t = np.linspace(0, 10, 50)
    x1, y1, z1 = np.cos(t), np.sin(t), t
    fig.add_trace(
        go.Scatter3d(x=x1, y=y1, z=z1,
                     mode='lines'))

    fig.show()
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # # for i in range(len(x)):
    # #     ax.scatter(x[i], y[i], z[i])
    # ax.scatter(x,y,z)
    # plt.show()
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
