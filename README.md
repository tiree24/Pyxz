# Pyxz

**After cloning:**

- pipenv install django
- pip install django-taggit
- python -m pipenv install Pillow

**UX and WebApp Preview:**


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
