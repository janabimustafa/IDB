import React, {Component} from 'react';

import { Navbar, Nav, NavItem, NavDropdown, MenuItem, FormGroup, FormControl, Button} from 'react-bootstrap';
import {  LinkContainer, IndexLinkContainer } from 'react-router-bootstrap';

class NavBar extends Component {

  render() {
    return (
      <Navbar className="navbar title-font" inverse collapseOnSelect>
        <Navbar.Header>
          <IndexLinkContainer to="/" style={{ cursor: 'pointer' }}>
            <Navbar.Brand>
              RLDB
            </Navbar.Brand>
          </IndexLinkContainer>
          <Navbar.Toggle/>
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav>
            <NavDropdown title="Items" id="nav-dropdown">
              <MenuItem href="/crates">Crates</MenuItem>
              <MenuItem href="/bodies">Bodies</MenuItem>
              <MenuItem href="/paints">Paint Finish</MenuItem>
              <MenuItem href="/antennas">Antennas</MenuItem>
              <MenuItem href="/banners">Banners</MenuItem>
              <MenuItem href="/boosts">Boosts</MenuItem>
              <MenuItem href="/decals">Decals</MenuItem>
              <MenuItem href="/explosions">Explosions</MenuItem>
              <MenuItem href="/toppers">Toppers</MenuItem>
              <MenuItem href="/trails">Trails</MenuItem>
              <MenuItem href="/wheels">Wheels</MenuItem>
            </NavDropdown>
            <IndexLinkContainer to="/players">
              <NavItem>Players</NavItem>
            </IndexLinkContainer>
            <IndexLinkContainer to="/dlcs">
              <NavItem>DLCs</NavItem>
            </IndexLinkContainer>
            <IndexLinkContainer to="/about">
              <NavItem>About</NavItem>
            </IndexLinkContainer>
          </Nav>
          <Nav pullRight>
            <Navbar.Form>
              <FormGroup>
                <FormControl type="text" placeholder="This doesn't work" />
              </FormGroup>
              {' '}
              <LinkContainer to="/search">
                <Button type="submit">Submit</Button>
              </LinkContainer>
            </Navbar.Form>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}

export default NavBar;