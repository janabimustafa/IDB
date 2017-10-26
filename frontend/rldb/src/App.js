import React, { Component } from 'react';
import {Route, Switch} from 'react-router-dom';

import './App.css';

import Header from './Header';
import NavBar from './NavBar';

import Home from './Home';
import Crate from './Crate';
import Body from './Body';
import Paint from './Paint';
import Player from './Player';
import About from './About';

//right now header is just navbar, but maybe header could be something more

const App = () => (
  <div>
    <NavBar />
    <Switch>
      <Route exact path='/' component={Home}/>
      <Route path='/crate' component={Crate}/>
      <Route path='/body' component={Body}/>
      <Route path='/paint' component={Paint}/>
      <Route path='/player' component={Player}/>
      <Route path='/about' component={About}/>
    </Switch>
  </div>

)

export default App;
