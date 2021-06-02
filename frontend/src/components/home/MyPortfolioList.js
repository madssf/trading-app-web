import React, { Component } from 'react';

import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Container} from "react-bootstrap";

import PortfoliosList from '../portfolios/PortfolioList';
import AddPortfolio from '../portfolios/AddPortfolio';

import TagsList from '../tags/TagsList';

import Sidebar from '../Sidebar';
import { logout } from "../login/LoginActions";

class MyPortfolioList extends Component {
  onLogout = () => {
    this.props.logout();
  };
  render() {
    const { user } = this.props.auth;
    return (
      <div>
        <Sidebar />
        <Container>
          <div className='portfolios'> 
          <h1>Your Portfolios</h1>
          <h3>{user.username}</h3>
          <PortfoliosList />
          <AddPortfolio />

          </div>        
      </Container>
  
    </div>

     
  );
}
}

MyPortfolioList.propTypes = {
  logout: PropTypes.func.isRequired,
  auth: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(mapStateToProps, {
  logout
})(withRouter(MyPortfolioList));
