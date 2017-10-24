import React, {Component} from 'react';

import { Navbar, Nav, NavItem} from 'react-bootstrap';
import {  LinkContainer, IndexLinkContainer } from 'react-router-bootstrap';

class NavBar extends Component {
  render() {
    return (
      <Navbar className="navbar title-font" inverse collapseOnSelect>
        <Navbar.Header>
          <Navbar.Brand>
            RLDB
          </Navbar.Brand>
          <Navbar.Toggle/>
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav>
            <IndexLinkContainer to="/">
              <NavItem>Home</NavItem>
            </IndexLinkContainer>
            <IndexLinkContainer to="/crate">
              <NavItem>Crate</NavItem>
            </IndexLinkContainer>
            <IndexLinkContainer to="/body">
              <NavItem>Body</NavItem>
            </IndexLinkContainer>
            <IndexLinkContainer to="/paint">
              <NavItem>Paint Finish</NavItem>
            </IndexLinkContainer>
            <IndexLinkContainer to="/player">
              <NavItem>Player</NavItem>
            </IndexLinkContainer>
            <IndexLinkContainer to="/about">
              <NavItem>About</NavItem>
            </IndexLinkContainer>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}

export default NavBar;