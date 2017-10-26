import React, { Component } from 'react';
import {Route, Switch} from 'react-router-dom';

import './App.css';

import Header from './Header';
import NavBar from './NavBar';
import Footer from './components/footer/footer'

import Home from './Home';
import Crate from './Crate';
import Body from './Body';
import Paint from './Paint';
import Player from './Player';
import About from './About';
import InstancePage from './InstancePage';
import NotFound from './NotFound';

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
      <Route path='/body/:bodyname' component={InstancePage}/>
      <Route path='/paint/:paintname' component={InstancePage}/>
      <Route path='/player/:playername' component={InstancePage}/>
      <Route component={NotFound}/>
    </Switch>
  </div>

)

export default App;
