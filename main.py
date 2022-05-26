class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name, age, tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = []
        self.score = float(score)
    
    def change_name(self, newName):
        self.name = newName
    
    def change_age(self, newAge):
        self.name = newAge

    def add_track(self, track):
        self.tracks.append(track)
    
    def get_score(self):
        return self.score


        
    
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
