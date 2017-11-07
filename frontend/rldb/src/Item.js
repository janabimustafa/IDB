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

        this.changePage = this.changePage.bind(this);
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

    //for each value in state, generate a model card
    render() {
        if (this.state.data === null)
            return (<LoadingOverlay />)

        // Create the cards before rendering
        var cards = [];
        this.state.view.forEach( function(item) {
            cards.push(<InstanceCard data={item}/>);
        });
        return (
            <div className="container">
                <h1>{this.state.type.charAt(0).toUpperCase() + this.state.type.slice(1)}</h1>
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