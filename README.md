[![N|Solid](https://raw.githubusercontent.com/y7usuf/Document-Analysis-API/master/app.jpg)](#)

# To Do

- Python version upgrade 2.7 -> 3.6
- New app logic
- Fast text scan algorithm



Important Message: If you want to use this app, you have to edit some code. 

### Technologies

DAA(Document Analysis App) uses a number of open source projects to work properly:

* [Flask] - A microframework based on Werkzeug, Jinja2 and good intentions http://flask.pocoo.org/
* [Flask RESTful] - Simple framework for creating REST APIs http://flask-restful.readthedocs.io/
* [Redis] - Redis is an in-memory database that persists on disk. http://redis.io/
* [Angular JS] - HTML enhanced for web apps http://angularjs.org/

### Installation

DAA requires [Python 2.7](https://www.python.org/download/releases/2.7/) to run.

**Step 1) Activate python environment**

```bash
$ source ./yourOwnEnvironmentDirectory/bin/activate
```

**Step 2) Install the project dependencies**

```bash
$ pip install -r requirements.txt
```

**Step 3) Run the project**

```bash
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

###Additional

langdetect library supports 55 languages out of the box ([ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)):

af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he, hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl, pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw

### Development

Want to contribute? Great!

Fork, commit, push

[Flask]: https://github.com/pallets/flask
[Flask RESTful]: http://flask-restful-cn.readthedocs.io/en/0.3.5/
[Redis]: https://github.com/antirez/redis
[Angular JS]: https://github.com/angular/angular.js/tree/master