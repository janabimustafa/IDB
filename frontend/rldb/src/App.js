import React, { Component } from 'react';
import {Route, Switch} from 'react-router-dom';

import './App.css';

import NavBar from './NavBar';

import Home from './Home';
import Item from './Item';
import Player from './Player';
import About from './About';
import Search from './Search';
import InstancePage from './InstancePage';
import PaintPage from './PaintPage';
import PlayerPage from './PlayerPage';

import NotFound from './NotFound';

//right now header is just navbar, but maybe header could be something more

const App = () => (
  <div>
    <NavBar />
    <Switch>
      <Route exact path='/' component={Home}/>
      <Route exact path='/crates' component={Item}/>
      <Route exact path='/bodies' component={Item}/>
      <Route exact path='/paints' component={Item}/>
      <Route exact path='/antennas' component={Item}/>
      <Route exact path='/banners' component={Item}/>
      <Route exact path='/decals' component={Item}/>
      <Route exact path='/explosions' component={Item}/>
      <Route exact path='/toppers' component={Item}/>
      <Route exact path='/trails' component={Item}/>
      <Route exact path='/boosts' component={Item}/>
      <Route exact path='/wheels' component={Item}/>

      <Route exact path='/dlcs' component={Item}/>
      

      <Route exact path='/players' component={Player}/>
      <Route exact path='/about' component={About}/>
      
      <Route path='/search/:searchterm' component={Search}/>
      <Route path='/crates/:cratename' component={InstancePage}/>
      <Route path='/bodies/:bodyname' component={InstancePage}/>
      <Route path='/paints/:paintname' component={InstancePage}/>
      <Route path='/antennas/:antennaname' component={InstancePage}/>
      <Route path='/banners/:bannername' component={InstancePage}/>
      <Route path='/decals/:decalname' component={InstancePage}/>
      <Route path='/explosions/:explosionname' component={InstancePage}/>
      <Route path='/decals/:decalname' component={InstancePage}/>
      <Route path='/toppers/:toppername' component={InstancePage}/>
      <Route path='/trails/:trailname' component={InstancePage}/>
      <Route path='/boosts/:boostname' component={InstancePage}/>
      <Route path='/wheels/:wheelname' component={InstancePage}/>

      <Route path='/dlcs/:dlcname' component={InstancePage}/>

      <Route path='/players/:playername' component={PlayerPage}/>
      <Route component={NotFound}/>
    </Switch>
  </div>

)

export default App;
