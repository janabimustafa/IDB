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
              <IndexLinkContainer to="/crates">
                <MenuItem>Crates</MenuItem>
              </IndexLinkContainer>
              <IndexLinkContainer to="/bodies">
                <MenuItem>Bodies</MenuItem>
              </IndexLinkContainer>
              <IndexLinkContainer to="/paints">
                <MenuItem>Paint Finish</MenuItem>
              </IndexLinkContainer>
              <IndexLinkContainer to="/antennas">
                <MenuItem>Antennas</MenuItem>
              </IndexLinkContainer>
              <IndexLinkContainer to="/banners">
                <MenuItem>Banners</MenuItem>
              </IndexLinkContainer>
              <IndexLinkContainer to="/boosts">
                <MenuItem>Boosts</MenuItem>
              </IndexLinkContainer>
              <IndexLinkContainer to="/decals">
                <MenuItem>Decals</MenuItem>
              </IndexLinkContainer>
              <IndexLinkContainer to="/explosions">
                <MenuItem>Explosions</MenuItem>
              </IndexLinkContainer>
              <IndexLinkContainer to="/toppers">
                <MenuItem>Toppers</MenuItem>
              </IndexLinkContainer>
              <IndexLinkContainer to="/trails">
                <MenuItem>Trails</MenuItem>
              </IndexLinkContainer>
              <IndexLinkContainer to="/wheels">
                <MenuItem>Wheels</MenuItem>
              </IndexLinkContainer>
            </NavDropdown>
            <IndexLinkContainer to="/players">
              <NavItem>Players</NavItem>
            </IndexLinkContainer>
            <IndexLinkContainer to="dlcs">
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