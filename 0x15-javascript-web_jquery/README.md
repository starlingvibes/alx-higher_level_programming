0x15. JavaScript - Web jQuery
=============================

![Logo](https://www.howtogeek.com/wp-content/uploads/2021/05/laptop-with-terminal-big.png?height=200p&trim=2,2,2,50)

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/qv-13Upi3L10qLhZdrkFag "explain to anyone"), **without the help of Google**:

### General

*   Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
*   How to select HTML elements in JavaScript
*   How to select HTML elements with JQuery
*   What are differences between `ID`, `class` and `tag name` selectors
*   How to modify an HTML element style
*   How to get and update an HTML element content
*   How to modify the DOM
*   How to make a `GET` request with JQuery Ajax
*   How to make a `POST` request with JQuery Ajax
*   How to listen/bind to DOM events
*   How to listen/bind to user events

Resources
---------

**Read or watch**:

*   [What is JavaScript?](https://intranet.hbtn.io/rltoken/FBd59d6M-Bal5PiSJbhw9g "What is JavaScript?")
*   [Selector](https://intranet.hbtn.io/rltoken/RtFB5Ycdvvk5OYv79zgr6A "Selector")
*   [Get and set content](https://intranet.hbtn.io/rltoken/JAC2vdSj1pbH6y_9OwQrAw "Get and set content")
*   [Manipulate CSS classes](https://intranet.hbtn.io/rltoken/Pvl_U4kdmxtHrZAHoFh_qw "Manipulate CSS classes")
*   [Manipulate DOM elements](https://intranet.hbtn.io/rltoken/fA1R3S7dNUX4lj68z6qMyw "Manipulate DOM elements")
*   [API](https://intranet.hbtn.io/rltoken/w_Y67Y3UlGQ6nluZx9KJyQ "API")
*   [Introduction](https://intranet.hbtn.io/rltoken/LOMQvsml-4ttg2Y2TVNbqQ "Introduction")
*   [GET & POST request](https://intranet.hbtn.io/rltoken/xN81Z76ZeNgB42tyJOgXjA "GET & POST request")
*   [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://intranet.hbtn.io/rltoken/Rq2Ob5rhN-N458YBxxaRXQ "JQuery Ajax Tutorial #1 - Using AJAX & API's")
*   [What went wrong? Troubleshooting JavaScript](https://intranet.hbtn.io/rltoken/ZpjZXl5AxHmurQFuxQfB4A "What went wrong? Troubleshooting JavaScript")
*   [JQuery](https://intranet.hbtn.io/rltoken/L5nA7F44DBhrCAdlEvxrqQ "JQuery")
*   [JQuery API](https://intranet.hbtn.io/rltoken/U3XGm3WaMxON5c-NkBFS6Q "JQuery API")
*   [JQuery Ajax](https://intranet.hbtn.io/rltoken/pZmSwUxd65dxIrX7D4n1pg "JQuery Ajax")

More Info
Import JQuery
```
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

Dependences
-----------

### 0\. No JQuery

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

*   You must use `document.querySelector` to select the HTML tag
*   You can’t use the JQuery API

Please test with this HTML file in your browser:

    
    guillaume@ubuntu:~/0x15$ cat 0-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="0-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$ 
    
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [0-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/0-script.js)

### 1\. With JQuery

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

    
    guillaume@ubuntu:~/0x15$ cat 1-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="1-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [1-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/1-script.js)

### 2\. Click and turn red

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

   
    guillaume@ubuntu:~/0x15$ cat 2-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <div id="red_header">Red header</div>
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="2-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$ 
   
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [2-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/2-script.js)

### 3\. Add \`.red\` class

Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`

*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

    
    guillaume@ubuntu:~/0x15$ cat 3-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
        <style>
          .red {
            color: #FF0000;
          }
        </style>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <div id="red_header">Red header</div>
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="3-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$
     
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [3-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/3-script.js)

### 4\. Toggle classes

Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`:

*   The `<header>` element must always have one class: `red` or `green`, never both in the same time and never empty.
*   If the current class is `red`, when the user click on `DIV#toggle_header`, the class must be updated to `green` ; and the reverse.
*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

    
    guillaume@ubuntu:~/0x15$ cat 4-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
        <style>
          .red {
            color: #FF0000;
          }
          .green {
            color: #00FF00;
          }
        </style>
      </head>
      <body>
        <header class="green"> 
          First HTML page
        </header>
        <div id="toggle_header">Toggle header</div>
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="4-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$
     
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [4-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/4-script.js)

### 5\. List of elements

Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:

*   The new element must be: `<li>Item</li>`
*   The new element must be added to `UL.my_list`
*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

    
    guillaume@ubuntu:~/0x15$ cat 5-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <br />
        <div id="add_item">Add item</div>
        <br />
        <ul class="my_list">
          <li>Item</li>
        </ul>
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="5-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$
    
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [5-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/5-script.js)

### 6\. Change the text

Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`

*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

   
    guillaume@ubuntu:~/0x15$ cat 6-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <br />
        <div id="update_header">Update the header</div>
        <br />
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="6-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$
    
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [6-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/6-script.js)

### 7\. Star wars character

Write a JavaScript script that fetches the character `name` from this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`

*   The name must be displayed in the HTML tag `DIV#character`
*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

    
    guillaume@ubuntu:~/0x15$ cat 7-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      </head>
      <body>
        <header> 
          Star Wars character
        </header>
        <br />
        <div id="character"></div>
        <br />
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="7-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$
    
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [7-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/7-script.js)

### 8\. Star Wars movies

Write a JavaScript script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`

*   All movie titles must be list in the HTML tag `UL#list_movies`
*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API

Please test with this HTML file in your browser:

    guillaume@ubuntu:~/0x15$ cat 8-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      </head>
      <body>
        <header> 
          Star Wars movies
        </header>
        <br />
        <ul id="list_movies">
        </ul>
        <br />
        <footer>
          Holberton School - 2017
        </footer>
        <script type="text/javascript" src="8-script.js"></script>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$ 
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [8-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/8-script.js)

### 9\. Say Hello!

Write a JavaScript script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`.

*   The translation of “hello” must be displayed in the HTML tag `DIV#hello`
*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API
*   Your script must work when it is imported from the `<head>` tag

Please test with this HTML file in your browser:

   
    guillaume@ubuntu:~/0x15$ cat 9-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
        <script type="text/javascript" src="9-script.js"></script>
      </head>
      <body>
        <header> 
          Say Hello!
        </header>
        <br />
        <div id="hello"></div>
        <br />
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$
    
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [9-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/9-script.js)

### 10\. No jQuery - document loaded

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

*   You must use `document.querySelector` to select the HTML tag
*   You can’t use the jQuery API
*   Note: Your script must be imported from the `<head>` tag, not at the end of the HTML

Please test with this HTML file in your browser:

    
    guillaume@ubuntu:~/0x15$ cat 100-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script type="text/javascript" src="100-script.js"></script>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$
    

    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [100-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/100-script.js)

### 11\. List, add, remove

Write a JavaScript script that adds, removes and clears `LI` elements from a list when the user clicks:

*   The new element must be: `<li>Item</li>`
*   The new element must be added to `UL.my_list`
*   When the user clicks on `DIV#add_item`: a new element is added to the list
*   When the user clicks on `DIV#remove_item`: the last element is removed from the list
*   When the user clicks on `DIV#clear_list`: all elements of the list are removed
*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API
*   You script must work when it imported from the `HEAD` tag

Please test with this HTML file in your browser:

    
    guillaume@ubuntu:~/0x15$ cat 101-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
        <script type="text/javascript" src="101-script.js"></script>
      </head>
      <body>
        <header> 
          First HTML page
        </header>
        <br />
        <div id="add_item">Add item</div>
        <div id="remove_item">Remove item</div>
        <div id="clear_list">Clear list</div>
        <br />
        <ul class="my_list">
          <li>Item</li>
        </ul>
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$ 
    
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [101-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/101-script.js)

### 12\. Say hello to everybody!

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

*   You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
*   The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
*   The translation must be fetched when the user clicks on `INPUT#btn_translate`
*   The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API
*   You script must work when imported from the `<head>` tag

Please test with this HTML file in your browser:

    
    guillaume@ubuntu:~/0x15$ cat 102-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
        <script type="text/javascript" src="102-script.js"></script>
      </head>
      <body>
        <header> 
          Say Hello
        </header>
        <br />
        <input id="language_code" type="text" placeholder="Language code"/>
        <input id="btn_translate" type="button" value="Translate"/>
        <br />
        <div id="hello"></div>
        <br />
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$
    
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [102-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/102-script.js)

### 13\. And press ENTER

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

*   You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
*   The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
*   The translation must be fetched when the user clicks on `INPUT#btn_translate` OR presses `ENTER` when the focus is on `INPUT#language_code`
*   The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
*   You can’t use `document.querySelector` to select the HTML tag
*   You must use the JQuery API
*   You script must work when imported from the `<head>` tag

Please test with this HTML file in your browser:

    
    guillaume@ubuntu:~/0x15$ cat 103-main.html 
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>Holberton School</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
        <script type="text/javascript" src="103-script.js"></script>
      </head>
      <body>
        <header> 
          Say Hello
        </header>
        <br />
        <input id="language_code" type="text" placeholder="Language code"/>
        <input id="btn_translate" type="button" value="Translate"/>
        <br />
        <div id="hello"></div>
        <br />
        <footer>
          Holberton School - 2017
        </footer>
      </body>
    </html>
    guillaume@ubuntu:~/0x15$
     
    

**Repo:**

*   GitHub repository: `holbertonschool-higher_level_programming`
*   Directory: `0x15-javascript-web_jquery`
*   File: [103-script.js](https://github.com/Imanolasolo/holbertonschool-higher_level_programming/blob/master/0x15-javascript-web_jquery/103-script.js)

## Installing, compiling and using
	
> Only install cloning this repository on your local device:  https://github.com/Imanolasolo/holbertonschool-higher_level_programming.git
	
> make executable the programs with `chmod +x` followed with .js file and name of executable file.
	
> Run the executable `main` files with `./` followed with the `.js` file

## Credits

## Author(s):blue_book:

Work is owned and maintained by:

* Imanol Asolo <[3848](mailto:3848@holbertonschool.com)> [![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Imanolasolo) [![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)](https://twitter.com/jjusturi) [![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)](https://www.linkedin.com/in/imanol-asolo-5ba9b42a/)


## Acknowledgments :mega: 

### **`Holberton School`** (*providing guidance*)
This program was written as part of the curriculum for Holberton School.
Holberton School is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information, visit [this link](https://www.holbertonschool.com/).
<p align="center">
	<img src="https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg" alt="This is a secret;)">
</p>