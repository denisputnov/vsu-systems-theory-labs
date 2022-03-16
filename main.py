from hall import MontyHall


if __name__ == '__main__':
	monty_hall = MontyHall()

	monty_hall.start()
	print(monty_hall)

	monty_hall.reset()
	monty_hall.switch_mode()

	monty_hall.start()
	print(monty_hall)
