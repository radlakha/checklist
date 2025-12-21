import sys

def add_to_checklist(file_name):
    checklist_file = 'checklist.txt'
    
    with open(checklist_file, 'r') as file:
        checklist = file.read().splitlines()
    
    if file_name in checklist:
        print(f"{file_name} already exists in the checklist.")
        return
    
    with open(checklist_file, 'a') as file:
        file.write(file_name + '\n')
    
    print(f"{file_name} has been added to the checklist.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_to_checklist.py <file_name>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    add_to_checklist(file_name)
