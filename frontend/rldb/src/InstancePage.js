import React, {Component} from 'react';
import InstanceCard from './InstanceCard';
import LoadingOverlay from './LoadingOverlay';
// import {Link} from 'react-router-dom';

class InstancePage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: null,
            itemsData: null
        };
    }

    getApiType (type_name) {
        var apiTypes = {"crate":"crates", "paint":"paints", "body":"bodies","player":"players"};
        return apiTypes[type_name];
    } 

    //is it better to do fetch in constructor or in componentDidMount
    componentDidMount() {
        var url = this.props.match.url

        fetch('/api' + url, { 
            method: 'GET',
            dataType: 'json'
        })
        .then(function(response) {
            return response.json()
        })
        .then(j => {
            console.log(j);
            var items = [];
            if(j.items !== undefined)
            {

            
            var itemsPromise = j.items.map( function(item) {
                var uri = '/api/id/' + item;
                return fetch(uri, { 
                                    method: 'GET',
                                    dataType: 'json'
                                })
                                .then(function(response) {
                                    return response.json()
                                });
                });

            Promise.all(itemsPromise).then((result)=>{
                console.log("All items fetched!");
                console.log(result);
                console.log(typeof(result));                
                this.setState({
                    itemsData : result
                });
            });}

            this.setState({
                data: j,
            });

        });
    }

    getRarity (rarity_num) {
        if (!rarity_num)
            return "unknown";
        var rarities = ["unknown", "common", "uncommon", "rare", "very rare", "limted", "premium", "import", "exotic", "black market"];
        return rarities[rarity_num];
    }

    getRarityColor (raw_rarity) {
        return "color-" + this.getRarity(raw_rarity);
    }

    upperCaseFirst(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }

    /* This could be useful.
        var content = this.state.data;
        {Object.keys(content).map(function(key, index) {
            if(!(content[key] === null)){
                return <h3>{key}: {content[key]} </h3>
            }
        })}
    */

    render() {
        if (this.state.data === null)
            return (<LoadingOverlay />)
        
        var itemCards = [];
        if(this.state.itemsData !== null)
        {
            this.state.itemsData.forEach( function(item) {
                itemCards.push(<InstanceCard key={item.id} data={item}/>);
            });
        }

        return (
            <div className="container">
                {/* <Link to={'/'+ this.props.match.url.split('/')[1]}>
                    <h3>Go back.</h3>
                </Link> */}
                <h1>{this.state.data.name}</h1>
                <h3 className={this.getRarityColor(this.state.data.rarity)}> {this.getRarity(this.state.data.rarity).toUpperCase()}</h3>
                <div className="row">
                    <div className="col-md-4">
                        <img className="img-rounded img-responsive" src={this.state.data.image} alt="rocket-league-item"/>
                    </div>
                    <h3>Description:</h3>
                    <div className="">
                        <p>{this.state.data.description}</p>   
                    </div>
                    <br/>
                    <p className="">Item Type: {this.upperCaseFirst(this.state.data.type)}</p>
                    <p>Release Date: {this.state.data.release_date ? this.state.data.release_date : "Unknown"}</p>
                    <p>Source: {this.state.data.crates.length > 0 ? "Crate" : "Drop"}</p>
                </div>
                
                    {
                        itemCards.length > 0 ?
                            <div className="row">
                                <hr/>
                                <h3>Contains:</h3> 
                                {itemCards}
                            </div>
                                
                            : 
                                ''
                    }                   
                    
                
                
            </div>
        )
    }
}

export default InstancePage;