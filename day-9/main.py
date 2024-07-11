# WAP to grade students based on their marks.
student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]

    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Exceptation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

# WAP
travel_log = [
    {
        "country" : "India",
        "total_visits" : 12,
        "cities_visited" : ["delhi", "mumbai"],
    },
    {
        "country" : "Korea",
        "total_visits" : 2,
        "cities_visited" : ["seoul", "busan"],
    },
]

def add_country(place, visits, cities):
    new_country = {}
    new_country["country"] = place
    new_country["total_visits"] = visits
    new_country["cities_visited"] = cities

    travel_log.append(new_country)

add_country( place = "USA", visits = 20, cities = ["new york", "california", "los angelas", "las vegas"])
print(travel_log)