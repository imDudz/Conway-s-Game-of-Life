import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

cellOn = 255
cellOff = 0
vals = [cellOn, cellOff]

def randomGrid(grideSize):
	return np.random.choice(vals, grideSize*grideSize, p=[0.2, 0.8]).reshape(grideSize, grideSize)

def addGlider(i, j, grid):
	glider = np.array([[0, 0, 255],
		[255, 0, 255],
		[0, 255, 255]])
	grid[i:i+3, j:j+3] = glider

def addGosperGliderGun(i, j, grid):
	gun = np.zeros(11*38).reshape(11, 38)

	gun[5][1] = gun[5][2] = 255
	gun[6][1] = gun[6][2] = 255

	gun[3][13] = gun[3][14] = 255
	gun[4][12] = gun[4][16] = 255
	gun[5][11] = gun[5][17] = 255
	gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = 255
	gun[7][11] = gun[7][17] = 255
	gun[8][12] = gun[8][16] = 255
	gun[9][13] = gun[9][14] = 255

	gun[1][25] = 255
	gun[2][23] = gun[2][25] = 255
	gun[3][21] = gun[3][22] = 255
	gun[4][21] = gun[4][22] = 255
	gun[5][21] = gun[5][22] = 255
	gun[6][23] = gun[6][25] = 255
	gun[7][25] = 255

	gun[3][35] = gun[3][36] = 255
	gun[4][35] = gun[4][36] = 255

	grid[i:i+11, j:j+38] = gun

def update(frameNum, img, grid, grideSize):
	newGrid = grid.copy()
	for i in range(grideSize):
		for j in range(grideSize):
			total = int((grid[i, (j-1)%grideSize] + grid[i, (j+1)%grideSize] +
				grid[(i-1)%grideSize, j] + grid[(i+1)%grideSize, j] +
				grid[(i-1)%grideSize, (j-1)%grideSize] + grid[(i-1)%grideSize, (j+1)%grideSize] +
				grid[(i+1)%grideSize, (j-1)%grideSize] + grid[(i+1)%grideSize, (j+1)%grideSize])/255)

			#Apply Conway's rules
			if grid[i, j] == cellOn:
				if (total < 2) or (total > 3):
					newGrid[i, j] = cellOff
			else:
				if total == 3:
					newGrid[i, j] = cellOn

	#Update data
	img.set_data(newGrid)
	grid[:] = newGrid[:]
	return img

def main():
	grideSize = 100
	updateInterval = 50
	grid = randomGrid(grideSize)
    #Set animation
	fig, ax = plt.subplots()
	img = ax.imshow(grid, interpolation='nearest')
	ani = animation.FuncAnimation(fig, update, fargs=(img, grid, grideSize, ),
		frames = 10,
		interval=updateInterval,
		save_count=50)

	plt.show()

#Call main
if __name__ == '__main__':
	main()