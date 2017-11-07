import React, {Component} from 'react';

import PlayerCard from './PlayerCard';
import LoadingOverlay from './LoadingOverlay';

class Player extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: null
        };
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
            cards.push(<PlayerCard data={item}/>);
        });
        return (
            <div className="container">
                <hr/>
                <h1>Players</h1>
                <hr/>
                <div className="">
                    {cards.length == 0 ? "No items to show." : cards}
                </div>
            </div>
        )
    }
}

export default Player;