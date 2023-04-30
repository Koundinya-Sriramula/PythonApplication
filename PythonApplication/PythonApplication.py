from difflib import SequenceMatcher

with open(r"C:\Users\sriramula's\source\repos\sample1.txt") as first_file,open(r"C:\Users\sriramula's\source\repos\sample2.txt") as second_file:
      
    # Reading Both Text Files
    file1 = first_file.read()
    file2 = second_file.read()
      
    # Comparing Both Text Files
    dd= SequenceMatcher(None, file1,
                         file2).ratio()
      
    # converting decimal output in integer
    result = int(dd*100)
    print(f"{result}% Plagiarized Content")