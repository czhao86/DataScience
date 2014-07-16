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


def reducer(person, list_of_friends):
    # key: word
    # value: list of occurrence counts
    num=0
    for fri in list_of_friends:
	num+=1
    mr.emit((person,num))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
