"""
Name : Md. Ishraq Uddin Sikder
Email : nirzon.sikderbd@gmail.com 

"""

class Star_Cinema:
    hall_list = []
    def entry_hall(self, obj):
        self.hall_list.append(obj)
        
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        super().__init__()
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)
        
    def entry_show(self, id, movie_name, time):
        self.id = id
        self.movie_name = movie_name
        self.time = time
        self.show_list.append((id, movie_name, time))
        self.list = [['_' for i in range(self.cols)] for j in range(self.rows)]
        self.seats[id] = self.list
    
    def book_seats(self, id, tuple):
        for i in self.show_list:
            if i[0] == id:
                if tuple[0] < self.rows and tuple[1] < self.cols:
                    if self.seats[id][tuple[0]][tuple[1]] == '_':
                        self.seats[id][tuple[0]][tuple[1]] = '1'
                        print('The sit is booked for you successfully')
                    else:
                        print('Sorry, The sit is already booked') 
                else:
                    print('Invalid rows or cols')
            else:
                print('The id is not matched with the shows')
            break
    
    def view_show_list(self):
        for i in self.show_list:
            print('\nShow Id: ', i[0])
            print('Movie Name: ', i[1])
            print('Show Time: ', i[2])
            
    def view_available_seats(self, id):
        print('Available seats are marked with (_)')
        for i in self.show_list:
                if i[0] == id:
                    for x in range(self.rows):
                        for y in range(self.cols):
                            print(self.seats[id][x][y], end=' ')
                        print()
                else:
                    print('The id is not matched with the shows')
                break
        
class Counter(Hall):
    def __init__(self) -> None:
        print('\nWelcome to the Phitron Cinema Hall')
    
    def replica(self, obj):
        while True:
            print('\nMenu:')
            print('1. View all running shows')
            print('2. View avaiable seats')
            print('3. Book ticket')
            print('4. Exit')
            opt = int(input('Enter your choice : '))
            if opt == 1:
                obj.view_show_list()
            elif opt == 2:
                id= int(input('\nEnter the Show Id: '))
                obj.view_available_seats(id)
            elif opt == 3:
                id = int(input('\nEnter the Show Id: '))
                tuple = (int(input('Enter row number: ')),int(input('Enter column number: ')))
                obj.book_seats(id, tuple)  
            else:
                print('\nThank You')
                break
                                      
       
obj1 = Hall(5, 3, 1)
obj2 = Hall(7, 5, 2)
obj1.entry_show(111, 'Jawan', '10.50pm')
obj2.entry_show('222', 'Sujon', '02.50pm')
# obj1.book_seats('111', (4,2))
# obj2.book_seats('123', (4,5))
# obj1.view_show_list()
# obj2.view_show_list()
# obj1.view_available_seats('111')
# obj2.view_available_seats('222')
obj = Counter()
obj.replica(obj1)