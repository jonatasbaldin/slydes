# Slydes
Why not show your presentations with Python?

### Create a presentation
`$ cat presentation.py`

```python
from slydes import Presentation, Template


talk = Presentation()
template = Template()


@talk.add_slide
def first_slide():
    title = 'This is the title!'
    msg = '''
    Hello world!
    My name is PySlides!
    '''
    return template.default(title, msg)
    

@talk.add_slide
def second_slide():
    title = 'The second slide!'
    msg = '''
    * Bullet points!
    * why
    * not?
    '''
    return template.default(title, msg)


@talk.add_slide
def third_slide():
    title = 'The last slide!'
    msg = 'Bye world!'
    return template.default(title, msg)
```


### Run it!
`$ ipython`
```bash
from presentation import talk

talk.next()
--------------------------------------------------------------------------------
#                                                                              #
#                                                                              #
#      This is the title!                                                      #
#                                                                              #
#                                                                              #
#          Hello world!                                                        #
#          My name is PySlides!                                                #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
--------------------------------------------------------------------------------

talk.next()
--------------------------------------------------------------------------------
#                                                                              #
#                                                                              #
#      The second slide!                                                       #
#                                                                              #
#                                                                              #
#          * Bullet points!                                                    #
#          * why                                                               #
#          * not?                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
--------------------------------------------------------------------------------

talk.previous()
--------------------------------------------------------------------------------
#                                                                              #
#                                                                              #
#      This is the title!                                                      #
#                                                                              #
#                                                                              #
#          Hello world!                                                        #
#          My name is PySlides!                                                #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
--------------------------------------------------------------------------------

talk.current()
--------------------------------------------------------------------------------
#                                                                              #
#                                                                              #
#      This is the title!                                                      #
#                                                                              #
#                                                                              #
#          Hello world!                                                        #
#          My name is PySlides!                                                #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
--------------------------------------------------------------------------------
```

### Installing
```bash
$ pip install slydes
```

### Important (or not!)
The library is suuuuuuuper alpha, at the point that we could change everything!  
If you have any ideas, please drop an issue ❤️
