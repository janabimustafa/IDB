import React, {Component} from 'react';

import {Pagination} from 'react-bootstrap';

import InstanceCard from './InstanceCard';
import LoadingOverlay from './LoadingOverlay';

class Item extends Component {
    constructor(props) {
        super(props);

        this.state = {
            type: "",
            data: null,
            filter : [],
            view: [],
            pageNumber: 1
        };
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
                data: j
            });
        });
    }

    //for each value in state, generate a model card
    render() {
        if (this.state.data === null)
            return (<LoadingOverlay />)
        // Create the cards before rendering
        var cards = [];
        this.state.data.forEach( function(item) {
            cards.push(<InstanceCard data={item}/>);
        });
        return (
            <div className="container">
                <h1>{this.state.type.charAt(0).toUpperCase() + this.state.type.slice(1)}</h1>
                <div className="row">
                    {cards.length == 0 ? "No items to show." : cards}
                </div>
            </div>
        )
    }
}

export default Item;