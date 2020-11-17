fig = plt.figure(dpi=100)
ax = plt.axes()

xs = delta_gmst_by186[:15]
ys = net_toa_flux_by186[:15]

ax.scatter(xs,ys)#, s=8)
plt.plot(np.unique(xs), np.poly1d(np.polyfit(xs, ys, 1))(np.unique(xs)), c='darkgrey')

#plt.legend()
plt.xlabel('Delta T / K')
plt.ylabel(f'Net TOA flux / W m-2')
plt.title('Net TOA flux vs temp change 2015-2050')
#plt.savefig(f'{file_loc}ch4_grad_1985_2018.png') 

print(f'Gradient = {np.polyfit(xs, ys, 1)[0]:.2f}')
print(f'Offset = {np.polyfit(xs, ys, 1)[1]:.2f}')
