import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    person=record[0]
    friend=record[1]
    mr.emit_intermediate(person,friend)
    if friend in mr.intermediate and person in mr.intermediate.get(friend):
        mr.intermediate.get(friend).append(person)
        mr.intermediate.get(person).append(friend)



def reducer(person, list_of_friends):
    # key: word
    # value: list of occurrence counts
    for friend in list_of_friends:
	if list_of_friends.count(friend)==1:
            mr.emit((friend,person))
            mr.emit((person,friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  print mr.intermediate
