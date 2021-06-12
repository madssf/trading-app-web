import React from 'react';
import axios from 'axios';
import {Container, Button} from "react-bootstrap";
import {toastOnError} from "../../../../utils/Utils";

import Dropdown from '../../../ui/Dropdown'
import "./style.css"
export default class AddAsset extends React.Component {

  constructor(props){
    super(props);
    this.state={
     exchange: null,
     data: "",
     res: ""
    }
}
  

  handleSubmit= event => {
  const url = `http://localhost:1337/api/v1/asset/batch_post/${this.props.portfolio}/${this.state.exchange.id}`
  console.log(url)
  axios.post(url, {'data': this.state.data, 'exchange': this.state.exchange.id}, {headers: {
    'Content-Type': 'application/json'
}}).then(res => {this.setState({res: res})
  }).catch(error => {
    toastOnError(error);
  });
}
  handleChange= e => {
    this.setState({ [e.target.name]: e.target.value });

  }

  render() {
    return (
      <div>
      <Container>
      <p>Paste assets [CTRL+V]</p>
      <form>
        <textarea name="data" onChange={this.handleChange} value={this.state.data} style={{width: '200px'}} />
        {this.props.exchanges !== undefined ?
        <Dropdown 
          options={this.props.exchanges} 
          prompt="Select an exchange..."
          id='id'
          label='name'
          value={this.state.exchange}
          onChange={val => this.setState({exchange
            : val})}
          />
        : ""}
        <br></br>
        <Button className="action" disabled={!(this.state.data && this.state.exchange !== null)} onClick={this.handleSubmit} value="Submit">Add</Button>
      </form>
      </Container>
    </div>
    )
  }
}