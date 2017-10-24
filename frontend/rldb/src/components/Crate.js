import React, {Component} from 'react';

import InstancePreview from './InstancePreview';

class Crate extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: {}
        };
    }

    componentDidMount() {
        fetch('http://echo.jsontest.com/key/value/one/two', { 
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
    
    render() {
        let data = this.state.data;

        return (
            <div className="container">
                <h1>Crate</h1>
                <InstancePreview name="name" value="value" />
                {Object.keys(data).map((content, i ) => {
                    return <InstancePreview name={content} value={data[content]} key={i} />
                })}
            </div>
        )
    }
}

export default Crate;