# Code to plot all the stuff for the theta scheme

from solver import Solver
import numpy as np 
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import pandas as pd

def main():
    parser = ArgumentParser()
    parser.add_argument('--plot','-p',action="store_true")
    parser.add_argument('--save','-s',action="store_true")
    args = parser.parse_args()

    time = [0.01,0.75,2,3]
    space = [16,32,64,128]
    a, eta, theta = 1, 1, 0.5
    data = []
    analytic = []
    for i in range(len(time)):
        T = time[i]
        data.append([])
        for N in space:
            solver = Solver(a, eta, theta, N, T)
            x, v = solver.run()
            e = solver.get_errors()
            data[i].append([x,v,e])

        xx, uu = solver.get_analytic()
        analytic.append([xx,uu])

    # //			Error Semilog Plots
    # // #######################################################################
    fig, axs = plt.subplots(2,2,figsize=(12,8))
    fig.tight_layout(pad=3)
    rows = [0,0,1,1]
    cols = [0,1,0,1]
    for i in range(4):
        col = cols[i]
        row = rows[i]
        T = time[i]
        d = data[i]

        for k in range(4):
            x = d[k][0]
            e = d[k][2]
            N = space[k]
            axs[row][col].plot(x, abs(e), marker='.', linestyle='dashed',  label=f'N = {N}')
        if row==1:
            axs[row][col].set_xlabel('x')
        if col==0:
            axs[row][col].set_ylabel('abs(Error)')
        axs[row][col].set_yscale('log')
        axs[row][col].set_title(f'T={T}')
        axs[row][col].legend()
    if args.plot:
        plt.show()
    if args.save:
        plt.savefig('error_semilog_plots.pdf')

    # //			Exact vs. Approximate Plots
    # // #######################################################################
    fig, axs = plt.subplots(2,2,figsize=(12,8))
    fig.tight_layout(pad=3)
    rows = [0,0,1,1]
    cols = [0,1,0,1]
    for i in range(4):
        col = cols[i]
        row = rows[i]
        T = time[i]
        d = data[i]

        [xx,uu] = analytic[i]
        axs[row][col].plot(xx,uu, label='Exact')
        for k in range(4):
            x = d[k][0]
            v = d[k][1]
            N = space[k]
            axs[row][col].plot(x, v, marker='.', linestyle='dashed',  label=f'N = {N}')
        if row==1:
            axs[row][col].set_xlabel('x')
        if col==0:
            axs[row][col].set_ylabel('y')
        axs[row][col].set_title(f'T={T}')
        axs[row][col].set_ylim([-1,1])
        axs[row][col].legend()
    if args.plot:
        plt.show()
    if args.save:
        plt.savefig('exact_v_approx.pdf')

    # //			Max Error v. N plots
    # // #######################################################################
    fig, axs = plt.subplots(2,2,figsize=(9,6), sharex=True, sharey=True)
    fig.tight_layout(pad=3)
    rows = [0,0,1,1]
    cols = [0,1,0,1]
    for i in range(4):
        col = cols[i]
        row = rows[i]
        T = time[i]
        d = data[i]

        #Calculate RMSE
        errorlist = []
        orderlist = [np.nan]
        for k in range(4):
            x = d[k][0]
            err = d[k][2]
            N = space[k]
            error = max(abs(err))
            errorlist.append(error)
            if k > 0:
                order = np.log(errorlist[k-1]/error)/np.log(N/space[k-1])
                orderlist.append(order)

        table = pd.DataFrame({'N':space, 'Error':errorlist, 'Order':orderlist})
        if args.plot:
            print(table)
        if args.save:
            table.to_csv(f'error_table_T={T}.csv', index=False)

        axs[row][col].plot(space, errorlist, marker='.', linestyle='dashed')
        if row==1:
            axs[row][col].set_xlabel('N')
        if col==0:
            axs[row][col].set_ylabel('Max Error')
        axs[row][col].set_title(f'T={T}')
        axs[row][col].set_yscale('log')
        axs[row][col].set_xscale('log', base = 2)

    if args.plot:
        plt.show()
    if args.save:
        plt.savefig('error_v_n.pdf')
        


if __name__=="__main__":
    main()