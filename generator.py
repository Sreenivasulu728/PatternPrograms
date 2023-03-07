import random
name=['chinni','bunny','pinni','sunny','vinny']
subject=['python','django','drf','datascience','devops']

def people_list(num_of_people):
    results=[]
    for i in range(num_of_people):
        person={
        'id':i,
        'name':random.choice(name),
        'subject':random.choice(subject)
        }
        results.append(person)
    return results
people=people_list(2)
print(people)

