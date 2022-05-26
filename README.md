# Contact Application 
<p>This application aims to display randomly generated contacts from the radomuser.me api.</p>
<p>After getting the data from this api, we use sqlachemy to enter these values in a Contact table in a postgres database</p>
<p>We use flask to retrieve the data from the database and display it with a GET request in a json.</p>
<p>Finally we display the data with React and Javascript in an html window</p>

# deployment of the application
<p>First we need to launch the flask api to be able to retrieve the data</p>
<p>For this we need to run the <code>main.py</code> file</p>
<p>After that we go in our terminal to the <code>my-app</code> folder and launch the react application</p>
<pre><code>cd my-app </code>
<code>npm start</code></pre>
