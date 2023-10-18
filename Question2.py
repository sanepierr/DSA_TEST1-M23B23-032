# Create two separate lists named catholic_martyrs and anglican_martyrs containing the names of Catholic and Anglican martyrs respectively.

catholic_martyrs = ['Achileo Kiwanuka', 'Adolphus Ludigo', 'Mukasa', 'Ambrosius Kibuuka', 'Anatoli Kiriggwajjo', 'Andrew Kaggwa', 'Antanansio Bazzekuketta', 'Bruno Sserunkuuma', 'Charles Lwanga', 'Denis Ssebuggwawo', 'Wasswa', 'Gonzaga Gonza', 'Gyavira Musoke', 'Yowana Mukiibi', 'Yusufu Lugalama', 'Zakayo Lubega', 'James Buuzaabalyaawo', 'John Maria Muzeeyi', 'Joseph Mukasa', 'Kizito', 'Lukka Baanabakintu', 'Matiya Mulumba', 'Mbaga Tuzinde', 'Mugagga Lubowa', 'Mukasa Kiriwawanvu', 'Nowa Mawaggali', 'Ponsiano Ngondwe', 'Eria Sebukyala', 'Fredrick Kizza', 'James Hannington', 'Matia Mulumba', 'Samwiri Mukasa', 'Yefusa Namayanja', 'Yosefu Lugalama', 'Yowana Maria', 'George Kizza', 'Janani Luwum', 'Joseph Balikuddembe', 'Kizito', 'Mark Kakumba', 'Nuhu Mbegu', 'Robert Munyagayirwa', 'Yohana Mukasa', 'Yowana Kitaka', 'Mukasa']

anglican_martyrs = ['Aaron Lubega', 'Apollo Kivebulaya']


#Question 2
print("# Identify and remove any duplicate names present in both lists.")

duplicate_names = set(catholic_martyrs).intersection(anglican_martyrs)
for name in duplicate_names:
    catholic_martyrs.remove(name)
    anglican_martyrs.remove(name)

# Print the lists after removing the duplicate names
print(f"Catholic martyrs: {catholic_martyrs}")
print(f"Anglican martyrs: {anglican_martyrs}")

#Question 3
# Write a function named martyr_count that takes in a martyr's name as an argument and returns the group (Catholic or Anglican) to which the martyr belongs.

def martyr_count(martyr_name):
    if martyr_name in catholic_martyrs:
        return "Catholic"
    elif martyr_name in anglican_martyrs:
        return "Anglican"
    else:
        return "Not a martyr"


#Question 4
# Using the function from task 3, determine the group of the martyr named "Kizito".

kizito_group = martyr_count("Kizito")
print(kizito_group)


#Question 5
# Write a Python function that returns True if the input string matches names of the Uganda Martyrs in both lists

def is_uganda_martyr(name):
    return name in catholic_martyrs or name in anglican_martyrs

#example:

martyr_name = "Kizito"
is_martyr = is_uganda_martyr(martyr_name)

if is_martyr:
    print(f"{martyr_name} is a Uganda Martyr.")
else:
    print(f"{martyr_name} is not a Uganda Martyr.")