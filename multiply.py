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
    if record[0]=='a':
	for i in range(0,5):
            mr.emit_intermediate(record[1]*5+i,record)
    else:
        for j in range(0,5):
	    mr.emit_intermediate(record[2]+5*j,record)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    ans=0
    for value in list_of_values:
	for temp in list_of_values:
	    if value[0]=='a' and temp[0]=='b' and value[2]==temp[1]:
		ans+=value[3]*temp[3]
    mr.emit((key/5,key%5,ans))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  print mr.intermediate
