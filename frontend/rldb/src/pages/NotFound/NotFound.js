import React from 'react';
import {Link} from 'react-router-dom';

const NotFound = () => (
  <div>
    <div className="container">
        <h1>Page Not Found</h1>
        <h3>How did you get here?</h3>
        <h3>You should probably go <Link to="/"> back to the home page </Link>.</h3>
    </div>
  </div>
)

export default NotFound;
