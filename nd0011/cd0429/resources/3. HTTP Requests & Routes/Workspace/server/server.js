/* Express to run server and routes */
const express = require('express');

/* Start up an instance of app */
const app = express();

/* Dependencies */
const bodyParser = require('body-parser')
/* Middleware*/
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
const cors = require('cors');
app.use(cors());

/* Initialize the main project folder*/
app.use(express.static('website'));

const port = 8000;
/* Spin up the server*/
const server = app.listen(port, listening);
function listening() {
  console.log('server running');
  console.log(`running on localhost: ${port}`);
};

// MOVIE EXAMPLE
const data = [];
app.post('/addMovie', addMovie);

function addMovie(req, res) {
  data.push(req.body);
  console.log(data);
};

// GET all movies
app.get('/movies', getMovies);

function getMovies(request, response) {
  response.send(data);
};