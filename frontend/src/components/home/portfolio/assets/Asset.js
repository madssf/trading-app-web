import React, { Component } from 'react'
import { toastOnError } from "../../../../utils/Utils";
import axios from 'axios';
import PropTypes from "prop-types";

import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import {getExchanges} from '../../../store/ExchangesActions'
import { Container } from 'react-bootstrap';


class Asset extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "",
      deleteConfirm: false,
    };
  }

  
  componentDidMount() {
    this.props.getExchanges();

    const exchanges = this.props.exchanges.exchanges
    for (var i = 0; i < exchanges.length; i++){

      if (this.props.asset.exchange === exchanges[i].id) {
        this.setState({name: exchanges[i].name})
      }
    }
  }
  
    handleDeleteClick= event => {
      if (this.state.deleteConfirm) {
        this.handleDelete()
      } else {
        this.setState({deleteConfirm: true})
      }
    }
    handleDelete= event => {

      
   
  
      const asset = {
        id: this.props.asset.id, 
       };
      console.log(asset)
  
      axios.delete(`http://localhost:1337/api/v1/portfolio_assets/${asset.id}/`)
        .then(res => {
          window.location.reload();
        }).catch(error => {
          toastOnError(error);
        });
        console.log(asset)
  
      
    }   
  
  render() {
    
  
    return (
      <Container>
      <div className="assetGrid">
        <div className="assetGrid1">
         {this.state.name !== "" ? this.state.name +" ": "unknown"} 
        </div>
        <div className="assetGrid2">
        <b>{Math.round(this.props.asset.value*100)/100} $ </b>
       </div>
       <div className="assetGrid3">
       {this.props.asset.status}    
       </div>
       <div className="assetGrid4">
       {this.props.asset.source}   
       </div>
       <div className="assetGrid5">
       <button className="deleteAssetBtn" onClick={this.handleDeleteClick} type="submit">{this.state.deleteConfirm ? "Confirm" : "Delete"}</button>
       </div>
      </div>      
      </Container>
      
    
    )
  }
}

Asset.propTypes = {
  exchanges: PropTypes.object.isRequired,
  getExchanges: PropTypes.func.isRequired,
}
const mapStateToProps = state => ({
  exchanges: state.exchanges

});
export default connect(mapStateToProps, {getExchanges})(withRouter(Asset))