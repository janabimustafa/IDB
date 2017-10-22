import React, { Component } from 'react';
import {Route, Switch} from 'react-router-dom';

import './App.css';

import Header from './Header';
import Home from './Home';
import About from './About';

const App = () => (
  <div>
    <Header />
    <Switch>
      <Route exact path='/' component={Home}/>
      <Route path='/About' component={About}/>
    </Switch>
  </div>

)

export default App;
