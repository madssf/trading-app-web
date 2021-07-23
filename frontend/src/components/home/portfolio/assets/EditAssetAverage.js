import React from 'react';
import axios from 'axios';
import { toast } from "react-toastify";

import {Container, Button} from "react-bootstrap";
import {toastOnError} from "../../../../utils/Utils";

import "./style.css"
export default class EditAssetAverage extends React.Component {

  constructor(props){
    super(props);
    this.state={
     average: "",
     res: ""
    }
}
  

  handleSubmit = () => {
  const url = `http://localhost:1337/api/v1/portfolio_assets/${this.props.id}/`
  axios.patch(url, {'average': this.state.average}, {headers: {
    'Content-Type': 'application/json'}})
    .then(res => {toast.success(res);})
    .catch(error => {toastOnError(error)});
  }

  handleChange= e => {
    this.setState({ [e.target.name]: e.target.value });
  }

  render() {
    return (
      <div>
      <Container>
      <form>
        <input type="number" name="average" onChange={this.handleChange} value={this.state.average} />
    
        <br></br>
        <Button className="action" disabled={!(this.state.average)} onClick={this.handleSubmit} value="Submit">Edit</Button>
      </form>
      </Container>
    </div>
    )
  }
}