import random


# perform a random number task
def do_task(task):
    print('Performing task: {}'.format(task))
    print('Random number: {}'.format(random.randint(1, 100)))


if __name__ == '__main__':
    do_task('Hello World')
