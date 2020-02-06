def main():
	skills = ["counting", "reading", "drawing", "jumping", "napping", "solving deferential equations"]
	cv = {}
	cv['name'] = input("What's your name?  ")
	cv['age'] = input("What's your age?  ")
	cv['experience'] = input("How many years of experience do you have?  ")
	cv['skills'] = []
	n = 1
	for skill in skills:
		print(str(n) + ". " + skill)
		n += 1
	skill1 = input("Choose a skill from above by entering its number: ")
	skill2 = input("Choose another skill from above by entering its number: ")
	cv['skills'] = skills[int(skill1) - 1] + skills[int(skill2) - 1]
	if int(cv['age']) > 25 and int(cv['age']) < 40 and int(cv['experience']) > 5 and (int(skill1) == 6 or int(skill2) == 6):
		print("Congrats! you have been accepted.")
	else:
		print("You're rejected! apply again next time loser.")

if __name__ == '__main__':
	main()
