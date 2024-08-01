// Replace this with the URL of the "Server API Page" underneath this workspace.
const serverURL = 'https://6nfa64yzva.prod.udacity-student-workspaces.com'

/* Function to POST data */
const postData = async (url = '', data = {}) => {
    console.log(data);
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.

      // The credentials options are "include", "same-origin", and "omit"
      // When the client and server locations are the same 
      // (e.g. in your personal computer), use "same-origin".
      // In this case, Udacity workspace creates different addresses
      // for client and server, hence "include" is the appropriate value.
      credentials: 'include',
      
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data), // body data type must match "Content-Type" header        
    });
  
    try {
      const newData = await response.json();
      // console.log(newData);
      return newData;
    } catch (error) {
      console.log("error", error);
      return;
      // appropriately handle the error
    }
  }
  
  // postData('/addMovie', { movie: 'the matrix', score: 5 });
  
  /* Function to GET data */
  const getData = async (url = '') => {
    try {
      const response = await fetch(url, {
        method: 'GET', // Only the GET method is used here
        credentials: 'include', // *include, same-origin, omit
        headers: {
          'Content-Type': 'application/json',
        },
      });
  
      const newData = await response.json(); // Parse JSON response into JavaScript object
      console.log(newData); // Log the received data
      return newData;
    } catch (error) {
      console.log("error", error); // Log any errors
      return; // Return undefined on error
    }
  }
  
  // Things to do on DOM load:
  document.addEventListener('DOMContentLoaded', function () {
      /* Handle the form submission */
      function submitMovie() {
        const title = document.getElementById('movieTitle').value;
        const score = document.getElementById('score').value;
  
        const url = `${serverURL}/addMovie`;
        postData(url, { movie: title, score: score });
      }
      /* Attach submitMovie to a button event listener */
      document.getElementById('movie-form').querySelector('button').addEventListener('click', submitMovie);
  
      /* Get movies from the API and display them */
      async function loadMovies() {
        const url = `${serverURL}/movies`;
        const movies = await getData(url);
        const list = document.getElementById('movie-list');
        list.innerHTML = '';
        for (const movie of movies) {
          const entry = document.createElement('li');
          entry.textContent = `Movie: ${movie.movie}, Score: ${movie.score}`;
          list.appendChild(entry);
        }
  
      }
      document.getElementById('load-movies-button').addEventListener('click', loadMovies);
  
    });