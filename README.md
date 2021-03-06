# Pyxz

Outdated-NonPersistent database hosting example:
https://new-pyxz.herokuapp.com/

**TEAM:**
| Members | Description |
| --- | --- |
| Timothy Reynoso | Jack of all Trades :hammer_and_pick: [Portfolio](https://timothywebportfolio.web.app/). |
| Marcus Chiriboga | marcuschiriboga@gmail.com |
| Tracy DeWitt | justdewitt8485@gmail.com |
| Tiree Jackson | tiree_jackson@yahoo.com |


**After cloning:**

```cli
- pipenv install django
- pip install django-taggit
- python -m pipenv install Pillow
```
**Our Quick Mockup:**
- The Vision:
![alt text](https://github.com/tiree24/Pyxz/blob/main/ReadmeImages/mockup.png?raw=true)

**UX and WebApp Preview:**
- Homepage:
![alt text](https://github.com/tiree24/Pyxz/blob/main/ReadmeImages/homescreen.png?raw=true)
- Profile:
![alt text](https://github.com/tiree24/Pyxz/blob/main/ReadmeImages/profile.png?raw=true)
- Sub-Pyxz! (like Sub-Reddits):
![alt text](https://github.com/tiree24/Pyxz/blob/main/ReadmeImages/subpyxz.png?raw=true)
- Image Details + Comments:
![alt text](https://github.com/tiree24/Pyxz/blob/main/ReadmeImages/storydetail.png?raw=true)
- StoryUpload:
![alt text](https://github.com/tiree24/Pyxz/blob/main/ReadmeImages/uploadstory.png?raw=true)
- Login:
![alt text](https://github.com/tiree24/Pyxz/blob/main/ReadmeImages/login.png?raw=true)
- All Users:
![alt text](https://github.com/tiree24/Pyxz/blob/main/ReadmeImages/users.png?raw=true)
- Search:
![alt text](https://github.com/tiree24/Pyxz/blob/main/ReadmeImages/searchresults.png?raw=true)


**Unique Functions:**

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

**Preview of HomePage() Class based View Construction:** 

```python
class HomePage(View):

    html = 'homepage.html'
    form = CommentForm()

    def get(self, request):
        comments = Comment.objects.all()
        """ add this to views with all pictures except for stories """
        img_set = Image.objects.filter(is_story=False).all()
        # stories = Image.objects.filter(is_story=True).all()
        current_time = datetime.datetime.now(pytz.utc)
        stories = [img for img in Image.objects.filter(is_story=True).all() if maths(current_time, img.post_time) <= 1]
        tags = Image.tags.all()
        random_tags = []
        randomizer(random_tags, tags, 10)
        five_random = []
        randomizer(five_random, stories, 5)
        context = {'img_set': img_set, 'comments': comments, 'form': self.form, 'stories': five_random, 'taglist': random_tags}
        return render(request, self.html, context)

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            img = Image.objects.get(photo=request.POST.get("title", ""))
            model = Comment.objects.create(author=request.user, photo_linked=img, text=data['comment'])
            model.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
```
