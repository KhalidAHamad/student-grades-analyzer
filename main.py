import analyze

grades_file = open("test_files/grades_small.csv", "r")

# read a file and turn the grades into a list
grades = analyze.get_grades(grades_file)
print(grades)

# create a grades range
grade_ranges = analyze.generate_grade_ranges()
print(grades_hist)

# Write a histo to file
