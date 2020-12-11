import random
import tkinter
import time

roll_no = []
total_students = int(input('enter total number of students'))
for i in range(1, total_students + 1):
    roll_no.append(i)
done = []


def generate_roll_no():
    global roll_no
    global done
    global total_students
    if len(roll_no) > 0:
        r = random.choice(roll_no)
        gen.set('next roll number is {0}'.format(str(r)))
        roll_no.remove(r)
        done.append(r)
        t = total_students - len(done)
        rem.set('remaining students are {0}'.format(str(t)))


if __name__ == '__main__':
    random_roll = tkinter.Tk()
    random_roll.geometry('640x480')
    random_roll.title('roll number generator')
    # random_roll.config(background='yellow')

    rem = tkinter.StringVar()
    rem.set(total_students)

    studentLabel = tkinter.Label(random_roll, textvariable=rem, fg='green')
    studentLabel.pack(side='top', anchor='n')
    studentLabel.config(font=('Courier', 25))

    gen = tkinter.StringVar()
    gen.set('-')

    number = tkinter.Label(random_roll, textvariable=gen, fg='blue')
    number.pack(side='top', anchor='s')
    number.config(font=('Courier', 30))

    generator_button = tkinter.Button(random_roll, text='generate number', command=generate_roll_no)
    generator_button.pack(side='top', anchor='s')

    lab = tkinter.Label(random_roll, text='-', height=10, fg='red')
    lab.pack(side='bottom', anchor='n')
    lab.config(font=('Courier', 26))

    x = random.randint(1, total_students)
    while len(done) != total_students:
        lab.config(text=str(x))
        random_roll.update()
        x = random.randint(1, total_students)
        time.sleep(0.2)
    random_roll.mainloop()
