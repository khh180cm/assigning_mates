import random

def put_members():
	total_number = int(input('전체 멤버수를 입력하시오. : '))
	member_set = set()
	for i in range(1, total_number + 1):
		user_input = input('멤버 이름을 입력하시오. : ')	
		while user_input in member_set or user_input == '':
			user_input = input('중복 또는 공백입력입니다. 다시 입력하시오. : ')

		member_set.add(user_input)	
		print(f'{i}명 입력했습니다.')
	return member_set, total_number
	
def make_mates(member_set, total_number):
	#2명씩인지, 3명씩인지 등
	num_per_mate = int(input('각 짝궁의 멤버 수를 입력하시오. : ')) 
	member_list = list(member_set)	
	
	member_dict = dict()
	total_team = total_number // num_per_mate
	remainder = total_number % num_per_mate
	
	for team in range(1, total_team+1):
		tmp_list = list()
		for num in range(num_per_mate):
			tmp = member_list.pop(random.randint(0, len(member_list)-1))
			tmp_list.append(tmp) 
			team = str(team)
			member_dict[team+'team'] = tmp_list
	
	while remainder != 0:
		rand_team = random.randint(1, total_team)
		rand_team = str(rand_team)
		member_dict[rand_team+'team'].append(member_list.pop())
		remainder -= 1	
	return member_dict

def display(member_dict):
	print(member_dict)

if __name__ == '__main__':
	member_set, total_number = put_members()
	result = make_mates(member_set, total_number)
	display(result)
