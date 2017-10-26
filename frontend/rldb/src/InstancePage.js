import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class InstancePage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: []
        };
    }

    getApiType (type_name) {
        var apiTypes = {"crate":"crates", "paint":"paints", "body":"bodies","player":"players"};
        return apiTypes[type_name];
    } 

    //is it better to do fetch in constructor or in componentDidMount
    componentDidMount() {
        var url = this.props.match.url

        fetch('/api/' + this.getApiType(url.split('/')[1]) + "/" + url.split('/')[2] ), { 
            method: 'GET',
            dataType: 'json'
        }
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

    getRarity (rarity_num) {
        if (!rarity_num)
            return "unknown";
        var rarities = ["unknown", "common", "uncommon", "rare", "very rare", "limted", "premium", "import", "exotic", "black market"];
        return rarities[rarity_num];
    } 

    render() {
        return (
            <div className="container">
                <h1>{this.state.data.name}</h1>
                <div className="row">
                    <div className="col-md-4">
                        <img className="img-rounded img-responsive" src={this.state.data.image}/>
                    </div>
                    <div classNAme="col-md-8">
                        {this.state.data.description}
                    </div>
                <p></p>
            </div>
        )
    }
}

export default InstancePage;