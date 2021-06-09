class Member:

    def __init__(self, name, age, classroom, scores):
        self.name = name
        self.age = age
        self.classroom = classroom
        self.role = "Student"
        self.scores = scores
    
    def averageTestScore(self):
        var = 0
        for i in range(len(scores)):
            var += scores[i]
        return int((var)/len(scores))

scores = [10,8,9,5]
student1 = Member("Tommy","20","2A",scores)

print(str(getattr(student1, "name")) + " got " + str(student1.averageTestScore()) + " on avergage!")

