from collections import defaultdict
def mapper(word):
    return word, 1
def reducer(key_value_pair):
    key, values = key_value_pair
    return key, sum(values)
def map_reduce_function(input_list, mapper, reducer):
    map_results = map(mapper, input_list)
    shuffler = defaultdict(list)
    for key, value in map_results:
        shuffler[key].append(value)
    return map(reducer, shuffler.items())
words = "python best language".split(" ")
result = list(map_reduce_function(words, mapper, reducer))
print(result)
