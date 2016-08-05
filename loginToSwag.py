def login(driver):
	config = open('../SearchTheSwagConfig/config.txt', 'r')
		
	credentials = config.read().splitlines()

	config.close()

	username = driver.find_element_by_id('sbxJxRegEmail')
	username.send_keys(credentials[0])	

	password = driver.find_element_by_id('sbxJxRegPswd')
	password.send_keys(credentials[1] + '\n')
