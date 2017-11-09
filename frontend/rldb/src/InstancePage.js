import React, {Component} from 'react';
import InstanceCard from './InstanceCard';
import LoadingOverlay from './LoadingOverlay';
// import {Link} from 'react-router-dom';

class InstancePage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: null,
            itemsData: null,
            crateData: null,
            decalData: null,
            bodyData: null,
            dlcData: null,
            paintData: null
        };
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
            var crates = [];
            var decals = [];
            var bodies = [];
            var paints = [];

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

            if(j.crates !== undefined)
            {
                var cratesPromise = j.crates.map( function(crate) {
                    var uri = '/api/id/' + crate;
                    return fetch(uri, { 
                                        method: 'GET',
                                        dataType: 'json'
                                    })
                                    .then(function(response) {
                                        return response.json()
                                    });
                    });

                Promise.all(cratesPromise).then((result)=>{
                    console.log("All crates fetched!");
                    console.log(result);
                    console.log(typeof(result));                
                    this.setState({
                        crateData : result
                    });
            });}

            if(j.decals !== undefined)
            {
                var decalsPromise = j.decals.map( function(item) {
                    var uri = '/api/id/' + item;
                    return fetch(uri, { 
                                        method: 'GET',
                                        dataType: 'json'
                                    })
                                    .then(function(response) {
                                        return response.json()
                                    });
                    });

                Promise.all(decalsPromise).then((result)=>{
                    console.log("All decals fetched!");
                    console.log(result);
                    console.log(typeof(result));                
                    this.setState({
                        decalData : result
                    });
            });}

            if(j.bodies !== undefined)
            {
                var bodiesPromise = j.bodies.map( function(item) {
                    var uri = '/api/id/' + item;
                    return fetch(uri, { 
                                        method: 'GET',
                                        dataType: 'json'
                                    })
                                    .then(function(response) {
                                        return response.json()
                                    });
                    });

                Promise.all(bodiesPromise).then((result)=>{
                    console.log("All bodies fetched!");
                    console.log(result);
                    console.log(typeof(result));                
                    this.setState({
                        bodyData : result
                    });
            });}
            if(j.dlcs !== undefined)
            {
                var dlcsPromise = j.dlcs.map( function(item) {
                    var uri = '/api/id/' + item;
                    return fetch(uri, { 
                                        method: 'GET',
                                        dataType: 'json'
                                    })
                                    .then(function(response) {
                                        return response.json()
                                    });
                    });

                Promise.all(dlcsPromise).then((result)=>{
                    console.log("All dlcs fetched!");
                    console.log(result);
                    console.log(typeof(result));                
                    this.setState({
                        dlcData : result
                    });
            });}

            if(j.paints !== undefined)
            {
                var paintsPromise = j.paints.map( function(item) {
                    var uri = '/api/id/' + item;
                    return fetch(uri, { 
                                        method: 'GET',
                                        dataType: 'json'
                                    })
                                    .then(function(response) {
                                        return response.json()
                                    });
                    });

                Promise.all(paintsPromise).then((result)=>{
                    console.log("All dlcs fetched!");
                    console.log(result);
                    console.log(typeof(result));                
                    this.setState({
                        paintData : result
                    });
            });}

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

        var crateCards = [];
        if(this.state.crateData !== null)
        {
            this.state.crateData.forEach( function(item) {
                crateCards.push(<InstanceCard key={item.id} data={item}/>);
            });
        }

        var decalCards = [];
        if(this.state.decalData !== null)
        {
            this.state.decalData.forEach( function(item) {
                decalCards.push(<InstanceCard key={item.id} data={item}/>);
            });
        }

        var bodyCards = [];
        if(this.state.bodyData !== null)
        {
            this.state.bodyData.forEach( function(item) {
                bodyCards.push(<InstanceCard key={item.id} data={item}/>);
            });
        }

        var dlcCards = [];
        if(this.state.dlcData !== null)
        {
            this.state.dlcData.forEach( function(item) {
                dlcCards.push(<InstanceCard key={item.id} data={item}/>);
            });
        }

        var paintCards = [];
        if(this.state.paintData !== null)
        {
            this.state.paintData.forEach( function(item) {
                paintCards.push(<InstanceCard key={item.id} data={item}/>);
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
                        <p>{this.state.data.description ? this.state.data.description : "No description for this item."}</p>   
                    </div>
                    <br/>
                    <p className="">Item Type: {this.upperCaseFirst(this.state.data.type)}</p>
                    <p>Release Date: {this.state.data.release_date ? this.state.data.release_date : "Unknown"}</p>
                    <p>Source: {this.state.data.crates.length > 0 ? "Crate" : (this.state.data.dlcs.length > 0 || this.state.data.type == "dlc") > 0 ? "DLC" : "Drop"}</p>
                    <br/>
                </div>
                
                {
                    this.state.data.items !== undefined && this.state.data.items.length > 0 ?
                        <div className="row">
                            <hr/>
                            <h3>Contains:</h3>
                            {itemCards.length > 0 ?
                                itemCards
                            :
                                <LoadingOverlay />}
                        </div>
                            
                        : 
                            ''
                }

                {
                    this.state.data.crates !== undefined && this.state.data.crates.length > 0 ?
                        <div className="row">
                            <hr/>
                            <h3>Crate Source:</h3>
                            {crateCards.length > 0 ?
                                crateCards
                            :
                                <LoadingOverlay />}
                        </div>
                            
                        : 
                            ''
                }

                {
                    this.state.data.dlcs !== undefined && this.state.data.dlcs.length > 0 ?
                        <div className="row">
                            <hr/>
                            <h3>DLC Source:</h3>
                            {dlcCards.length > 0 ?
                                dlcCards
                            :
                                <LoadingOverlay />}
                        </div>
                            
                        : 
                            ''
                }

                {
                    this.state.data.decals !== undefined && this.state.data.decals.length > 0 ?
                        <div className="row">
                            <hr/>
                            <h3>Decals:</h3>
                            {decalCards.length > 0 ?
                                decalCards
                            :
                                <LoadingOverlay />}
                        </div>
                            
                        : 
                            ''
                }
                {
                    this.state.data.bodies !== undefined && this.state.data.bodies.length > 0 ?
                        <div className="row">
                            <hr/>
                            <h3>Bodies:</h3>
                            {bodyCards.length > 0 ?
                                bodyCards
                            :
                                <LoadingOverlay />}
                        </div>
                            
                        : 
                            ''
                }   
                {
                    this.state.data.paints !== undefined && this.state.data.paints.length > 0 ?
                        <div className="row">
                            <hr/>
                            <h3>Paint Finishes:</h3>
                            {paintCards.length > 0 ?
                                paintCards
                            :
                                <LoadingOverlay />}
                        </div>
                            
                        : 
                            ''
                }                          
            </div>
        )
    }
}

export default InstancePage;