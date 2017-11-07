import React, {Component} from 'react';

import {Pagination} from 'react-bootstrap';
import InstanceCard from './InstanceCard';
import LoadingOverlay from './LoadingOverlay';
import Select from 'react-select';
import 'react-select/dist/react-select.css';
import './Item.css';

class Item extends Component {
    constructor(props) {
        super(props);

        this.state = {
            type: "",
            data: null,
            filter : [],
            rarityFiltersValues : [], //currently applied filters
            rarityFilter : [], //currently applied filters
            view: [],
            pageNumber: 1
        };

        this.changePage = this.changePage.bind(this);
        this.handleRarityFilterChange = this.handleRarityFilterChange.bind(this);
    }

    componentDidMount() {
        fetch('/api'+ this.props.match.url, { 
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
                view: j.slice(0,9)
            });
        });
    }
    //change what is being displayed in view list based on filter list
    changePage(eventKey) {
        console.log(eventKey);
        this.setState({
            pageNumber: eventKey,
            view: this.state.filter.slice((eventKey-1) * 9, eventKey * 9)
        });
    }
    handleRarityFilterChange (value) {
        
        var filtered = value.length == 0 ? this.state.data : this.state.data.filter(item => value.map(x=>x.value).includes(item.rarity));        
        this.setState({
            filter: filtered,
            rarityFiltersValues: value,
            pageNumber: 1,
            view: filtered.slice(0, 9),
        });
    }
    //for each value in state, generate a model card
    render() {
        console.log("render");
        if (this.state.data === null)
            return (<LoadingOverlay />)
        let {rarityFiltersValues, view} = this.state
        let rarityOptions = [
            {value: 1, label: 'Common'},
            {value: 2, label: 'Uncommon'},
            {value: 3, label: 'Rare'},
            {value: 4, label: 'Very rare'},
            {value: 5, label: 'Limited'},
            {value: 6, label: 'Premium'},
            {value: 7, label: 'Import'},
            {value: 8, label: 'Exotic'},
            {value: 9, label: 'Black market'}
        ]
        
        // Create the cards before rendering
        var cards = view.map(item => (<InstanceCard data={item}/>));
        console.log(cards);
        return (
            <div className="container">
                <div className="row">
                    <div className="col-md-4">
                        <h1>{this.state.type.charAt(0).toUpperCase() + this.state.type.slice(1)}</h1>
                    </div>
                    <div className="col-md-8">
                        <div className="col-md-4 filter-container">
                            <Select placeholder="Rarity Filter: Any" onChange={this.handleRarityFilterChange} multi value={rarityFiltersValues} options={rarityOptions}></Select>
                        </div>
                    </div>
                </div>
                <div className="row">
                    {cards.length == 0 ? "No items to show." : cards}
                </div>
                <div className="text-center">
                    <Pagination
                        bsSize="medium" 
                        items={Math.floor(this.state.filter.length / 9) + 1} 
                        activePage={this.state.pageNumber}
                        onSelect={this.changePage}
                    />
                </div>
            </div>
        )
    }
}

export default Item;