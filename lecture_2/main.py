user_name=input('Enter your full name: ')
birth_year_str=input('Enter your birth year: ')
birth_year=int(birth_year_str)
current_age=int(2025-birth_year)

def generate_profile(current_age):

    """Эта функция сравнивает возраст пользователя и возвращает значение его этапа жизни соответственно"""

    if current_age>=0 and current_age<=12:
        return 'Child'
    if current_age>=13 and current_age<=19:
        return 'Teenager'
    if current_age>=20:
        return 'Adult'

life_stage=str(generate_profile(current_age))

hobbies_1=''
hobbies=[]
while hobbies_1!='stop':
        """Этот цикл позволяет вводить хобби пользователя.
         
         Хобби добавляется в конец списка.
         Пользователь вводит свои хобби до тех пор,
         пока он не введет с клавиватуры stop.
         """

        hobbies_1=input('Enter a favorite hobby or type \'stop\' to finish: ')
        if hobbies_1 != 'stop':
            hobbies.append(hobbies_1)

user_profile={
    'Name':user_name,
    'Age':current_age,
    'Life Stage':life_stage
}

print('Profile Summary: ')
for key, value in user_profile.items():
        """Этот цикл выводит ключи и значения словаря user_profile."""
        print(f"{key}: {value}")

if len(hobbies) != 0:
    """На этом этапе проверяется пустой ли список.
    
     Если список непустой, то выводится на экран хобби, которые ввел пользователь, 
     иначе на экрн будет выводится сообщение о том, что пользователь не упомянул никаких увлечений
     """

    print(f"Favorite Hobbies ({len(hobbies)}):")
    for i in range(len(hobbies)):
        """Этот цикл выводит на экран элементы списка hobbies, пока не закончится список."""

        print(f"-{hobbies[i]}")
else:
    print(f"You didn't mention any hobbies.")