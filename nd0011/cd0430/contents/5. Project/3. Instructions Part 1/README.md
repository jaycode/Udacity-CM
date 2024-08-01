## Project Instructions

This <a href="https://github.com/MidoUdacity/evaluate-news-nlp" target="_blank">Github repository</a> is your starter code for the project. 

### If you are working on your local computer
Clone the `main` branch or download the ZIP file, although feel free to start from scratch! It is the same as the starter code we began with in Lesson 2. Install and configure Webpack just as we did in the course. Feel free to refer to the course repo as you build this one, and remember to make frequent commits and to create and merge branches as necessary!

### If you are working on the Workspace

The files are already available on your Udacity Workspace. Duplicate/rename the `starter_project` directory, navigate to it using `cd [new directory name]`, and then simply run `npm install` to install all the required packages. The information on this page can be used as a reference for when you need to set up a similar project on your own in the future. 

---

The goal of this project is to give you practice with:

* Setting up Webpack
* Sass styles
* Webpack Loaders and Plugins
* Creating layouts and page design
* Service workers
* Using APIs and creating requests to external URLs

We have divided the instructions into the following stages, as  explained below:

### Stage 1 - Getting Started - Setting up the Project

It would be good to first get your basic project up and functioning. Fork the project Github repo, and then clone or download the zip file locally.

Remember that once you clone, you will still need to install everything:

```
cd <project directory>
npm install
```

Follow the steps from the course up to Lesson 4, but ***do not add Service Workers just yet***. We won't need the service workers during *development*, and having extra caches floating around just means there's more potential for confusion.

For reference, here is a brief summary of the steps that you need to follow from the course up to Lesson 4.

**Step 1.** After `npm install`, verify if both `webpack.dev.js` and `webpack.prod.js` files have: 

```js
const path = require("path") 
const webpack = require("webpack") 
module.exports = { }
```

Your Webpack installation must be completed by now.

**Step 2.** Verify, if both the Webpack config files have an entry point.

**Note:** There should be an index.js file in the client folder, if it’s not there you need to create it and add an alert: `alert("I EXIST")`.

**Step 3.** Now, that the Webpack entry is decided, you need to have babel installed:

```bash
npm i -D @babel/core @babel/preset-env babel-loader
```

**Step 4.** Create a .babelrc file and fill it with the following configuration: 

```json
{
    "presets": ["@babel/preset-env"]
}
```

**Step 5.** Both Webpack config files should have the test for babel-loader.

Remove quotes from `/.js` if they are present here e.g. `test: /\.js$/` instead of `test: '/\.js$/'`.

**Step 6.** In the client/index.js file make an import for `handleSubmit`, if it is not present. Don't forget to export this module.

**Step 7.** Now let us move to plugins. Install the HTML plugin `npm i -D html-webpack-plugin`.

**Step 8.** We need to add the `require` at the top of your Webpack config files

```js
const HtmlWebPackPlugin = require('html-webpack-plugin');
```

**Step 9.** Add a plugins list to the Webpack config and instantiate the plugin

```js
plugins: [
    new HtmlWebPackPlugin({
        template: "./src/client/views/index.html",
        filename: "./index.html",
    })
]
```

**Step 10.** Verify if the `mode` is present in both dev and prod Webpack configs.

**Step 11.** Let’s install the clean webpack plugin: `npm i -D clean-webpack-plugin` and add this new plugin to the plugin array as discussed earlier in plugins lessons.

**Step 12.** Rename all the `.css` files in client/styles to `.scss`.

**Step 13.** Install the sass loaders `npm i -D style-loader node-sass css-loader sass-loader`.

**Step 14.** Add the test case to the rule in webpack.dev.js and prod:

```js
{
    test: /.scss$/,
    use: [ 'style-loader', 'css-loader', 'sass-loader' ]
}
```

**Step 15.** Now, we can import the scss files like this in client/index.js:

```js
import './styles/resets.scss'
import './styles/base.scss'
import './styles/footer.scss'
import './styles/form.scss'
import './styles/header.scss'
```

Note that, with `sass` enabled, you also don't need to include the `<link rel="stylesheet" />` tags directly in your HTML documents. The stylesheets are applied automatically by the loader packages.

---

Just for your quick reference, we installed the following loaders and plugins so far:

```bash
## Choose the necessary installation for your development mode
npm i -D @babel/core @babel/preset-env babel-loader
npm i -D html-webpack-plugin
npm i -D clean-webpack-plugin
npm i -D style-loader node-sass css-loader sass-loader
```

If you'd like to, you may also use the following plugins to optimize your CSS and Javascript files to improve page loading speed (learn more on their respective documentations pages[mini-css-extract-plugin](https://www.npmjs.com/package/mini-css-extract-plugin), [optimize-css-assets-webpack-plugin](https://www.npmjs.com/package/optimize-css-assets-webpack-plugin), [terser-webpack-plugin](https://webpack.js.org/plugins/terser-webpack-plugin/)):

```bash
npm i -D mini-css-extract-plugin
npm i -D optimize-css-assets-webpack-plugin terser-webpack-plugin
```

*Note: If you are facing package compatibility issues, here is a proposed set of packages with their versions. These versions are compatible with each other.*

```json
"dependencies": {
    "cors": "^2.8.5",
    "css-loader": "^6.10.0",
    "dotenv": "^16.4.5",
    "express": "^4.17.1",
    "html-webpack-plugin": "^5.6.0",
    "node-fetch": "^3.3.2",
    "style-loader": "^3.3.4",
    "webpack-cli": "^5.1.4"
},
"devDependencies": {
    "@babel/core": "^7.5.4",
    "@babel/preset-env": "^7.5.4",
    "babel-loader": "^8.0.6",
    "jest": "^29.7.0",
    "sass": "^1.72.0",
    "sass-loader": "^14.1.1",
    "webpack": "^5.90.3",
    "webpack-dev-server": "^5.0.2",
    "workbox-webpack-plugin": "^7.0.0"
}
```

*As these versions are not the latest versions, make sure to install them with:*

```bash
npm i --legacy-peer-deps
```

## Build & Run the App

Both of these commands are available in the `package.json` file, but to clarify:

1. To run the client app, use the command `npm run build-dev` or `npm run build-prod` and then click on **Links** > **View the Web Page** to view it.
2. To run the server app, use the command `npm run start` and then click on **Links** > **Server API Page** to view it. **If you're working on the workspace**, the URL of the server API needs to be copied over to the `src/client/js/formHandler.js` file so the client app may communicate with the server API.

When everything works properly, you should see the following when viewing the server API page:

[The sample server API page](sample-server.png)

and the following when viewing the web page (i.e. the client app):

[The sample client app page](sample-client.png)

We also prepared a sample verification routine there. Try entering captain names like `Picard` or `Kirk` or random inputs. The the verification function is available in file `client/js/nameChecker.js`. Replace this file and function with a system to verify the correctness of the URL.
