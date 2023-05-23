import random

class State:
    def __init__(self, time, resource_influence, deadline_influence=None ) -> None:
        self.time = time
        self.resource_influence = resource_influence
        self.deadline_influence = deadline_influence

class FSM:

    EAT = State(1, 30)
    CLASSES = State(1, -20)
    HOMEWORK = State(2, -20, -1)
    LEISURE = State(2, 15)

    PINK = '\033[95m'
    RESET = '\033[0m'

    def __init__(self, student) -> None:
        self.student = student
        self.cur_time = None

    def run(self):
        self.start_the_day()

    def start_the_day(self):
        rand = random.random()
        print(f"{FSM.PINK}THE DAY OF LIFE OF A STUDENT{FSM.RESET}")
        if rand <= 0.9:
            print('7:00: I woke up on time. Ready to start a new day!')
            self.cur_time = 8
            self.eat()
        elif (rand > 0.9) and (rand < 0.98):
            print("8.00: Oh, no! I overslept. I need to hurry up!")
            self.cur_time = 9
            self.attending_classes()
        else:
            print("8.00: I feel so bad..It seems like I have a cold. I need to stay at home today :(")

    def eat(self):
        self.student.energy += FSM.EAT.resource_influence
        print(f"{self.cur_time}:00: Eating")
        self.cur_time += FSM.EAT.time

        self.student.energy = min(self.student.energy, 100)
        if self.cur_time >= 22:
            self.sleep()


        if random.random() < 0.6 and self.cur_time <= 15:
            self.attending_classes()
        else:
            self.doing_homework()

    def attending_classes(self):
        self.student.energy += FSM.CLASSES.resource_influence
        print(f"{self.cur_time}:00: Attending classes")
        self.cur_time += FSM.CLASSES.time

        if self.student.energy < 45:
            self.eat()

        if random.random() <= 0.7:
            self.doing_homework()
        else:
            self.attending_classes()

    def doing_homework(self):
        rand = random.random()
        self.student.deadlines += FSM.HOMEWORK.deadline_influence
        self.student.done += 1
        print(f"{self.cur_time}:00: Start do homework...")
        print(f"       {self.student.done} task is done")
        self.student.energy += FSM.HOMEWORK.resource_influence

        self.cur_time += FSM.HOMEWORK.time

        if rand <= 0.2 and (self.cur_time > 13) and (self.cur_time < 16) :
            self.walk_with_Stepan()

        if self.student.energy < 45:
            self.eat()
        elif self.cur_time >= 22:
            self.sleep()
        elif (self.student.done < 3) or (self.student.deadlines > 3):
            self.doing_homework()

        if rand <= 0.33:
            self.doing_yoga()
        elif rand <= 0.66:
            self.meet_friends()
        else:
            self.relax()
    
    def walk_with_Stepan(self):
        print(f"{self.cur_time}:00: Sun is shining. Stepan calls for a walk")
        if self.student.deadlines <=3:
            self.cur_time += 1
            print('       Walking...')
        else:
            print('      But I need to do homework')
        self.doing_homework()

    def _extracted_from_relax_2(self, arg0):
        print(f"{self.cur_time}{arg0}")
        self.cur_time += FSM.LEISURE.time
        self.student.energy += FSM.LEISURE.resource_influence
        self.student.mental = 'good'
        self.sleep()

    def meet_friends(self):
        self._extracted_from_relax_2(':00: Meet friends')


    def doing_yoga(self):
        self._extracted_from_relax_2(':00: Doing yoga')

    def relax(self):
        self._extracted_from_relax_2(':00: Relaxing')
    
    def sleep(self):
        if self.cur_time > 24:
            self.cur_time = self.cur_time%24
        print(f"{self.cur_time}:00: I'm going to bed. Good night.")
        if self.student.mental == 'bad':
            print("It was a hard day.. I'm tired 😞")
        else:
            print("It was a nice day 🥰")
        exit()



class Student:
    def __init__(self, energy = 70, deadlines=3) -> None:
        '''
        enegry: 0-100%
        deadlines: number of deadlines (integer)
        '''
        self.energy = energy
        self.deadlines = deadlines
        self.done = 0
        self.mental = 'bad'

if __name__ == '__main__':
    fsm = FSM(Student(70, 4))
    fsm.run()