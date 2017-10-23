import React, {Component} from 'react';

import InstanceCard from './InstanceCard';

class Crate extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: []
        };
    }
    
    //is it better to do fetch in constructor or in componentDidMount

    componentDidMount() {
        fetch('http://httpbin.org/get', { 
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
        return (
            <div className="container">
                <h1>Crate</h1>
                {Object.keys(this.state.data).map(function(content, i){
                    return <InstanceCard name={content} key={i}/>;
                })}
                <InstanceCard name= "test" />
            </div>
        )
    }
}

export default Crate;