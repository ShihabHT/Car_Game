class Car:
    def __init__(self, speed = 0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I am going ", self.speed, "kmph!")

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1
    def flymood(self):
        self.speed += 10
    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass

if __name__ == '__main__':
    my_car = Car()
    print("I am a car")

    while True:
        action = input("What should you do? Acceletate, Brake, Odometer, Speed, Fly Mood\n").upper()

        if action not in 'ABOS' or len(action) != 1:

            print("I don't know how to do that")
            continue

        elif action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has travelled ", my_car.odometer, "kilometers")
        elif action == 'S':
            print("The car's average speed is ", my_car.average_speed(), "kmph")

        elif action == 'F':
            print("Car is in flying mood .\n speed",my_car.flymood(),"kmph")
        my_car.step()
        my_car.say_state()


