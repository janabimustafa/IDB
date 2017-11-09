import React, {Component} from 'react';
import {withRouter} from 'react-router-dom';
import { Navbar, Nav, NavItem, NavDropdown, MenuItem, FormGroup, FormControl, Button} from 'react-bootstrap';
import {  LinkContainer, IndexLinkContainer } from 'react-router-bootstrap';
import './NavBar.css';

class NavBar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      searchTerm: ''
    }
    this.searchSubmit = this.searchSubmit.bind(this);
    this.searchChange = this.searchChange.bind(this);
  }
  searchChange(event){
    this.setState({searchTerm: event.target.value});
  }
  searchSubmit(event){
    event.preventDefault()
    var searchTermEncoded = encodeURI(this.state.searchTerm)    
    this.props.history.push(`/search/${searchTermEncoded}`)
  }
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
              <MenuItem href="/crates/">Crates</MenuItem>
              <MenuItem href="/bodies/">Bodies</MenuItem>
              <MenuItem href="/paints/">Paint Finish</MenuItem>
              <MenuItem href="/antennas/">Antennas</MenuItem>
              <MenuItem href="/banners/">Banners</MenuItem>
              <MenuItem href="/boosts/">Boosts</MenuItem>
              <MenuItem href="/decals/">Decals</MenuItem>
              <MenuItem href="/explosions/">Explosions</MenuItem>
              <MenuItem href="/toppers/">Toppers</MenuItem>
              <MenuItem href="/trails/">Trails</MenuItem>
              <MenuItem href="/wheels/">Wheels</MenuItem>
            </NavDropdown>
            <IndexLinkContainer to="/players/">
              <NavItem>Players</NavItem>
            </IndexLinkContainer>
            <IndexLinkContainer onClick={this.forceUpdate} to="/dlcs/">
              <NavItem>DLCs</NavItem>
            </IndexLinkContainer>
            <IndexLinkContainer to="/about">
              <NavItem>About</NavItem>
            </IndexLinkContainer>
          </Nav>
          <Nav pullRight>
            <Navbar.Form>
              <form onSubmit={this.searchSubmit}>
                <FormGroup>
                  <FormControl value={this.state.searchTerm} onChange={this.searchChange} type="text" placeholder="Search..." />
                </FormGroup>
                {' '}
                <Button type="submit">Submit</Button>
              </form>
            </Navbar.Form>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}

export default withRouter(NavBar);