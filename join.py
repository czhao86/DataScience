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
    key=record[1]
    value=record
    mr.emit_intermediate(key,value)


def reducer(key, list_of_records):
    # key: word
    # value: list of occurrence counts
    ans=[]
    for record in list_of_records:
        for temp in list_of_records:
            if record[0]=="order" and record[0]!=temp[0]:
		mr.emit(record+temp)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
