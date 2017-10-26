import React, {Component} from 'react';

import PlayerCard from './PlayerCard';

class Player extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: []
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
        // Create the cards before rendering
        var cards = [];
        this.state.data.forEach( function(item) {
            cards.push(<PlayerCard data={item}/>);
        });
        return (
            <div className="container">
                <h1>Players</h1>
                <div className="row">
                    {cards.length == 0 ? "No items to show." : cards}
                </div>
            </div>
        )
    }
}

export default Player;