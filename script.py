import datetime

def read_checklist(file_path):
    checklist = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().rsplit(' - ', 1)
            if len(parts) == 2:
                file_name, due_date = parts
                if due_date:
                    due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
                else:
                    due_date = None
            else:
                file_name = parts[0]
                due_date = None
            checklist.append((file_name, due_date))
    return checklist

def display_checklist(checklist):
    for file_name, due_date in checklist:
        if due_date:
            print(f"{file_name} - Due: {due_date}")
        else:
            print(f"{file_name} - No due date")

if __name__ == "__main__":
    checklist = read_checklist('checklist.txt')
    display_checklist(checklist)
