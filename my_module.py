# my_module.py


def is_letter(character):
    return character.isalpha()


def convert_to_lowercase(character):
    return character.lower()


def calculate_letter_frequency(text):
    total_letters = sum(text.count(letter) for letter in 'abcdefghijklmnopqrstuvwxyz')
    frequency_dict = {letter: text.count(letter) / total_letters * 100 for letter in 'abcdefghijklmnopqrstuvwxyz'}
    return frequency_dict


def display_info():
    student_name = "Mehmet Akif"
    student_surname = "BAYRAK"
    student_number = "211213065"
    note = "Sevelim sevilelim"

    print(f"Öğrenci : {student_name} {student_surname}")
    print(f"Öğrenci numarası : {student_number}")
    print(f"Not :{note}")