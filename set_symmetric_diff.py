# using ^ operator
# morning = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
# afternoon = {'Python', 'C#', 'Java', 'C', 'Ruby'}
#
# possible_courses = morning ^ afternoon
# print(possible_courses)

# Converting lists to sets and using symmetric_difference method
morning = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon = ['Python', 'C#', 'Java', 'C', 'Ruby']

possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)

# Example for symmetric_difference is commutative
possible_courses = set(afternoon).symmetric_difference(morning)
print(possible_courses)
