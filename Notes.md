# A tale about how I've connected my Python app with React.

I wanted to keep the whole code of mine on the backend while adding react on the frontend.
I didn't want to initialize a new app (what seemed to be the easiest solution) but learn how to work
on the codebase I already have.

As the first step, I've moved all the code I've written so far into a `server` directory in order to make
the whole file structure more readable.

Before I start with explaining the process I've taken step by step I wanted to briefly talk about my other approaches to this problem that didn't work well.

### Approaches that didn't work for me

#### 1) Fully manual - didn't work well because of the need of translating the JS from ES5 to ES6 every time I make a change.
I've installed all the packages needed for react app (react, react-dom) using npm install. I've wrote some React code using ES5 syntax and quickly added it to my code.
I've followed this official React tutorial - Add React in One minute: https://reactjs.org/docs/add-react-to-a-website.html. It's possible to write React in without es6, again,
the official documentation explains how: https://reactjs.org/docs/react-without-es6.html.

The problem was that writing in non es6 produces a much uglier, longer and harder to read code.
Also, most of the materials online are in es6, so using this syntax would make easier to me to find some answers online.

So I've decided I'll write my code in es6 forgetting that the browsers don't understand it! I've got an `"Uncaught SyntaxError: Unexpected identifier"` error in my first es6 line - ``import React from `react``. The solution to this is Babel - a compiler that translates ES6 to oldschool JS (https://babeljs.io/). I've tried to add it manually and reached a point where babel was translating a file. The problem was that nothing was automated - I needed to translate the documents after each change what would make the development process much much longer. As the setup is very important and influences the future works a lot, I've decided to spend some time and try again, this time in an automated way

#### 2) Automated - did't work because of the magic connected to create-react-app plugin. TL;DR - I had no idea how my own program works.
There is an npm package called `create-react-app` and it's just magical - it does all of the stuff for you. You don't need to install and setup babel, you don't write a webpack, you don't have to run anything else than `npm start` to make your React written in ES6 appear on a server that this plugin writes for you as well. Here you can find a repo with my React app written using this package: https://github.com/Kotauror/giftgiver.

You know, I had this amazing idea of creating a react app using this magical tool inside of my python app and then remove everything that I don't need like the node server.
God, how proud I was of this tricky idea - It's going to solve all my problems I thought. Nope, it didn't. It's so magical and automated (ie. does everything for you), that I just couldn't adjust it to my app and the existing folder structure.

### How I made it work - Conscious automation.  
I've followed this blogpost - https://codeburst.io/creating-a-full-stack-web-application-with-python-npm-webpack-and-react-8925800503d9 and added my own improvements.

1. I've started with the following directories structure:

```plain
.
├── README.md
├── .gitignore
└── server/    -------> my old python code
└── static/
    └── js/
      ├── components/
    └── styles/
```
2. I've initialized npm to create package.json file (`npm init`)
3. I've installed webpack as a dev dependency (` npm i webpack --save-dev`). Webpack takes all your module dependencies and generates static assets that represent them.
In other words, it will take all my ES6 javascript files and bundle them into one file - bundle.js.
4. Using webpack requires a webpack.config file. The config tells webpack where to find the Javascript and React files, and where to put the generated Javascript bundle. I've placed it in the `static` directory which is basically the root for all my front-end stuff.

```plain
const webpack = require('webpack');
const config = {
    entry:  __dirname + '/js/index.js',       -----> Where it takes the js code that it's going to bundle
    output: {
        path: __dirname + '/dist',            -----> Where it will place the bundled .js file (the dist directory will be created automatically)
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.js', '.css']
    },
};
module.exports = config;
```
5. I've added a few run commands (scripts) to my package.json:
- Build is used for production builds, and dev-build for non-minified builds.
- Watch is similar to dev-build, with the added benefit that it monitors your project files. Any changed files will be automatically rebuilt, and refreshing your browser will show the change you just made. I use watch the whole time! I keep the npm watch command open in one terminal window what ensures me that the code will be refreshed automatically.

```json
"scripts": {
  "build": "webpack -p --progress --config webpack.config.js",
  "dev-build": "webpack --progress -d --config webpack.config.js",
  "test": "echo \"Error: no test specified\" && exit 1",
  "watch": "webpack --progress -d --config webpack.config.js --watch"
}
```
6. Adding babel support. Webpack itself just bundles all javascript into one file. But we don't only want to bundle it - we want to translate it wrom ES6 and then bundle it. . By installing the es2015 and react presets, Babel converts our Javascript and React jsx files into Javascript syntax compatible with all modern browsers.
To install babel type:
`$ npm i babel-core babel-loader babel-preset-es2015 babel-preset-react --save-dev`
Add the Babel presets to the package.json:
```plain
“babel”: {
  “presets”: [
    “es2015”,
    “react”
  ]
},
```
7. Add a babel-loader rule to the Webpack config. It will ensure that the files are not only bundled, but also translated.
```plain
module: {
  rules: [
    {
      test: /\.jsx?/,
      exclude: /node_modules/,
      use: 'babel-loader'
    }
  ]
}
```
8. In the static folder create the following index.html file:
```html
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <div id="content" />
    <script src="dist/bundle.js" type="text/javascript"></script>   // <----- it links the bundled .js file the webpack created!
  </body>
</html>
```
9. In the static/js folder, create an index.js file with the following line:
```javascript
alert(“Hello World!”);
```
10. Start the Webpack watch command we just created in a separate terminal tab. This means it can run in the background whilst we continue working. It should build your bundle without errors.

```plain
$ npm run watch
```
Open the index.html file in your browser of choice. It should show an alert saying “Hello World!”.

11. Install react

```plain
$ npm i react react-dom --save-dev
```
12. Next we replace the alert in the index.js with a simple React app, and have it load a React class we have created in a separate App.js file that will be placed in components directory.

```javascript
// index.jsx
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
ReactDOM.render(<App />, document.getElementById("content"));
```

13. Create App component in components directory in the js folder:

```Javascript
// App.jsx
import React from “react”;
export default class App extends React.Component {
  render () {
    return <p> Hello React!</p>;
  }
}
```

14. Add a route to the server to show this website. In my app.py file I've added a new route:

```python
@app.route('/', methods=['GET'])
def testRoute():
    return render_template("index.html")
```
On the `/` path, I want my server to render the index.html created above, the one that links the bundle.js file. The problem was that my server was looking for static (html) files in the server directory, not in the static one. In order to fix it, I needed to tell my app where to find the html files. In order to do it, I've added the collowing code to my create_app.py file: ```static_folder="../static/dist", template_folder="../static")```. The whole file looks like this:

```Python
from flask import Flask
import config

def create_app(app_config):
    app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
    app.config.from_object(app_config)
    return app
```

15. Adding tests. I've added the following packages to my package.json:
```json
"enzyme": "^3.6.0",
"enzyme-adapter-react-16": "^1.5.0",
"jest-cli": "^20.0.4"
```

In the components folder I've created a `__tests__` directory where I've placed my App.test.js file with a simple snapshot test:

```javascript
import React from 'react';
import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

Enzyme.configure({adapter: new Adapter()});

import App from '../App';


describe('App', () => {
  const app = shallow(<App />);

  it('renders correctly', () => {
    expect(app).toMatchSnapshot();
  });
});
```
I run the `jest` command to run the test from anywhere in the `static` directory. 
