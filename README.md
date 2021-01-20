# Pyxz

After cloning:

- pipenv install django
- pip install django-taggit
- python -m pipenv install Pillow


**Unique Functions**

- maths(current_time, post_time)
  - Helper function that allows story's to 'delete' after 24 hours
  
- randomizer(random_list, choices, length)
  - Helper function which enables you to select how many random unique items from a QuerySet you would like in a empty list which can be displayed on any view.
  
  
```python
def maths(current_time, post_time):
    numofdays = current_time - post_time
    return numofdays.days


def randomizer(random_list, choices, length):
    while len(random_list) < min(len(choices), length):
        choice = random.choice(choices)
        if choice not in random_list:
            random_list.append(choice)
```
