import React, { Component } from 'react';

import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { Container, Button} from "react-bootstrap";
import { logout } from "./LoginActions.js";



class Logout extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: ""
    };
  }
  onLogout = () => {
    this.props.logout();
  };

  render() {
    const { user } = this.props.auth;
    return (
      <div>
        <Container>
          <div className='home'> 
          <Button color="primary" onClick={this.onLogout}>Log out</Button>
          <p>{user.username}</p>
          </div>        
          
      </Container>
  
    </div>

     
  );
}
}

Logout.propTypes = {
  logout: PropTypes.func.isRequired,
  auth: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(mapStateToProps, {
})(withRouter(Logout));
