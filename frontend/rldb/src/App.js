import React, { Component } from 'react';
import {Route, Switch} from 'react-router-dom';

import './styles/App.css';

import Header from './components/Header';
import NavBar from './components/NavBar';

import Home from './components/Home';
import Crate from './components/Crate';
import Body from './components/Body';
import Paint from './components/Paint';
import Player from './components/Player';
import About from './components/About';
import InstancePage from './components/InstancePage';

//right now header is just navbar, but maybe header could be something more

const App = () => (
  <div>
    <NavBar />
    <Switch>
      <Route exact path='/' component={Home}/>
      <Route exact path='/crate' component={Crate}/>
      <Route exact path='/body' component={Body}/>
      <Route exact path='/paint' component={Paint}/>
      <Route exact path='/player' component={Player}/>
      <Route exact path='/about' component={About}/>
      <Route path='/crate/:cratename' component={InstancePage}/>
    </Switch>
  </div>

)

export default App;
