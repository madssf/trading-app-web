import React, { Component } from 'react';

import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Container} from "react-bootstrap";



import { logout } from "../login/LoginActions";

class Home extends Component {
  onLogout = () => {
    this.props.logout();
  };
  render() {
    const { user } = this.props.auth;
    return (
      <div>
        <Container>
          <div className='home'> 
          <h1>Home</h1>
          <p>{user.username}</p>
          </div>        
      </Container>
  
    </div>

     
  );
}
}

Home.propTypes = {
  logout: PropTypes.func.isRequired,
  auth: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(mapStateToProps, {
  logout
})(withRouter(Home));
