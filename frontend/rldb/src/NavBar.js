import React, {Component} from 'react';

import { Navbar, Nav, NavItem} from 'react-bootstrap';
import {  LinkContainer, IndexLinkContainer } from 'react-router-bootstrap';

class NavBar extends Component {
  render() {
    return (
      <Navbar className="navbar title-font" inverse collapseOnSelect>
        <Navbar.Header>
          <div className='navbar-brand'>Header Text</div>
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav>
            <IndexLinkContainer to="/">
              <NavItem>Home</NavItem>
            </IndexLinkContainer>
            <IndexLinkContainer to="/About">
              <NavItem>About</NavItem>
            </IndexLinkContainer>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}

export default NavBar;