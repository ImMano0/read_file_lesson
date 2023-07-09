#Rread file and convert to list
def read_file(filename: str) -> list[int]:
    """
    Reads a file and returns a list of integers.

    Args:
        filename (str): The name of the file to read.
    Returns:
        data (list): A list of integers from the file.
    """
    # Open the file
    # Read the file
    w = []
    for i in filename.split(","):
        w.append(int(i))
    return w 

#Print list from file
w = open('data.txt')
data = w.read() 
w.close()

print(read_file(data))
