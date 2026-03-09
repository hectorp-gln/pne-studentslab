student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

#The student's name#

print("Name:",student["name"])

#The number of subjects they are enrolled in

print("Number of subjetcs:", len(student["subjects"]))

#Whether "PNE" is in their subjects list

print("Enrolled in PNE:", bool("PNE" in student["subjects"]))

#Their grade in Databases

print("Databases grade:", student["grades"]["Databases"])

#Their average grade across all subjects (rounded to 2 decimals)

total = 0
n = len(student["subjects"])
for subject in student["subjects"]:
    total += student["grades"][subject]
print("Average grade:", round(total/n,2))

#All subject-grade pairs, one per line

print("Subject grades:")
for subject in student["subjects"]:
    print("  ",subject, "->", student["grades"][subject])