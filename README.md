# Slydes
Why not show your presentations with Python?

[![codecov](https://codecov.io/gh/jonatasbaldin/slydes/branch/master/graph/badge.svg)](https://codecov.io/gh/jonatasbaldin/slydes)
[![CircleCI](https://circleci.com/gh/jonatasbaldin/slydes/tree/master.svg?style=svg)](https://circleci.com/gh/jonatasbaldin/slydes/tree/master)

### Installing
```bash
$ pip install slydes
```

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
```

### Run it
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
```

### Presentation Mode
Now you can navigate the presentation using the arrow keys! To exit, just type `CTRL+C`.
```python
talk.present()
```

### Complete API
```python
# Move to next slide
talk.next()
# or
talk()

# Move to previous slide
talk.previous()

# Shows current slide
talk.current()
```

### Important (or not!)
The library is suuuuuuuper alpha, at the point that we could change everything!  
If you have any ideas, please drop an issue ❤️
