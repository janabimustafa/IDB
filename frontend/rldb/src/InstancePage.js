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
                    data: j,
                    itemsData : result
                });
            });}
            else {
                this.setState({
                    data: j,
                });
            }

        });
    }

    getRarity (rarity_num) {
        if (!rarity_num)
            return "unknown";
        var rarities = ["unknown", "common", "uncommon", "rare", "very rare", "limted", "premium", "import", "exotic", "black market"];
        return rarities[rarity_num];
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
                <div className="row">
                    <div className="col-md-4">
                        <img className="img-rounded img-responsive" src={this.state.data.image} alt="rocket-league-item"/>
                    </div>
                    <h3>Description:</h3>
                    <div className="col-md-8 text-center">
                        <p>{this.state.data.description}</p>   
                    </div>
                    {itemCards.length > 0 ? <h3>Contains:</h3> : <hr/>}                   
                    {itemCards}
                </div>
                
            </div>
        )
    }
}

export default InstancePage;