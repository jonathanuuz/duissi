   json1 = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Charlie'}]
   json2 = [{'id': 101, 'age': 30}, {'id': 102, 'age': 25}]

   filtered_pairs = [(item1, item2) for item1, item2 in zip(json1, json2) if item1['id'] % 2 == 0]

   print(filtered_pairs)
   