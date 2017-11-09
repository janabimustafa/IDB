import React, {Component} from 'react';

import {Pagination, DropdownButton, MenuItem} from 'react-bootstrap';
import PlayerCard from './PlayerCard';
import LoadingOverlay from './LoadingOverlay';
import Select from 'react-select';
import 'react-select/dist/react-select.css';

const numberPerPage = 10;

class Player extends Component {
    constructor(props) {
        super(props);

        this.state = {
            type: "",
            data: null,
            filter : [],
            platformFiltersValues : [], //currently applied filters
            platformFilter : [], //currently applied filters
            view: [],
            pageNumber: 1
        };

        this.changePage = this.changePage.bind(this);
        this.handlePlatformFilterChange = this.handlePlatformFilterChange.bind(this);
        this.handleSort = this.handleSort.bind(this);
    }

    //is it better to do fetch in constructor or in componentDidMount
    componentDidMount() {
        fetch('/api/players/', { 
            method: 'GET',
            dataType: 'json'
        })
        .then(function(response) {
            return response.json()
        })
        .then(j => {
            console.log(j);
            this.setState({
                type: this.props.match.url.split('/')[1],
                data: j,
                filter: j,
                view: j.slice(0, numberPerPage)
            });
        });
    }

     //change what is being displayed in view list based on filter list
     changePage(eventKey) {
        this.setState({
            pageNumber: eventKey,
            view: this.state.filter.slice((eventKey-1) * numberPerPage, eventKey * numberPerPage)
        });
    }

    handleSort(eventKey) {
        //https://stackoverflow.com/questions/979256/sorting-an-array-of-javascript-objects
        var mySort = function(field, reverse, primer){
            var key = primer ? function(x) {return primer(x[field])} : function(x) {return x[field]};
            reverse = !reverse ? 1 : -1;

            return function(a, b) {
                return a = key(a), b = key(b), reverse * ((a > b) - (b > a));
            }
        }
        
        let ekey = parseInt(eventKey);
        let rev = ekey % 2 == 0

        if (Math.floor((ekey + 1) / 2) == 1) {
            var sorted = this.state.filter.sort(mySort('name', rev));
        }
        else if (Math.floor((ekey + 1) / 2) == 2) {
            var sorted = this.state.filter.sort(mySort('skill_rating', rev));
        }
        else if (Math.floor((ekey + 1) / 2) == 3) {
            var sorted = this.state.filter.sort(mySort('wins', rev, function(x){return new Date(x)}));
        }
        console.log(sorted);

        this.setState({
            filter: sorted,
            view: sorted.slice((this.state.pageNumber - 1) * numberPerPage, (this.state.pageNumber) * numberPerPage)
        });
    }

    handlePlatformFilterChange (value) {
        var filtered = value.length == 0 ? this.state.data : this.state.data.filter(player => value.map(x=>x.value).includes(player.platform));        
        this.setState({
            filter: filtered,
            platformFiltersValues: value,
            pageNumber: 1,
            view: filtered.slice(0, numberPerPage),
        });
    }

    //for each value in state, generate a model card
    render() {
        if (this.state.data === null)
            return (<LoadingOverlay />)

        let {platformFiltersValues, view} = this.state
        let platformOptions = [
            {value: 1, label: 'Steam'},
            {value: 2, label: 'Playstation'},
            {value: 3, label: 'Xbox'}
        ]

        // Create the cards before rendering
        var cards = [];
        this.state.view.forEach( function(item) {
            cards.push(<PlayerCard data={item}/>);
        });
        return (
            <div className="container">
                <hr/>
                <h1>Players</h1>
                <hr/>
                <div className="row">
                    <div className="col-md-12 refine-options">
                        <div className="col-md-8">
                        </div>
                        <div className="col-md-3">
                            <Select placeholder="Platform Filter: Any" onChange={this.handlePlatformFilterChange} multi value={platformFiltersValues} options={platformOptions}></Select>                          
                        </div>
                        <div className="col-md-1">
                            <DropdownButton bsStyle="default" title="Sort By: ">
                                <MenuItem header>Name</MenuItem>
                                <MenuItem eventKey="1" onSelect={this.handleSort}>Increasing</MenuItem>
                                <MenuItem eventKey="2" onSelect={this.handleSort}>Decreasing</MenuItem>
                                <MenuItem divider />
                                <MenuItem header>Skill Rating</MenuItem>
                                <MenuItem eventKey="3" onSelect={this.handleSort}>Increasing</MenuItem>
                                <MenuItem eventKey="4" onSelect={this.handleSort}>Decreasing</MenuItem>
                                <MenuItem divider />
                                <MenuItem header>Wins</MenuItem>
                                <MenuItem eventKey="5" onSelect={this.handleSort}>Increasing</MenuItem>
                                <MenuItem eventKey="6" onSelect={this.handleSort}>Decreasing</MenuItem>
                            </DropdownButton>
                        </div>
                    </div>
                </div>
                <div className="">
                    {cards.length === 0 ? "No items to show." : cards}
                </div>
                <div className="text-center">
                    <Pagination
                        bsSize="medium"     
                        items={this.state.filter.length % numberPerPage === 0 ? Math.floor(this.state.filter.length / numberPerPage) : Math.floor(this.state.filter.length / numberPerPage) + 1} 
                        activePage={this.state.pageNumber}
                        onSelect={this.changePage}
                    />
                </div>
            </div>
        )
    }
}

export default Player;