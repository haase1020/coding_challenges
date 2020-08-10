// print out each element of the following array on a separate line:
//["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]



function nested_print(arr) {
    for element in arr {
      if type(element) == Array {
        nested_print(element)
      } else {
        print(element)
      }
    }
  }