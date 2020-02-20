def solution():
	# 画拟合直线
	x=np.linspace(-10,10,100) ##在0-15直接画100个连续点
	y=x*x ##函数式
	plt.plot(x,y,color="red",linewidth=2)#label="solution line",
	plt.legend() #绘制图例
	plt.show()

solution()
